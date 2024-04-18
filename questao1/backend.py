#backend.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Item(BaseModel):
    description: str

class TaskAssignee(BaseModel):
    task_index: int
    assignee: str

tasks: List[Item] = []

@app.post("/items/")
async def add_item(item: Item):
    tasks.append(item)
    return {"message": "Item added successfully"}

@app.get("/items/", response_model=List[Item])
async def get_items():
    return tasks

@app.delete("/items/{item_index}")
async def delete_item(item_index: int):
    try:
        del tasks[item_index]
    except IndexError:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}

@app.put("/items/{item_index}")
async def edit_item(item_index: int, new_item: Item):
    try:
        tasks[item_index] = new_item
    except IndexError:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item edited successfully"}

@app.post("/assign/")
async def assign_task(assignee_info: TaskAssignee):
    try:
        tasks[assignee_info.task_index].assignee = assignee_info.assignee
    except IndexError:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Task assigned successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
