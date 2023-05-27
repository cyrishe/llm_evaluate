import os,sys
import platform
import signal
from transformers import AutoTokenizer, AutoModel
import json


if len(sys.argv) == 2:
    f = sys.argv[1]
else:
    f = 'std_questions'



#tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True)
#model = AutoModel.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True).half().cuda()
model_path='ptuning/output/adgen-chatglm-6b-pt-8-1e-2/checkpoint-1000/'
model_path='ptuning/output/new-8-1e-2/checkpoint-100/'
model_path='ptuning/output/new1-8-1e-2/checkpoint-500'
model_path='../../freight_assistant_model/ptuning/glm_ori/'
#model_path='ptuning/output/new1-8-1e-2/checkpoint-1000'
#model_path='ptuning/output/new1-8-1e-2/checkpoint-1600'
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
#model = AutoModel.from_pretrained(model_path, trust_remote_code=True)
model = AutoModel.from_pretrained(model_path, trust_remote_code=True).half().cuda()
model = model.eval()

os_name = platform.system()
clear_command = 'cls' if os_name == 'Windows' else 'clear'
stop_stream = False


def build_prompt(history):
    prompt = "欢迎使用 ChatGLM-6B 模型，输入内容即可进行对话，clear 清空对话历史，stop 终止程序"
    for query, response in history:
        prompt += f"\n\n用户：{query}"
        prompt += f"\n\nChatGLM-6B：{response}"
    return prompt


def signal_handler(signal, frame):
    global stop_stream
    stop_stream = True


def main():
    type_class = 0
    history = []
    for line in open(f,'r').readlines():
        query = line.rstrip("\n")
        if query == '':
            type_class+=1
            continue
        response, history = model.chat(tokenizer, query, history=[])
        response = response.replace("\n",'\\n')
        print(str(type_class)+"|"+query+"|"+response)


if __name__ == "__main__":
    main()
