from flask import request, g
from responses.resp import *

def json_checker(data):
    return "user" in data and "topic" in data


def topic_add():
    if request.method == 'POST':
        data = request.json
        if len(data) != 2 or not json_checker(data):
            return error_response("incorrect parameters")
        user = data['user']
        topic = data['topic']
       #inserting
        cur = g.db.cursor()
        try:
            cur.execute(f"insert into {user}_topic(topic) values('{topic}')")
            cur.execute(f"create table {user}_{topic} (id serial primary key, stopic text, description text, resource text);")
            cur.close()
            g.db.commit()
        except:
            return error_response("No user found")
        return success_message("Successfully Added!")

    else:
        return error_response("bad requset")
