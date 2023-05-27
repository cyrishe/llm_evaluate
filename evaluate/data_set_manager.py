from llm_db  import fetch_record


def get_data_set(data_set):
    sql = "select question_id , question_type , question , answer_type , answer from question_table where `group` = %s and in_use = 1"
    data_set  = fetch_record(sql , (data_set))
    return data_set


