from flask import g
from responses.resp import *
import json

def get_topics(user):
    curr = g.db.cursor()
    try:
        curr.execute(f"SELECT * FROM {user}_topic")
        x = curr.fetchall()
        final = []
        for each in x:
            final.append({"id":each[0], "topic":str(each[1])})
        return success_message(final)
    except:
        return error_response("not found")

