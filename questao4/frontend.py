<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Event Management</title>
</head>
<body>
    <h1>Event Management</h1>
    <ul id="event-list"></ul>

    <script>
        // Função para carregar eventos da API
        function loadEvents() {
            fetch('/events')
                .then(response => response.json())
                .then(events => {
                    const eventList = document.getElementById('event-list');
                    eventList.innerHTML = '';
                    events.forEach(event => {
                        const li = document.createElement('li');
                        li.textContent = `${event.description} - Date: ${event.date}, Time: ${event.start_time}`;
                        const addButton = document.createElement('button');
                        addButton.textContent = 'Add Participant';
                        addButton.addEventListener('click', () => addParticipant(event.id));
                        li.appendChild(addButton);
                        eventList.appendChild(li);
                    });
                })
                .catch(error => console.error('Error loading events:', error));
        }

        // Função para adicionar participante a um evento
        function addParticipant(eventId) {
            const participantName = prompt('Enter participant name:');
            if (participantName) {
                fetch(`/events/${eventId}/add_participant`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ name: participantName })
                })
                .then(response => {
                    if (response.ok) {
                        alert('Participant added successfully');
                    } else {
                        alert('Failed to add participant');
                    }
                })
                .catch(error => console.error('Error adding participant:', error));
            }
        }

        // Carregar eventos ao carregar a página
        document.addEventListener('DOMContentLoaded', () => {
            loadEvents();
        });
    </script>
</body>
</html>
