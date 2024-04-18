from flet import Page, TextInput, Button
import requests

def send_text():
    text = Page.get_element("input_text").value
    response = requests.post("http://localhost:8000/echo/", json={"text": text})
    Page.get_element("output_text").text = response.json()["echo"]

def main():
    input_text = TextInput("Enter text", id="input_text")
    submit_button = Button("Submit", onclick=send_text)
    output_text = Page("output_text")
    Page.append(input_text, submit_button, output_text)

if __name__ == "__main__":
    main()
