from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
)


class Base(DeclarativeBase):
    pass


class DBGardener(Base):
    __tablename__ = "gardener"

    user_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_name: Mapped[str] = mapped_column(nullable=False)


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
    user_id: Mapped[int] = mapped_column(ForeignKey("gardener.user_id"))
    posted_date: Mapped[datetime] = mapped_column(nullable=False)
    summary: Mapped[str] = mapped_column(nullable=False)
    plant_id: Mapped[int] = mapped_column(ForeignKey("plant.plant_id"))


class DBComment(Base):
    __tablename__ = "comment"

    comment_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    project_id: Mapped[int] = mapped_column(ForeignKey("project.project_id"))
    plant_id: Mapped[int] = mapped_column(ForeignKey("plant.plant_id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("gardener.user_id"))
    posted_date: Mapped[datetime] = mapped_column(nullable=False)
    comment: Mapped[str] = mapped_column(nullable=True)


# from datetime import datetime
# from sqlalchemy import ForeignKey
# from sqlalchemy.orm import (
#     DeclarativeBase,
#     Mapped,
#     mapped_column,
#     relationship,
# )


# class Base(DeclarativeBase):
#     pass


# class DBGardener(Base):
#     __tablename__ = "gardener"

#     user_id: Mapped[int] = mapped_column(primary_key=True, index=True)
#     user_name: Mapped[str] = mapped_column(nullable=False)

#     projects: Mapped[list["DBProject"]] = relationship(back_populates="gardener", cascade="all, delete")
#     comments: Mapped[list["DBComment"]] = relationship(back_populates="gardener", cascade="all, delete")


# class DBPlant(Base):
#     __tablename__ = "plant"

#     plant_id: Mapped[int] = mapped_column(primary_key=True, index=True)
#     common_name: Mapped[str] = mapped_column(nullable=False)
#     default_image: Mapped[str] = mapped_column(nullable=True, default=None)
#     watering: Mapped[str] = mapped_column(nullable=False)
#     sunlight: Mapped[str] = mapped_column(nullable=False)
#     hardiness_min: Mapped[str] = mapped_column(nullable=False)
#     hardiness_max: Mapped[str] = mapped_column(nullable=False)
#     flowers: Mapped[str] = mapped_column(nullable=True)
#     flowering_season: Mapped[str] = mapped_column(nullable=False)
#     indoor: Mapped[bool] = mapped_column(nullable=False)
#     description: Mapped[str] = mapped_column(nullable=False)

#     projects: Mapped[list["DBProject"]] = relationship(back_populates="plant", cascade="all, delete")
#     comments: Mapped[list["DBComment"]] = relationship(back_populates="plant", cascade="all, delete")


# class DBProject(Base):
#     __tablename__ = "project"

#     project_id: Mapped[int] = mapped_column(primary_key=True, index=True)
#     project_name: Mapped[str] = mapped_column(nullable=False)
#     user_id: Mapped[int] = mapped_column(ForeignKey("gardener.user_id"))
#     posted_date: Mapped[datetime] = mapped_column(nullable=False)
#     summary: Mapped[str] = mapped_column(nullable=False)
#     plant_id: Mapped[int] = mapped_column(ForeignKey("plant.plant_id"))

#     gardener: Mapped["DBGardener"] = relationship(back_populates="projects")
#     plant: Mapped["DBPlant"] = relationship(back_populates="projects")
#     comments: Mapped[list["DBComment"]] = relationship(back_populates="project", cascade="all, delete")


# class DBComment(Base):
#     __tablename__ = "comment"

#     comment_id: Mapped[int] = mapped_column(primary_key=True, index=True)
#     project_id: Mapped[int] = mapped_column(ForeignKey("project.project_id"))
#     plant_id: Mapped[int] = mapped_column(ForeignKey("plant.plant_id"))
#     user_id: Mapped[int] = mapped_column(ForeignKey("gardener.user_id"))
#     posted_date: Mapped[datetime] = mapped_column(nullable=False)
#     comment: Mapped[str] = mapped_column(nullable=False)

#     project: Mapped["DBProject"] = relationship(back_populates="comments")
#     plant: Mapped["DBPlant"] = relationship(back_populates="comments")
#     gardener: Mapped["DBGardener"] = relationship(back_populates="comments")
