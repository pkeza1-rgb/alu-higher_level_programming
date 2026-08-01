#!/usr/bin/python3
"""Defines the State class."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class State(Base):
    """State class."""

    __tablename__ = "states"

    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        unique=True
    )

    name = Column(
        String(128),
        nullable=False
    )

    cities = relationship(
        "City",
        cascade="all, delete",
        backref="state"
    )
