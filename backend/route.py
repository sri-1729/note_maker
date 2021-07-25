from flask import Flask, g
from data.config import *
from responses.resp import *
import api.topic_get
import api.topic_add
import api.stopic_add
import api.stopic_get
import api.stopic_det
app = Flask("notes_api")

@app.before_request
def br():
    g.db = connect_db()

@app.route('/<user>')
def create_topics(user):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(f"create table if not exists {user}_topic(id serial primary key,topic text);")
    cur.close()
    conn.commit()
    return success_message(f"created {user} table successfully")

@app.route('/topics/add', methods=['POST'])
def add_topic():
    return api.topic_add.topic_add()

@app.route('/<user>/topics/get')
def fetch_topic(user):
    return api.topic_get.get_topics(user)

@app.route('/<user>/topic/stopics/add', methods = ['POST'])
def add_stopic(user):
    return api.stopic_add.stopic_add(user)

@app.route('/<user>/<topic>/stopics')
def get_stopics(user, topic):
    return api.stopic_get.stopic_get(user, topic)

@app.route('/<user>/<topic>/stopics/<name>')
def get_details(user, topic, name):
    return api.stopic_det.stopic_det(user, topic, name)

@app.after_request
def ar(response):
    return response
