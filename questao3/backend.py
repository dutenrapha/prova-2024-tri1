from flask import Flask, request
from frontend import generate_frontend

app = Flask(__name__)

names = []

@app.route('/')
def index():
    return generate_frontend(names)

@app.route('/add_name', methods=['POST'])
def add_name():
    name = request.form['name']
    names.append(name)
    return generate_frontend(names)

if __name__ == '__main__':
    app.run(debug=True)
