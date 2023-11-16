from hashlib import sha256
from typing import Sequence, Union
from uuid import uuid1

import strawberry
from sqlalchemy import select
from strawberry_sqlalchemy_mapper import StrawberrySQLAlchemyMapper

from models import Base, Session, engine, users

Base.metadata.create_all(engine)

strawberry_sqlalchemy_mapper = StrawberrySQLAlchemyMapper()  # pyright: ignore[reportUnknownVariableType]


@strawberry_sqlalchemy_mapper.type(users.Users)  # pyright: ignore[reportUnknownMemberType]
class User:
    __exclude__ = ["password_hash"]


@strawberry.type
class Query:
    @strawberry.field
    def get_user(self, id: str) -> Union[User, None]:
        with Session() as session:
            return session.scalar(select(users.Users).filter_by(id=id))

    @strawberry.field
    def list_users(self) -> Sequence[User]:
        with Session() as session:
            return session.scalars(select(users.Users)).all()


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, name: str, password: str) -> str:
        with Session() as session:
            user = users.Users(
                id=uuid1().hex,
                name=name,
                password_hash=sha256(password.encode("utf8")).hexdigest(),
            )
            session.add(user)
            session.commit()
            return str(user.id)


strawberry_sqlalchemy_mapper.finalize()
