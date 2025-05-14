from typing import List
from pydantic import BaseModel
from datetime import datetime


class PlantOut(BaseModel):
    plant_id: int
    common_name: str
    default_image: str | None = None
    watering: str
    sunlight: str
    hardiness_min: int
    hardiness_max: int
    flowers: str | None = None
    flowering_season: str | None = None
    indoor: bool
    description: str


class ProjectCreateIn(BaseModel):
    project_name: str
    summary: str


class ProjectPlantsCreateIn(BaseModel):
    project_id: int
    plant_id: int


class ProjectPlantsCreateOut(BaseModel):
    plant_project_id: int
    project_id: int
    plant_id: int


class ProjectCreateOut(BaseModel):
    project_id: int
    project_name: str
    posted_date: str
    summary: str


class ProjectPlants(BaseModel):
    project: ProjectCreateOut
    plants: List[PlantOut]


class CommentIn(BaseModel):
    project_id: int
    plant_id: int
    posted_date: datetime | None = None
    comment: str | None = None


class CommentOut(BaseModel):
    comment_id: int
    project_id: int
    plant_id: int
    posted_date: datetime | None = None
    comment: str
