import time
from llm_db  import insert_record 
def submit_task_info(eval_id ,eval_models_list , data_set , owner , tag ):
    question_num = len(data_set)
    model_num = len(eval_models_list)
    sql = 'insert into task_info_table (eval_task_id , task_tag , task_owner , question_num , model_num , submit_time ) values (%s,%s,%s,%s,%s,NOW());'
    params = (eval_id ,tag , owner , question_num , model_num )
    return insert_record(sql,params)
       


