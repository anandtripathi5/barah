from sqlalchemy import Column, String, Integer, Text

from extensions import Base


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), unique=True)
    description = Column(Text)
