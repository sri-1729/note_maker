import psycopg2
from flask import g 
from flask.cli import with_appcontext

host = "127.0.0.1"
port = "5432"
user = "srijith"
password = "postgres123"
TABLE = "user_topic"

def connect_db():
    if 'db' not in g:
        g.db = psycopg2.connect(dbname="notes", user=user, password=password, host=host, port=port)
    return g.db
