from fastapi import FastAPI
from typing import List

app = FastAPI()

# Small data load
@app.get("/small")
def small():
    return {"message": "This is a small payload", "data": [1, 2, 3]}

# Medium data load
@app.get("/medium")
def medium():
    medium_data = [{"id": 1, "name": "John Doe"} for _ in range(100)]
    return {"message": "This is a medium payload", "data": medium_data}

# Heavy data load
@app.get("/heavy")
def heavy():
    heavy_data = [{"id": _, "name": "John Doe","username":f"john{_}"} for _ in range(100000)]
    return {"message": "This is a heavy payload", "data": heavy_data}
