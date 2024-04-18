from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista de eventos com exemplo de participantes
events = [
    {"id": 1, "description": "Event 1", "date": "2024-04-20", "start_time": "10:00", "participants": ["John", "Alice"]},
    {"id": 2, "description": "Event 2", "date": "2024-04-22", "start_time": "14:00", "participants": ["Bob", "Eve"]}
]

# Rota para obter todos os eventos
@app.route('/events', methods=['GET'])
def get_events():
    return jsonify(events)

# Rota para adicionar participante a um evento
@app.route('/events/<int:event_id>/add_participant', methods=['POST'])
def add_participant(event_id):
    data = request.json
    participant_name = data.get('name')
    for event in events:
        if event['id'] == event_id:
            event['participants'].append(participant_name)
            return jsonify({'message': 'Participant added successfully'}), 200
    return jsonify({'error': 'Event not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
