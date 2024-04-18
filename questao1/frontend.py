import flet as ft
import requests

def main(page: ft.Page):
    page.title = "To-Do List App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    input_text = ft.TextField(hint_text="Add a new task", width=300, autofocus=True)
    assigned_dropdown = ft.Dropdown(
        label="Assign to:",
        options=[
            ft.dropdown.Option("Carlos"),
            ft.dropdown.Option("Carlão"),
            ft.dropdown.Option("Carlinhos")
        ]
    )
    submit_button = ft.ElevatedButton(text="Add")
    task_list = ft.ListView(expand=True)

    def add_task():
        description = input_text.value.strip()
        assigned_to = assigned_dropdown.value
        if description:
            response = requests.post("http://localhost:8080/items/", json={"description": description, "assigned_to": assigned_to})
            if response.status_code == 200:
                input_text.value = ""
                assigned_dropdown.value = None
                update_tasks()
            else:
                page.snackbar_text = "Failed to add item"
        page.update()

    def update_tasks():
        response = requests.get("http://localhost:8080/items/")
        task_list.controls.clear()
        if response.status_code == 200:
            items = response.json()
            for index, item in enumerate(items):
                edit_button = ft.IconButton(icon=ft.icons.CREATE, on_click=lambda _, i=index: edit_task(i))
                delete_button = ft.IconButton(icon=ft.icons.DELETE, on_click=lambda _, i=index: delete_task(i))
                task_list.controls.append(ft.ListTile(
                    title=ft.Text(f"{item['description']} (Assigned to: {item['assigned_to'] if item['assigned_to'] else 'None'})"),
                    leading=edit_button,
                    trailing=delete_button
                ))
        page.update()

    def delete_task(index):
        response = requests.delete(f"http://localhost:8080/items/{index}")
        if response.status_code == 200:
            update_tasks()

    def edit_task(index):
        item = requests.get(f"http://localhost:8080/items/").json()[index]
        input_text.value = item['description']
        assigned_dropdown.value = item['assigned_to']
        submit_button.on_click = lambda _: update_task(index)

    def update_task(index):
        description = input_text.value.strip()
        assigned_to = assigned_dropdown.value
        if description:
            response = requests.put(f"http://localhost:8080/items/{index}", json={"description": description, "assigned_to": assigned_to})
            if response.status_code == 200:
                input_text.value = ""
                assigned_dropdown.value = None
                update_tasks()
                submit_button.on_click = add_task  # Reset button action to add new task
            else:
                page.snackbar_text = "Failed to update item"
        page.update()

    submit_button.on_click = lambda _: add_task()
    page.add(input_text, assigned_dropdown, submit_button, task_list)
    update_tasks()

ft.app(target=main, port=8000)