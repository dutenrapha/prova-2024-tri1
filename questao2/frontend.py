import flet as ft

def main(page: ft.Page):
  questions = []
  scores = {"correct": 0, "total": 0}

  def fetch_questions():
    global questions
    response = ft.fetch(url="http://localhost:8080/questions/")
    questions = response.json()
    display_questions(questions)

  def display_questions(data):
    page.clean()
    for question in data:
      text = ft.Text(value=question["text"], size=20)
      options = []
      for i, option in enumerate(question["options"]):
        radio = ft.RadioButton(value=i, label=option)
        radio.on_change = lambda e: handle_radio_change(e, question["answer"])
        options.append(radio)
      page.add(text, ft.Row(*options))
    page.add(ft.ElevatedButton("Submit Answers", on_click=submit_answers))
    page.update()

  def handle_radio_change(e, correct_answer):
    user_answer = e.control.value
    if user_answer == correct_answer:
      scores["correct"] += 1
    scores["total"] += 1

  def submit_answers():
    user_answers = [q.value for q in page.controls if isinstance(q, ft.RadioButton) and q.selected]
    data = ft.UserAnswers(answers=user_answers)
    response = ft.fetch(url="http://localhost:8080/submit/", method="POST", json=data.json())
    result = response.json()
    show_result(result)

  def show_result(data):
    page.clean()
    text = ft.Text(value=f"You got {data['score']} out of {data['total']} questions correct!", size=24)
    page.add(text)
    page.update()

  fetch_questions()

  page.title = "Quiz App"
  page.update()

ft.app(target=main)
