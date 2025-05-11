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

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    tmdb_id: Mapped[int] = mapped_column(nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)
    overview: Mapped[str] = mapped_column(nullable=False)
    release_date: Mapped[datetime] = mapped_column(nullable=False)
    poster_path: Mapped[str] = mapped_column(nullable=True)


class DBProject(Base):
    __tablename__ = "project"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    tmdb_id: Mapped[int] = mapped_column(nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)
    overview: Mapped[str] = mapped_column(nullable=False)
    release_date: Mapped[datetime] = mapped_column(nullable=False)
    poster_path: Mapped[str] = mapped_column(nullable=True)


class DBComment(Base):
    __tablename__ = "comment"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    reviewer_name: Mapped[str] = mapped_column(nullable=False)
    review_text: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[int] = mapped_column(nullable=False)
    movie_id: Mapped[int] = mapped_column(ForeignKey("movie.id"))
