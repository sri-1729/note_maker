from flask import g
from responses.resp import *
def stopic_det(user, topic, name):
    cur = g.db.cursor()
    cur.execute(f"select * from {user}_{topic} where stopic = '{name}'")
    x = cur.fetchone()
    try:
        data = {"name" : x[1], "description": x[2], "resource" : x[3]}
        return success_message(data)
    except:
        return error_response("not found")
