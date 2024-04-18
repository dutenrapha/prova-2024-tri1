from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Lista de perguntas
questions = [
    {"text": "What is the capital of France?", "options": ["London", "Berlin", "Paris", "Rome", "Madrid"], "answer": 2},
    {"text": "What is 2 + 2?", "options": ["3", "4", "5", "6", "2"], "answer": 1},
    {"text": "Who wrote 'Macbeth'?", "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Leo Tolstoy", "Mark Twain"], "answer": 1},
    {"text": "Which planet is known as the Red Planet?", "options": ["Earth", "Venus", "Mars", "Jupiter", "Saturn"], "answer": 2},
    {"text": "What is the largest ocean on Earth?", "options": ["Atlantic", "Indian", "Arctic", "Pacific", "Southern"], "answer": 3}
]

@app.route("/questions/")
def get_questions():
    return jsonify([question for question in questions])

@app.route("/submit/", methods=["POST"])
def submit_answers():
    user_answers = request.get_json()["answers"]
    score = sum(1 for i, answer in enumerate(user_answers) if answer == questions[i]["answer"])
    return jsonify({"score": score, "total": len(questions)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
