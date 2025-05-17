from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pathlib import Path
from schemas import (
    PlantOut,
    ProjectCreateIn,
    ProjectCreateOut,
    ProjectPlants,
    ProjectPlantsCreateIn,
    ProjectPlantsCreateOut,
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


@app.get("/api/plants/{plant_id}")
def get_plant(plant_id: int) -> PlantOut:
    plant = db.get_plant(plant_id)
    if plant is None:
        raise HTTPException(status_code=404, detail="Entry not found")
    return plant


@app.post("/api/projects")
async def create_new_project(project: ProjectCreateIn) -> ProjectCreateOut:
    return db.create_new_project(project)


@app.get("/api/projects")
async def get_projects() -> list[ProjectCreateOut]:
    return db.get_projects()


@app.get("/api/projects/{project_id}", response_model=ProjectPlants)
async def get_project(project_id: int) -> ProjectPlants | None:
    return db.get_project(project_id)


@app.post("/api/project-plants/")
async def create_project_plants(
    project: ProjectPlantsCreateIn,
) -> ProjectPlantsCreateOut | None:
    if db.get_project(project.project_id) is None:
        raise HTTPException(status_code=404, detail="Project already exists")
    return db.create_project_plants(project)


@app.delete("/api/projects/{project_id}")
def delete_project_endpoint(project_id: int):
    if not db.delete_project(project_id):
        raise HTTPException(status_code=404, detail="Not Found")
    return {"detail": "Project deleted sucessfully"}


@app.delete("/api/projects/{project_id}/{plant_id}")
def delete_project_plant_endpoint(project_id: int, plant_id: int):
    if not db.delete_project_plant(project_id, plant_id):
        raise HTTPException(status_code=404, detail="Not Found")
    return {"detail": "Plant removed sucessfully"}


@app.get("/api/projects/{project_id}/comments/")
async def get_comments(project_id: int) -> list[CommentOut]:
    return db.get_comments(project_id)
