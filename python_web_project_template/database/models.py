import typing as t

import sqlmodel as sql



class BaseModel(sql.SQLModel, table=False):
    id: t.Optional[int] = sql.Field(default=None, primary_key=True)



class User(BaseModel, table=True):
    username: str
    """The username of the user."""
    email: str
    """The email of the user."""
    password: str
    """The password of the user."""
