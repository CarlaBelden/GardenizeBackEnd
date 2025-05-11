from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


def get_plants() -> list[MovieResponse]:
    with SessionLocal() as db:
        db_plants = db.query(DBMovie).all()

        plants: list[MovieResponse] = []
        for db_plant in db_plants:
            plants.append(
                MovieResponse(
                    id=db_movie.id,
                    tmdb_id=db_movie.tmdb_id,
                    overview=db_movie.overview,
                    title=db_movie.title,
                    release_date=db_movie.release_date,
                    poster_path=db_movie.poster_path,
                )
            )
        return plants
