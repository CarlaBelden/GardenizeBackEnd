from typing import Annotated
from pydantic import AfterValidator, BaseModel
from datetime import datetime


class GardenerIn(BaseModel):
    user_name: str


class GardenerOut(BaseModel):
    user_id: int
    user_name: str


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
    user_id: int
    summary: str
    plant_id: int


class ProjectCreateOut(BaseModel):
    project_id: int
    project_name: str
    user_id: int
    posted_date: datetime | None = None
    summary: str


class CommentIn(BaseModel):
    project_id: int
    plant_id: int
    user_id: int
    posted_date: datetime | None = None
    comment: str | None = None


class CommentOut(BaseModel):
    comment_id: int
    project_id: int
    plant_id: int
    user_id: int
    posted_date: datetime | None = None
    comment: str
