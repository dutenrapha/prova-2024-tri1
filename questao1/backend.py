# Backend (FastAPI)
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Item(BaseModel):
    id: int
    description: str
    assignee: Optional[str] = None

tasks: List[Item] = []
next_id = 1

@app.post("/items/")
async def add_item(item: Item):
    global next_id
    item.id = next_id
    next_id += 1
    tasks.append(item)
    return {"message": "Item added successfully"}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    global tasks
    tasks = [item for item in tasks if item.id != item_id]
    return {"message": "Item deleted successfully"}

@app.put("/items/{item_id}")
async def edit_item(item_id: int, updated_item: Item):
    global tasks
    for item in tasks:
        if item.id == item_id:
            item.description = updated_item.description
            item.assignee = updated_item.assignee
            return {"message": "Item updated successfully"}
    raise HTTPException(status_code=404, detail="Item not found")

@app.get("/items/", response_model=List[Item])
async def get_items():
    return tasks
