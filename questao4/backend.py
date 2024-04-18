from fastapi import FastAPI, Request
from flet import Page, Text, Container, FloatingActionButton, icons

app = FastAPI()

counter = 0

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI!"}

@app.get("/counter")
async def get_counter():
    return {"counter": counter}

@app.post("/increment")
async def increment_counter(request: Request):
    global counter
    counter += 1
    return {"counter": counter}
