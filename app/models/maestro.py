from app.db.database import Base
from sqlalchemy import Column,Integer,Boolean,Text,String,ForeignKey,DateTime,Float
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.sql import func


class Empresa(Base):
    __tablename__ = 'empresa'
    __table_args__ = dict(schema="maestro")
    idempresa = Column(Integer, primary_key=True,autoincrement=True)    
    ruc = Column(String(25),unique=True)
    razonsocial= Column(String(240),unique=True)
    domiciliolegal= Column(String(240),unique=True)
    registroactivo = Column(Integer,default=1)
    
class Book(Base):
    __tablename__ = 'book'
    __table_args__ = dict(schema="maestro")
    id  = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    rating = Column(Float)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    author_id = Column(Integer, ForeignKey('maestro.author.id'))

    author = relationship('Author')


class Author(Base):
    __tablename__ = 'author'
    __table_args__ = dict(schema="maestro")
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())  
