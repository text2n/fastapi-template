from sqlalchemy import Column, Integer, String

from app.core.db import Base

class Hero(Base):
    __tablename__ = "hero"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    age = Column(Integer, nullable=True)
    secret_name = Column(String(255))
