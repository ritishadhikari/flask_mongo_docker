import os
from flask import Flask, redirect, url_for, request,render_template
from flask_pymongo import PyMongo
from pymongo import MongoClient

app=Flask(__name__)
# app.config['MONGO_URI']="mongodb://mongo:27017/mongodb_test"
# mongo=PyMongo(app)
# db=mongo.db

client = MongoClient('mongodb://mongodb:27017/')
db = client.tododb

@app.route('/')
def todo():
    _items=db.tododb.find()
    items=[item for item in _items]

    return render_template('todo.html',items=items)


@app.route('/new',methods=['POST'])
def new():
    item_doc={
    'name':request.form['name'],
    'description':request.form['description']
    }
    db.tododb.insert_one(item_doc)
    return redirect(url_for('todo'))

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)
