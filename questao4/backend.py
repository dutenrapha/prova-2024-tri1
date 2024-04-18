from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Person(BaseModel):
    name: str
    age: int

@app.post("/person/")
async def create_person(person: Person):
    return {"message": f"Bem-vindo {person.name}!", "is_minor": person.age < 18}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
