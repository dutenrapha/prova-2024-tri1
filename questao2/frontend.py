from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('http://localhost:8080/questions/')
    questions = response.json()
    return render_template('index.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    user_answers = [int(answer) for answer in request.form.values()]
    response = requests.post('http://localhost:8080/submit/', json={"answers": user_answers})
    result = response.json()
    return render_template('result.html', score=result['score'], total=result['total'])

if __name__ == '__main__':
    app.run(debug=True)
