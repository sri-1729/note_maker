from flask import request, g
import json
from responses.resp import *

def stopic_get(user, topic):
    curr = g.db.cursor()
    try:
        curr.execute(f"select stopic from {user}_{topic}")
        x = curr.fetchall()
        final = []
        for each in x:
            final.append({"name":each[0]})
        return success_message(final)
    except:
        return error_response("not found")

