from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def root():
    return '<h1>Hello World!</h1><p>Welcome to the world of Flask!</p>'


@app.route('/hello')
@app.route('/hello/<user>')
def hello_world(user=None):
    user = user or 'Anonymous'
    return render_template('index.html', user=user)


@app.route('/api/hello/<user>')
def hello_json(user=None):
    user = user or 'Anonymous'
    return {
        "username": user,
        "message": 'hello world'
    }


if __name__ == '__main__':
    app.run()
