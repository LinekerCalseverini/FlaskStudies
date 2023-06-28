from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'


@app.route('/home', methods=['POST', 'GET'], defaults={'name': ''})
@app.route('/home/<name>', methods=['POST', 'GET'])
def personal_home(name):
    if not name:
        return '<h1>You are on the home page!</h1>'

    return f'<h1>Hello, {name}. You are on the home page!</h1>'


@app.route('/json')
def json():
    return jsonify({'key': 'value', 'key2': [1, 2, 3]})


@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return (f'<h1>Hi {name}, you are from {location}. You are on the query '
            'page.</h1>')


@app.route('/theform')
def theform():
    return ('<form method="POST" action="/process">'
            '<input type="text" name="name">'
            '<input type="text" name="location">'
            '<input type="submit" value="Submit">'
            '</form>')


@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    location = request.form['location']
    return (f'<h1>Hi {name}, you are from {location}. You have submitted the '
            'form successfully!</h1>')


@app.route('/processjson', methods=['POST'])
def processjson():
    data = request.get_json()
    name = data['name']
    location = data['location']
    return jsonify({'result': 'Success',
                    'name': name,
                    'location': location})
