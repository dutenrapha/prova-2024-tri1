from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista de tarefas
tasks = [
    {"id": 1, "description": "Fazer compras", "assigned_to": "João"},
    {"id": 2, "description": "Estudar Python", "assigned_to": "Maria"}
]

# Rota para deletar uma tarefa
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({"message": "Tarefa deletada com sucesso"}), 200

if __name__ == '__main__':
    app.run(debug=True)
# Rota para editar uma tarefa
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def edit_task(task_id):
    global tasks
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = request.json.get('description', task['description'])
            task['assigned_to'] = request.json.get('assigned_to', task['assigned_to'])
            return jsonify({"message": "Tarefa editada com sucesso"}), 200
    return jsonify({"error": "Tarefa não encontrada"}), 404


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)

