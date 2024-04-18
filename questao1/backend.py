from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    description: str
    person: str

# Lista temporária para armazenar as tarefas
tasks: List[Item] = []

@app.post("/items/")
async def add_item(item: Item):
    tasks.append(item)
    return {"message": "Item added successfully"}

@app.get("/items/", response_model=List[Item])
async def get_items():
    return tasks

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id < 0 or item_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Item not found")
    del tasks[item_id]
    return {"message": "Item deleted successfully"}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    if item_id < 0 or item_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Item not found")
    tasks[item_id] = item
    return {"message": "Item updated successfully"}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)