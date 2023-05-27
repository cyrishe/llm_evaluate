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
            max_tokens = 250 ,
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


type_class = 0
#for query_string,query_lang in all_list:
#for line in open('std_questions','r').readlines():
for line in open('rest','r').readlines():
    query = line.rstrip("\n")
    if query == '':
        type_class+=1
        continue
    prompt = []
    prompt.append(gen_record(query))
    response = chat_openai(prompt)
    time.sleep(31)
    if not response:
        print(str(type_class)+"|"+query+"|request failed")
        continue
    response = response.replace("\n",'\\n')
    print(str(type_class)+"|"+query+"|"+response)






