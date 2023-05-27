import pymysql


def get_connect():
    mysql_conn = pymysql.connect(host='10.10.129.241', port=13306, user='llm_user', password='llm_passwd',
                                 db='llm_eval')
    return mysql_conn


def fetch_record(query, params):
    con = get_connect()
    cursor = con.cursor()
    new_query = query % params
    cursor.execute(query, params)
    query_result = cursor.fetchall()
    return query_result


def insert_record(sql, params):
    if sql:
        # try:
        conn = get_connect()
        cursor = conn.cursor()
        cursor.execute(sql, params)
        conn.commit()
        return True
    else:
        # except Exception as e:
        #    print(str(e))
        return False


def insert_batch(sql):
    if sql:
        # try:
        conn = get_connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        return True
    else:
        # except Exception as e:
        #    print(str(e))
        return False


def update_record(query,params):
    conn = get_connect()
    cursor = conn.cursor()
    if True:
    #try:
        cursor.execute(query,params)
        conn.commit()
        return True
    # except Exception as e:
    else:
        #    print(str(e))
        return False
