from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Modelo de dados para uma pergunta
class Question(BaseModel):
    text: str
    options: List[str]
    answer: int  # índice da resposta correta

# Lista de perguntas
questions = [
    Question(text="What is the capital of France?", options=["London", "Berlin", "Paris", "Rome", "Madrid"], answer=2),
    Question(text="What is 2 + 2?", options=["3", "4", "5", "6", "2"], answer=1),
    Question(text="Who wrote 'Macbeth'?", options=["Charles Dickens", "William Shakespeare", "Jane Austen", "Leo Tolstoy", "Mark Twain"], answer=1),
    Question(text="Which planet is known as the Red Planet?", options=["Earth", "Venus", "Mars", "Jupiter", "Saturn"], answer=2),
    Question(text="What is the largest ocean on Earth?", options=["Atlantic", "Indian", "Arctic", "Pacific", "Southern"], answer=3)
]

@app.get("/questions/", response_model=List[Question])
async def get_questions():
    return questions

# Modelo para as respostas do usuário
class UserAnswers(BaseModel):
    answers: List[Optional[int]]

@app.post("/submit/")
async def submit_answers(user_answers: UserAnswers):
    score = sum(1 for i, answer in enumerate(user_answers.answers) if answer == questions[i].answer)
    return {"score": score, "total": len(questions)}
