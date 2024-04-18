from fastapi import FastAPI

app = FastAPI()

@app.post("/echo/")
async def echo(text: str):
    return {"echo": text}
