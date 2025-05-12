from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path
from schemas import (
    GardenerIn,
    GardenerOut,
    PlantOut,
    ProjectCreateIn,
    ProjectCreateOut,
    CommentIn,
    CommentOut,
)
import db

app = FastAPI()

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/plants")
async def get_plants() -> list[PlantOut]:
    return db.get_plants()
