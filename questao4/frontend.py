import flet as ft
import requests

def main(page: ft.Page):
    page.title = "To-Do List"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    def add_task():
        task_text = input_field.value.strip()
        if task_text:
            try:
                response = requests.post("http://localhost:8000/tasks/", json={"task": task_text})
                result = response.json()
                message_text.value = result["message"]
                message_text.update()
                input_field.value = ""  # Limpar o campo de entrada após adicionar a tarefa
            except Exception as ex:
                message_text.value = f"Error: {ex}"
                message_text.update()

    def get_tasks():
        try:
            response = requests.get("http://localhost:8000/tasks/")
            result = response.json()
            tasks = result.get("tasks", [])
            task_list.value = "\n".join(tasks)
            task_list.update()
        except Exception as ex:
            message_text.value = f"Error: {ex}"
            message_text.update()

    input_field = ft.Input(placeholder="Enter task...")
    add_button = ft.ElevatedButton("Add Task", on_click=add_task)
    get_button = ft.ElevatedButton("Get Tasks", on_click=get_tasks)
    message_text = ft.Text("", margin=10)
    task_list = ft.Text("")

    page.add(input_field)
    page.add(add_button)
    page.add(get_button)
    page.add(message_text)
    page.add(task_list)

if __name__ == "__main__":
    ft.app(target=main)