from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_models import DBGardener, DBPlant, DBProject, DBComment
from schemas import (
    GardenerIn,
    GardenerOut,
    PlantOut,
    ProjectCreateIn,
    ProjectCreateOut,
    CommentIn,
    CommentOut,
)

DATABASE_URL = "postgresql+psycopg://postgres:postgres@localhost:5432/plant"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


def get_plants() -> list[PlantOut]:
    with SessionLocal() as db:
        db_plants = db.query(DBPlant).all()
        print(db_plants)
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
