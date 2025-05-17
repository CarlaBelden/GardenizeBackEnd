from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_models import DBPlant, DBProject, DBComment, DBPlants_Project
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

DATABASE_URL = "postgresql+psycopg://postgres:postgres@localhost:5432/plant"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)


def get_plants() -> list[PlantOut]:
    with SessionLocal() as db:
        db_plants = db.query(DBPlant).all()
        plants: list[PlantOut] = []
        for db_plant in db_plants:
            plants.append(
                PlantOut(
                    plant_id=db_plant.plant_id,
                    common_name=db_plant.common_name,
                    default_image=db_plant.default_image,
                    watering=db_plant.watering,
                    sunlight=db_plant.sunlight,
                    hardiness_min=db_plant.hardiness_min,
                    hardiness_max=db_plant.hardiness_max,
                    flowers=db_plant.flowers,
                    flowering_season=db_plant.flowering_season,
                    indoor=db_plant.indoor,
                    description=db_plant.description,
                )
            )
        return plants


def get_plant(plant_id: int) -> PlantOut | None:
    session = SessionLocal()
    plant = session.query(DBPlant).filter(DBPlant.plant_id == plant_id).first()
    if plant is None:
        return None
    if plant:
        PlantOut(
            plant_id=plant.plant_id,
            common_name=plant.common_name,
            default_image=plant.default_image,
            watering=plant.watering,
            sunlight=plant.sunlight,
            hardiness_min=plant.hardiness_min,
            hardiness_max=plant.hardiness_max,
            flowers=plant.flowers,
            flowering_season=plant.flowering_season,
            indoor=plant.indoor,
            description=plant.description,
        )
    session.close()
    # convert to a dictionary and return it
    return plant


def create_new_project(project: ProjectCreateIn) -> ProjectCreateOut:
    with SessionLocal() as db:
        db_project = DBProject(**project.model_dump())
        db.add(db_project)
        db.commit()
        db.refresh(db_project)
        project = ProjectCreateOut(
            project_id=db_project.project_id,
            project_name=db_project.project_name,
            posted_date=db_project.posted_date.strftime("%m-%d-%Y"),
            summary=db_project.summary,
        )

    return project


def get_projects() -> list[ProjectCreateOut]:
    with SessionLocal() as db:
        db_projects = db.query(DBProject).all()
        projects: list[ProjectCreateOut] = []
        for db_project in db_projects:
            projects.append(
                ProjectCreateOut(
                    project_id=db_project.project_id,
                    project_name=db_project.project_name,
                    posted_date=db_project.posted_date.strftime("%m-%d-%Y"),
                    summary=db_project.summary,
                )
            )
        return projects


def get_project(project_id: int) -> ProjectPlants | None:
    with SessionLocal() as db:

        project = db.query(DBProject).filter(DBProject.project_id == project_id).first()
        if project is None:
            return None
        if project:
            project = ProjectCreateOut(
                project_id=project.project_id,
                project_name=project.project_name,
                posted_date=project.posted_date.strftime("%m-%d-%Y"),
                summary=project.summary,
            )

        db_plants_project = (
            db.query(DBPlant)
            .join(DBPlants_Project, DBPlant.plant_id == DBPlants_Project.plant_id)
            .filter(DBPlants_Project.project_id == project_id)
            .all()
        )
        plants_project: list[PlantOut] = []
        for db_plant in db_plants_project:
            plants_project.append(
                PlantOut(
                    plant_id=db_plant.plant_id,
                    common_name=db_plant.common_name,
                    default_image=db_plant.default_image,
                    watering=db_plant.watering,
                    sunlight=db_plant.sunlight,
                    hardiness_min=db_plant.hardiness_min,
                    hardiness_max=db_plant.hardiness_max,
                    flowers=db_plant.flowers,
                    flowering_season=db_plant.flowering_season,
                    indoor=db_plant.indoor,
                    description=db_plant.description,
                )
            )
        return ProjectPlants(project=project, plants=plants_project)


def create_project_plants(
    project: ProjectPlantsCreateIn,
) -> ProjectPlantsCreateOut | None:
    with SessionLocal() as db:
        # Check if the combination of project_id and plant_id already exists
        existing_entry = (
            db.query(DBPlants_Project)
            .filter(
                DBPlants_Project.project_id == project.project_id,
                DBPlants_Project.plant_id == project.plant_id,
            )
            .first()
        )
        if existing_entry:
            return None

        db_plants_project = DBPlants_Project(**project.model_dump())
        db.add(db_plants_project)
        db.commit()
        db.refresh(db_plants_project)
        plants_project = ProjectPlantsCreateOut(
            plant_project_id=db_plants_project.plant_project_id,
            project_id=db_plants_project.project_id,
            plant_id=db_plants_project.plant_id,
        )

    return plants_project


def delete_project(project_id: int) -> bool:
    with SessionLocal() as db:
        project = db.query(DBProject).filter(DBProject.project_id == project_id).first()
        if project is None:
            return False
        db.delete(project)
        db.commit()
    return True


def delete_project_plant(project_id: int, plant_id: int) -> bool:
    with SessionLocal() as db:
        plants_project = (
            db.query(DBPlants_Project)
            .filter(
                DBPlants_Project.project_id == project_id,
                DBPlants_Project.plant_id == plant_id,
            )
            .first()
        )
        if plants_project is None:
            return False
        db.delete(plants_project)
        db.commit()
    return True


def get_comments(project_id: int) -> list[CommentOut]:
    with SessionLocal() as db:
        db_comments = (
            db.query(DBComment).filter(DBComment.project_id == project_id).all()
        )
        comments: list[CommentOut] = []
        for db_comment in db_comments:
            comments.append(
                CommentOut(
                    comment_id=db_comment.comment_id,
                    project_id=db_comment.project_id,
                    posted_date=db_comment.posted_date.strftime("%m-%d-%Y"),
                    comment=db_comment.comment,
                )
            )
        return comments
