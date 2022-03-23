from flask import Flask, render_template, request
from data.processor import Processor
import json
from types import SimpleNamespace

app = Flask(__name__)


@app.route('/')
def root():
    return '<h1>Hello World!</h1><p>Welcome to the world of Flask!</p>'


@app.route('/hello')
@app.route('/hello/<user>')
def hello_world(user=None):
    user = Processor.do_smth
    user = user or 'Anonymous'
    if request.args.get('user') is not None:
        user = request.args.get('user')
    return render_template('index.html', user=user)


@app.route('/api/hello/<user>')
def hello_json(user=None):
    user = user or 'Anonymous'
    return {
        "username": user,
        "message": 'hello world'
    }


@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    name = data.get('name')
    password = data.get('password')

    x = json.loads(request.data, object_hook=lambda d: SimpleNamespace(**d))
    print(x.name, x.password)

    return {
        "username": name,
        "hash" : hash(password),
        "message": 'Success'
    }, 200


@app.route('/search', methods=['GET', 'POST'])
def search_form():
    if request.method == 'POST':
        data = 'Result: '+request.form.get('search')
        return render_template('search.html', data=data)
    return render_template('search.html')

if __name__ == '__main__':
    app.run()
