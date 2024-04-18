import flet as ft
import requests

def main(page: ft.Page):
    page.title = "Image Upload"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    def upload_files(e):
        files = page.get_file_picker_files()
        if files:
            image_data = files[0].data
            files_dict = {"file": ("image.jpg", image_data)}
            try:
                response = requests.post("http://localhost:8000/upload/", files=files_dict)
                result = response.json()
                num_objects = result["num_objects"]
                page.add(ft.Text(f"The image contains: {num_objects} objects"))
            except Exception as ex:
                page.add(ft.Text(f"Error: {ex}"))

    upload_button = ft.ElevatedButton("Upload", on_click=upload_files)

    page.add(upload_button)

if __name__ == "__main__":
    ft.app(target=main)