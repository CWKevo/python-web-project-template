import typing as t
import python_web_project_template.settings as s

from pathlib import Path
from sqlmodel import create_engine, SQLModel

# Need to move all models to the current namespace, so that SQLModel can create metadata for them.
from python_web_project_template.database.models import User


DATABASE_PATH = Path(__file__).parent / 'database.db'
DATABASE = create_engine(rf'sqlite:///{DATABASE_PATH.absolute()}', echo=s.DEBUG)


ALL_MODELS: t.List[t.Type[SQLModel]] = [
    User
]
"""A container for all database models, mainly used to supress "Unused import" warnings."""

SQLModel.metadata.create_all(DATABASE)
