from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path
from schemas import (
    PlantOut,
    ProjectCreateIn,
    ProjectCreateOut,
    ProjectPlants,
    ProjectPlantsCreateIn,
    ProjectPlantsCreateOut,
)
import db
from fastapi.middleware.cors import CORSMiddleware

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
) -> ProjectPlantsCreateOut:
    return db.create_project_plants(project)
