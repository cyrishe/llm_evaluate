from model_base_runner import model_run
from answer_judger import answer_judger
import json
import time
from llm_db import insert_batch, update_record
import argparse
from pymysql.converters import escape_string

DETAIL_INFO_SQL = 'insert into eval_detail_table (question_id , question_type , question , answer_type , answer , model_name , eval_task_id , model_result ,eval_score ) VALUES '

TASK_STATUS_SQL = "update `task_info_table` set `task_status` = %s where `eval_task_id` = %s ;"


class eval_runner:
    def __init__(self, eval_id, data_set, model_list):
        self.data_set = data_set
        self.model_list = model_list
        self.eval_id = eval_id
        f = open('config/models.conf.json', 'r')
        self.model_conf = json.load(f)

    # 评判答案，并且入库
    def answer_scoring(self, qa_pair, eval_model_name):
        value_sql = ''
        for q, model_answer in qa_pair:
            question_id, question_type, question, answer_type, answer = q
            score = answer_judger(answer, model_answer, answer_type)
            record_str = "( %d , '%s' , '%s' ,'%s' , '%s' , '%s' , %d , '%s' , %d)" % \
                         (question_id, question_type, escape_string(question), answer_type, answer,
                          escape_string(eval_model_name),
                          self.eval_id, escape_string(model_answer), score)
            print(f'record_str: {record_str}\n')
            value_sql = value_sql + "\n" + record_str + ","
        value_sql = DETAIL_INFO_SQL + value_sql[:-1] + ";"
        print(f'value_sql: {value_sql}\n')
        insert_batch(value_sql)

    # finish task , and change task status to finish
    # if error , set the abnormal status to inform user
    def change_task_status(self, status):
        params = [status, self.eval_id]
        print(TASK_STATUS_SQL)
        print(params)
        update_record(TASK_STATUS_SQL, params)
        return 0

    def run(self):
        try:
            for m in self.model_list:
                if m not in self.model_conf:
                    continue
                model_conf = self.model_conf[m]
                print("evalating model:" + m)
                ret_list = model_run(m, self.data_set, model_conf)
                # print(ret_list)
                time.sleep(10)
                q_a_pair = zip(self.data_set, ret_list)
                self.answer_scoring(q_a_pair, m)
            self.change_task_status(1)
        except:
            self.change_task_status(-1)


if __name__ == '__main__':
    from data_set_manager import get_data_set

    parser = argparse.ArgumentParser()
    parser.add_argument('--eval_id', default=None, type=int, required=True)
    parser.add_argument('--model_list', default=None, type=str, help="If None, perform inference on the base model")
    parser.add_argument('--data_set', default=None, type=str)
    parser.add_argument('--owner', default=None, type=str)
    parser.add_argument('--tag', default=None, type=str)
    args = parser.parse_args()
    data_set = get_data_set(args.data_set)
    model_list = args.model_list.split(",")
    print(model_list)
    eval_runner = eval_runner(args.eval_id, data_set, model_list)
    eval_runner.run()

    # eval_runner = eval_runner(1684491218812, 'default', ['llama'])
    # eval_runner.change_task_status(1)

