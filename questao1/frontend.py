import flet as ft
import requests

def main(page: ft.Page):
    page.title = "To-Do List App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    input_text = ft.TextField(hint_text="Add a new task", width=300, autofocus=True)
    submit_button = ft.ElevatedButton(text="Add", on_click=lambda _: add_task(page, input_text))
    task_list = ft.ListView(expand=True)

    assignee_options = ["John", "Alice", "Bob"]  # Opções de atribuição
    assignee_dropdown = ft.DropdownButton(options=assignee_options, value=assignee_options[0])
    
    def add_task(page, input_text):
        description = input_text.value.strip()
        assignee = assignee_dropdown.value
        if description:
            response = requests.post("http://localhost:8080/items/", json={"description": description, "assignee": assignee})
            if response.status_code == 200:
                input_text.value = ""
                update_tasks(page, task_list)
            else:
                page.snackbar_text = "Failed to add item"
        page.update()

    def delete_task(page, item_id):
        response = requests.delete(f"http://localhost:8080/items/{item_id}")
        if response.status_code == 200:
            update_tasks(page, task_list)
        else:
            page.snackbar_text = "Failed to delete item"
        page.update()

    def edit_task(page, item_id, new_description):
        response = requests.put(f"http://localhost:8080/items/{item_id}", json={"description": new_description})
        if response.status_code == 200:
            update_tasks(page, task_list)
        else:
            page.snackbar_text = "Failed to edit item"
        page.update()

    def update_tasks(page, task_list):
        response = requests.get("http://localhost:8080/items/")
        task_list.controls.clear()
        if response.status_code == 200:
            items = response.json()
            for item in items:
                edit_text = ft.TextField(value=item['description'], width=200)
                task_list.controls.append(
                    ft.Row(
                        ft.ListTile(title=edit_text),
                        ft.Button(text="Edit", on_click=lambda _, item_id=item['id'], new_description=edit_text.value: edit_task(page, item_id, new_description)),
                        ft.Button(text="Delete", on_click=lambda _, item_id=item['id']: delete_task(page, item_id)),
                        assignee_dropdown
                    )
                )
        page.update()

    page.add(input_text, submit_button, task_list)
    update_tasks(page, task_list)

ft.app(target=main, port=8000)
