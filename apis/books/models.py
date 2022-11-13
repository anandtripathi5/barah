from extensions import Base
from sqlalchemy import Column, Integer, String, Text


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), unique=True)
    description = Column(Text)
