import os
import openai
import json
import random
import time

openai.api_key = "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"
#openai.api_key = "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"
openai.api_base = 'http://47.251.17.1:9000/v1'

def chat_openai(question):
    retry_count = 0
    while retry_count < 3:
        try:
            ret = openai.Completion.create(
            model="text-davinci-003",
            temperature = 0.2,
            max_tokens = 250 ,
            top_p=1.0,
            n = 1,
            stream =False,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            prompt=question
            )
            break
        except Exception as e:
            print(str(e))
            retry_count += 1
            time.sleep(3)
            ret = None
    if ret:        
        return ret['choices'][0]['text']
    else:
        return ret



def gen_record(query_string):
    user_str = {"role":"user" , "content":query_string}
    return user_str

def run_dvc(data_set , model_conf):
    ret_list = []
    if model_conf and 'api_key' in model_conf:
        openai.api_key =  model_conf['api_key']

    for example in data_set:
        question_id, question_type, query , answer_type, answer = example
        prompt = query
        #prompt.append(gen_record(query))
        response = chat_openai(prompt)
        response = response.replace("\n",'\\n')
        ret_list.append(response)
    return ret_list    
        






