from flask import g, request
from responses.resp import *

def stopic_add(user):
    if request.method == 'POST':
        data = request.json
        topic = data['topic']
        stopic = data['stopic']
        descr = data['description']
        res = data['resource']
        cur = g.db.cursor()
        cur.execute(f"insert into {user}_{topic}(stopic, description, resource) values('{stopic}','{descr}','{res}')")
        cur.close()
        g.db.commit()
        return success_message("Successfully Added!")
