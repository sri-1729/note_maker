from flask import Flask, g
from data.config import *
from responses.resp import *
import api.topic_get
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

@app.route('/topics/add')
def add_topic():
    return api.addTopic()

@app.route('/<user>/topics/get')
def fetch_topic(user):
    return api.topic_get.get_topics(user)

@app.after_request
def ar(response):
    return response
