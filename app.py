import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://datastore:27017/dockerdemo')
db = client.tododb

@app.route('/')
def todo():

    _items = db.tododb.find()
    items = [item for item in _items]
    
    return render_template('todo.html', items=items)

    return "Hello!"

@app.route('/new', methods=['POST'])
def new():
    
    item_doc = {
        'firstName': request.form['firstName'],
        'lastName': request.form['lastName'],
        'age': request.form['age'],
        'gender': request.form['gender'],
        'email': request.form['email'],
        'registrationDate': request.form['registrationDate'],
    }

    db.tododb.insert_one(item_doc)

    return redirect(url_for('todo'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
