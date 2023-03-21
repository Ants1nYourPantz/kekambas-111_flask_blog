from app import app
from flask import render_template


@app.route('/')
def index(): 
    return render_template('index.html')


@app.route('/test')
def hello_test(): 
    return 'This is a test!'