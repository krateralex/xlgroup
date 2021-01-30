from flask import Flask, request, make_response, redirect, abort
from flask_script import Manager
app = Flask(__name__)
manager = Manager(app)

'''
#Пример 1
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

#Пример 2
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello %s!</h1>' % name

#Пример 3
@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s.</p>' % user_agent

#Пример 4
@app.route('/')
def index():
    return '<h1>Bad Request</h1>', 400

#Пример 5
@app.route('/')
def index():
    response = make_response('This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response


#Пример 6 (улучшенная версия Пример 4)
@app.route('/')
def index():
    response = make_response('')
    return '<h1>Status Code - %s</h1>' % response.status_code

#Пример 7
@app.route('/')
def index():
    return redirect('http://www.example.com')
'''
#Пример 8
class User():
    def __init__(self, i, n=''):
        self.id = i
        self.name = n

def load_user(id):
    user = User(id)
    if int(user.id) > 0 and int(user.id) < 10:
        user.name = 'Junior'
    elif int(user.id) >= 10 and int(user.id) <= 100:
        user.name = 'Master'
    else:
        return False
    return user

@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, %s</h1>' % user.name

"""
@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    return '<h1>Hello %s!</h1>' % user.name
"""

if __name__ == '__main__':
    #app.run(debug=True)
    manager.run()
