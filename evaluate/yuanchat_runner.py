import clueai
import time
# initialize the Clueai Client with an API Key
# generate a prediction for a prompt 
# 需要返回得分的话，指定return_likelihoods="GENERATION"
def run_yuan(data_set , model_conf):
    cl = clueai.Client('YdoL3QFVkKOTHrjMX24NX1010000100010', check_api_key=True)
    prompt= '用户：%s 小元：'
    ret_list = []
    if model_conf and 'api_key' in model_conf:
        cl = clueai.Client('YdoL3QFVkKOTHrjMX24NX1010000100010', check_api_key=True)
    for example in data_set:
        question_id, question_type, query , answer_type, answer = example
        query = prompt % query
        response = cl.generate(
            model_name='ChatYuan-large',
            prompt=query)
            
        response = response.generations[0].text
        time.sleep(5)
        ret_list.append(response)
    return ret_list    



