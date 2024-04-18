from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista de tarefas com exemplo de prioridade
tasks = [
    {"id": 1, "description": "Task 1", "priority": "low"},
    {"id": 2, "description": "Task 2", "priority": "medium"},
    {"id": 3, "description": "Task 3", "priority": "high"}
]

# Rota para obter todas as tarefas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(debug=True)
