from app.db.database import Base
from sqlalchemy import Column,Integer,Boolean,Text,String,ForeignKey,DateTime,Float,Date
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.sql import func

class TipoCreditoSBS(Base):
    __tablename__ = 'tipocreditosbs'
    __table_args__ = dict(schema="producto")
    idparametro = Column(Integer, primary_key=True,autoincrement=True)   
    tipo =  Column(String(80),unique=True)
    codigo = Column(String(25),unique=True)
    nombre= Column(String(240),unique=True)    
    eliminado=Column(String(1),default="N")
    ucreacion = Column(Integer) 
    fcreacion = Column(DateTime) 
    umodificacion =Column(Integer) 
    fmodificacion =Column(DateTime) 
    
class TipoCredito(Base):
    __tablename__ = 'tipocredito'
    __table_args__ = dict(schema="producto")
    idparametro = Column(Integer, primary_key=True,autoincrement=True)   
    tipo =  Column(String(25),unique=True)
    codigo = Column(String(25),unique=True)
    nombre= Column(String(240),unique=True)    
    eliminado=Column(String(1),default="N")
    ucreacion = Column(Integer) 
    fcreacion = Column(DateTime) 
    umodificacion =Column(Integer) 
    fmodificacion =Column(DateTime) 
    
class parametroCredito(Base):
    __tablename__ = 'parametrocredito'
    __table_args__ = dict(schema="producto")
    idparametro = Column(Integer, primary_key=True,autoincrement=True)   
    tipo =  Column(String(25),unique=True)
    codigo = Column(String(25),unique=True)
    nombre= Column(String(240),unique=True)    
    eliminado=Column(String(1),default="N")
    ucreacion = Column(Integer) 
    fcreacion = Column(DateTime) 
    umodificacion =Column(Integer) 
    fmodificacion =Column(DateTime) 
    
class Credito(Base):
    __tablename__ = 'credito'
    __table_args__ = dict(schema="producto")
    idparametro = Column(Integer, primary_key=True,autoincrement=True)   
    tipo =  Column(String(25),unique=True)
    codigo = Column(String(25),unique=True)
    nombre= Column(String(240),unique=True)    
    eliminado=Column(String(1),default="N")
    ucreacion = Column(Integer) 
    fcreacion = Column(DateTime) 
    umodificacion =Column(Integer) 
    fmodificacion =Column(DateTime) 
    
class CuotasCredito(Base):
    __tablename__ = 'cuotascredito'
    __table_args__ = dict(schema="producto")
    idparametro = Column(Integer, primary_key=True,autoincrement=True)   
    tipo =  Column(String(25),unique=True)
    codigo = Column(String(25),unique=True)
    nombre= Column(String(240),unique=True)    
    eliminado=Column(String(1),default="N")
    ucreacion = Column(Integer) 
    fcreacion = Column(DateTime) 
    umodificacion =Column(Integer) 
    fmodificacion =Column(DateTime) 
