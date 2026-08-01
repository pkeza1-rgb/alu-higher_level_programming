#!/usr/bin/python3
"""Create the State model."""

from model_state import Base, State
from sqlalchemy import create_engine
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            username,
            password,
            database
        ),
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)
