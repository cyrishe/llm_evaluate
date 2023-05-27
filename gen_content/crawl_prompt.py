import os
import openai
import json
import random
import time

#openai.api_key = "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"
openai.api_key = "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"
openai.api_base = 'http://47.251.17.1:9000/v1'

def chat_openai(question):
    retry_count = 0
    while retry_count < 3:
        try:
            ret = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature = 0.2,
            max_tokens = 1000 ,
            messages=question
            )
            break
        except Exception as e:
            print(str(e))
            retry_count += 1
            time.sleep(35)
            ret = None
    if ret:        
        return ret['choices'][0]['message']['content']
    else:
        return ret



def gen_record(query_string):
    user_str = {"role":"user" , "content":query_string}
    return user_str

def gen_prompts(all_list):
    prompts = []
    for i in range(10):
        prompt = seed(all_list)
        prompts.append(prompt)
    return prompts    


topic_dic = {}
topic_dic['货代'] = 20
topic_dic['零售'] = 20
topic_dic['电商'] = 20
topic_dic['运营'] = 20
topic_dic['新能源'] = 20
topic_dic['科技'] = 20
topic_dic['数学'] = 20
topic_dic['运筹学'] = 20
topic_dic['物理学'] = 20
topic_dic['BI'] = 20
#for query_string,query_lang in all_list:
#for line in open('std_questions','r').readlines():
for key in topic_dic:
    count = topic_dic[key]
    query = '请列举'+str(count)+'个'+key+'这个领域的概念词，输出在一行里，按照空格分隔即可'
    prompt = []
    prompt.append(gen_record(query))
    response = chat_openai(prompt)
    time.sleep(31)
    if not response:
        print(str(type_class)+"|"+query+"|request failed")
        continue
    response = response.replace("\n",'\\n')
    print(key+"|"+response)






