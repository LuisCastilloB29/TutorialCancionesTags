import enum

from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship

from .declarative_base import Base


class Premios(enum.Enum):
    LATIN_GRAMI = 1
    MTV_AWARD = 2
    GRAMMY = 3
    OTHER = 4


class Premio(Base):
    __tablename__ = 'premio'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    ano = Column(Integer)
    descripcion = Column(String)
    medio = Column(Enum(Premios))
