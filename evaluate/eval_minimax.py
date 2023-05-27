# -*- coding: utf-8 -*-
import requests
import readline
from generate_prompt import generate_prompt
def preprocess():
    """
    返回调用minimax的headers和url
    """
    group_id = "1684389779754504"
    api_key = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJTdWJqZWN0SUQiOiIxNjg0Mzg5Nzc5OTM0MTkyIiwiUGhvbmUiOiJNVE14TmpJek56RXlNRFk9IiwiR3JvdXBJRCI6IiIsIlBhZ2VOYW1lIjoiIiwiTWFpbCI6ImN5cmlzLmhlY0AxZGF0YS5pbmZvIiwiaXNzIjoibWluaW1heCJ9.GNva_1mMPQXa4YVsUNPecmXCNMUtrOfOcvckh9a0IFRJfxdK9U88kE4XYIRw2d9MW8yM0sBsp1fOkGJv31lTMkK8xpMCtu8w29vB3ZAX09y44U9je4FTp7jiou5sIW9DdhgmmHetStuK7TNoLKqwRHF2hW05mfLh5loSmEQId3rU5FsVvQZU4q-4IgXDgHcH3siON36FN4X_OeJKG-BSHdEul62Ti_tjaaanPwUeL15eTOlKwawDbqnwdIZNZEEf0YRrBlHBgf4b0OhQVZUgwfuE_iz4qEXA-eFFc34Z5cGlyNzpzsM-RxYZ2AZ7SCa2l3ThKvOKplzSFD6mcQAhGA"

    url = f"https://api.minimax.chat/v1/text/chatcompletion?GroupId={group_id}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    return headers, url

def run_minimax(data_set, model_conf=None):
    ret_list = []
    headers, url = preprocess()
    for index, example in enumerate(data_set):
        # prefix, user_name, bot_name = choose_prefix()
        # tokens_to_generate可自行修改，范围为0-4096
        request_body = {
            "model": "abab5-chat",
            "tokens_to_generate": 512,
            "messages": []
        }
        question_id, question_type, question, answer_type, answer = example
        # print(f'The {index}th question: {question}\n')
        # print(f'The {index}th answer: {answer}\n')
        input_text = generate_prompt(question, question_type, None)
        request_body["messages"].append({
            "sender_type": "USER",
            "text": input_text
        })
        response = requests.post(url, headers=headers, json=request_body)
        reply = response.json()["reply"]

        # print(f'The {index}th response: {reply}\n')
        ret_list.append(reply)
    return ret_list


# # 添加循环完成多轮对话
# while True:
#     line = input("发言：")
#     request_body["messages"].append({
#         "sender_type": "USER",
#         "text": line
#     })
#     response = requests.post(url, headers=headers, json=request_body)
#     reply = response.json()["reply"]
#     print(f"reply: {reply}")
#
#     # 将返回的输出当成输入再次加入messages
#     request_body["messages"].append({
#         "sender_type": "BOT",
#         "text": reply
#     })
