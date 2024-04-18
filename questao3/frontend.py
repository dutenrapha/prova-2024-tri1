<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>To-Do List with Priority</title>
</head>
<body>
    <h1>To-Do List with Priority</h1>
    <ul id="task-list"></ul>

    <script>
        // Função para carregar tarefas da API
        function loadTasks() {
            fetch('/tasks')
                .then(response => response.json())
                .then(tasks => {
                    const taskList = document.getElementById('task-list');
                    taskList.innerHTML = '';
                    tasks.forEach(task => {
                        const li = document.createElement('li');
                        li.textContent = `${task.description} - Priority: ${task.priority}`;
                        taskList.appendChild(li);
                    });
                })
                .catch(error => console.error('Error loading tasks:', error));
        }

        // Carregar tarefas ao carregar a página
        document.addEventListener('DOMContentLoaded', () => {
            loadTasks();
        });
    </script>
</body>
</html>
