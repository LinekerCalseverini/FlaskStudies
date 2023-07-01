from flask import (Flask, jsonify, request, url_for, redirect, session,
                   render_template)
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'Thisisasecret!'


@app.route('/')
def index():
    session.pop('name', None)
    return '<h1>Hello, World!</h1>'


@app.route('/home', methods=['POST', 'GET'], defaults={'name': ''})
@app.route('/home/<string:name>', methods=['POST', 'GET'])
def personal_home(name):
    if not name:
        return '<h1>You are on the home page!</h1>'

    session['name'] = name
    return render_template('home.html', name=name)


@app.route('/json')
def json():
    json_object = {'key': 'value', 'key2': [1, 2, 3]}
    if 'name' in session:
        json_object['name'] = session['name']
    return jsonify(json_object)


@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return (f'<h1>Hi {name}, you are from {location}. You are on the query '
            'page.</h1>')


@app.route('/theform', methods=['GET', 'POST'])
def theform():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        name = request.form['name']
        # location = request.form['location']
        # return (f'<h1>Hi {name}, you are from {location}. You have submitted'
        #         ' the form successfully!</h1>')

        return redirect(url_for('personal_home', name=name))


# @app.route('/process', methods=['POST'])
# def process():
#     name = request.form['name']
#     location = request.form['location']
#     return (f'<h1>Hi {name}, you are from {location}. You have submitted the'
#             ' form successfully!</h1>')


@app.route('/processjson', methods=['POST'])
def processjson():
    data = request.get_json()
    name = data['name']
    location = data['location']
    return jsonify({'result': 'Success',
                    'name': name,
                    'location': location})


if __name__ == '__main__':
    app.run(port=80)
