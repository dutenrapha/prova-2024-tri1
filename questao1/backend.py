from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Item(BaseModel):
    description: str
    assigned_to: Optional[str] = None  # Campo opcional para atribuir a uma pessoa

tasks: List[Item] = []

@app.post("/items/")
async def add_item(item: Item):
    tasks.append(item)
    return {"message": "Item added successfully"}

@app.get("/items/")
async def get_items():
    return tasks

@app.delete("/items/{item_index}")
async def delete_item(item_index: int):
    try:
        tasks.pop(item_index)
        return {"message": "Item deleted successfully"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_index}")
async def update_item(item_index: int, item: Item):
    try:
        tasks[item_index] = item
        return {"message": "Item updated successfully"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Item not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)