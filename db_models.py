from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
)


class Base(DeclarativeBase):
    pass


class DBPlant(Base):
    __tablename__ = "plant"

    plant_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    common_name: Mapped[str] = mapped_column(nullable=False)
    default_image: Mapped[str] = mapped_column(nullable=True, default=None)
    watering: Mapped[str] = mapped_column(nullable=False)
    sunlight: Mapped[str] = mapped_column(nullable=False)
    hardiness_min: Mapped[int] = mapped_column(nullable=False)
    hardiness_max: Mapped[int] = mapped_column(nullable=False)
    flowers: Mapped[str] = mapped_column(nullable=True)
    flowering_season: Mapped[str] = mapped_column(nullable=False)
    indoor: Mapped[bool] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)


class DBProject(Base):
    __tablename__ = "project"

    project_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    project_name: Mapped[str] = mapped_column(nullable=False)
    posted_date: Mapped[datetime] = mapped_column(nullable=False)
    summary: Mapped[str] = mapped_column(nullable=False)


class DBComment(Base):
    __tablename__ = "comment"

    comment_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    project_id: Mapped[int] = mapped_column(ForeignKey("project.project_id"))
    plant_id: Mapped[int] = mapped_column(ForeignKey("plant.plant_id"))
    posted_date: Mapped[datetime] = mapped_column(nullable=False)
    comment: Mapped[str] = mapped_column(nullable=True)


class DBPlant_Project(Base):
    __tablename__ = "plant_project"

    plant_project_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    project_id: Mapped[int] = mapped_column(ForeignKey("project.project_id"))
    plant_id: Mapped[int] = mapped_column(ForeignKey("plant.plant_id"))
