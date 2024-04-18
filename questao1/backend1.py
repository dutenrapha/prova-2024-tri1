from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    description: str

# Lista temporária para armazenar as tarefas
tasks: List[Item] = []

@app.post("/items/")
async def add_item(item: Item):
    tasks.append(item)
    return {"message": "Item added successfully"}

@app.get("/items/", response_model=List[Item])
async def get_items():
    return tasks

#if __name__ == "__main__":
    #import uvicorn
    #uvicorn.run(app, host="0.0.0.0", port=8080)
@app.delete("/items/{item_id}/")
async def delete_item(item_id: int):
    try:
        del tasks[item_id]
        return {"message": "Item deleted successfully"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Item not found")
@app.put("/items/{item_id}/")
async def update_item(item_id: int, item: Item):
    try:
        tasks[item_id] = item
        return {"message": "Item updated successfully"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Item not found")
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
