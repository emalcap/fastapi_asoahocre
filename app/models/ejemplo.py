from datetime import datetime
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    is_superuser = Column(Boolean(), default=False)
    is_active = Column(Boolean(), default=True)
    
    blog = relationship("Blog",back_populates="author")
   
    
class Blog(Base):
    __tablename__ = 'blog'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    slug = Column(String, nullable=False)
    content = Column(Text, nullable=True)    
    author_id =  Column(Integer,ForeignKey("user.id"))
    author = relationship("User",back_populates="blog")

    created_at = Column(DateTime, default=datetime.now)
    is_active = Column(Boolean, default=False)
    
    

class Country(Base):
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True)
    Code = Column(String)
    name = Column(String)
    cities = relationship("City", back_populates="country")

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    country_id = Column(Integer, ForeignKey('countries.id'))
    country = relationship("Country", back_populates="cities")
    

