from sqlalchemy import Column, String

from models import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)
