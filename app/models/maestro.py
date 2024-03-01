from app.db.database import Base
from sqlalchemy import Column,Integer,Boolean,String,ForeignKey,DateTime,Float,Date
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.sql import func

class Parametro(Base):
    __tablename__ = 'parametro'
    __table_args__ = dict(schema="maestro")
    idparametro = Column(Integer, primary_key=True,autoincrement=True)   
    tipo =  Column(String(25))
    codigo = Column(String(25))
    nombre= Column(String(240))
    registroactivo = Column(Integer,default=1)   
    eliminado=Column(String(1),default="N")
    ucreacion = Column(Integer) 
    fcreacion = Column(DateTime) 
    umodificacion =Column(Integer) 
    fmodificacion =Column(DateTime)   

class ParametroDet(Base):
    __tablename__ = 'parametrodet'
    __table_args__ = dict(schema="maestro")
    idparametrodet = Column(Integer, primary_key=True,autoincrement=True)  
    idparametro = Column(Integer, ForeignKey('maestro.parametro.idparametro'))  
    codigo =Column(String(25))
    nombre =Column(String(80))
    valorint =Column(String(1))
    valor =Column(String(25))
    otrovalor =Column(String(25))
    registroactivo = Column(Integer,default=1)
    eliminado=Column(String(1),default="N")
    ucreacion = Column(Integer) 
    fcreacion = Column(DateTime) 
    umodificacion =Column(Integer) 
    fmodificacion =Column(DateTime)  
    #
    parametro = relationship('Parametro')


class Continente(Base):
    __tablename__ = 'continente'
    __table_args__ = dict(schema="maestro")
    idcontinente = Column(Integer, primary_key=True,autoincrement=True)  
    codigo =Column(String(25))
    nombre =Column(String(200))
    registroactivo = Column(Integer,default=1)
    eliminado=Column(String(1),default="N")
    ucreacion = Column(Integer) 
    fcreacion = Column(DateTime) 
    umodificacion =Column(Integer) 
    fmodificacion =Column(DateTime)  
     
class Pais(Base):
    __tablename__ = 'pais'
    __table_args__ = dict(schema="maestro")   
    idpais= Column(Integer, primary_key=True,autoincrement=True)  
    idcontinente =  Column(Integer, ForeignKey('maestro.continente.idcontinente'))  
    nombre = Column(String(200))
    isoAlfaUno = Column(String(25))
    isoAlfaDos =   Column(String(25))
    registroactivo = Column(Integer,default=1)
    eliminado=Column(String(1),default="N")
    ucreacion = Column(Integer) 
    fcreacion = Column(DateTime) 
    umodificacion =Column(Integer) 
    fmodificacion =Column(DateTime)  
    #
    continete = relationship('Continente')
  
class PaisUbigeo(Base):  
    __tablename__ = 'paisubigeo'
    __table_args__ = dict(schema="maestro")   
    idubigeo =Column(Integer, primary_key=True,autoincrement=True)  
    idpais =  Column(Integer, ForeignKey('maestro.pais.idpais'))  
    nombre = Column(String(200))	
    codigoDepartamento = Column(String(4))
    codigoDistrito = Column(String(4))
    codigoProvincia = Column(String(4))
    codigo= Column(String(12))
    registroactivo = Column(Integer,default=1)
    eliminado=Column(String(1),default="N")
    ucreacion = Column(Integer) 
    fcreacion = Column(DateTime) 
    umodificacion =Column(Integer) 
    fmodificacion =Column(DateTime)  
    #
    pais = relationship('Pais')
    #pais = relationship('Pais', backpopulates="maestro.paisubigeo")
      
class ZonaUbigeo(Base):
    __tablename__ = 'zonaubigeo'
    __table_args__ = dict(schema="maestro")   
    idzona =Column(Integer, primary_key=True,autoincrement=True)  
    idubigeo =  Column(Integer, ForeignKey('maestro.paisubigeo.idubigeo')) 
    nombre =  Column(String(80))    
    registroactivo = Column(Integer,default=1)
    eliminado=Column(String(1),default="N")
    ucreacion = Column(Integer) 
    fcreacion = Column(DateTime) 
    umodificacion =Column(Integer) 
    fmodificacion =Column(DateTime)  
    #
    paisubigeo =  relationship('PaisUbigeo')
    
class Empresa(Base):
    __tablename__ = 'empresa'
    __table_args__ = dict(schema="maestro")
    idempresa = Column(Integer, primary_key=True,autoincrement=True) 
    idpais =  Column(Integer, ForeignKey('maestro.pais.idpais'))  
    idubigeo =  Column(Integer, ForeignKey('maestro.paisubigeo.idubigeo')) 
    idzona =  Column(Integer, ForeignKey('maestro.zonaubigeo.idzona')) 
    ruc = Column(String(25),unique=True)
    razonsocial= Column(String(240),unique=True)
    domiciliolegal= Column(String(240))
    registroactivo = Column(Integer,default=1)
    eliminado=Column(String(1),default="N")
    ucreacion = Column(Integer) 
    fcreacion = Column(DateTime) 
    umodificacion =Column(Integer) 
    fmodificacion =Column(DateTime)  
    #
    pais = relationship('Pais')
    ubigeo = relationship('PaisUbigeo')
    zona = relationship('ZonaUbigeo')
    
class EmpresaSede(Base):
    __tablename__ = 'empresasede'
    __table_args__ = dict(schema="maestro")
    idempresasede = Column(Integer, primary_key=True,autoincrement=True)  
    idempresa = Column(Integer, ForeignKey('maestro.empresa.idempresa')) 
    idpais =  Column(Integer, ForeignKey('maestro.pais.idpais'))  
    idubigeo =  Column(Integer, ForeignKey('maestro.paisubigeo.idubigeo')) 
    idzona =  Column(Integer, ForeignKey('maestro.zonaubigeo.idzona')) 
    nombre =  Column(String(200))
    registroactivo = Column(Integer,default=1)
    eliminado=Column(String(1),default="N")
    ucreacion = Column(Integer) 
    fcreacion = Column(DateTime) 
    umodificacion =Column(Integer) 
    fmodificacion =Column(DateTime)   
    #
    empresa = relationship('Empresa')
    pais = relationship('Pais')
    ubigeo = relationship('PaisUbigeo')
    zona = relationship('ZonaUbigeo')
    
class Persona(Base):
    __tablename__ = 'persona'
    __table_args__ = dict(schema="maestro")
    idpersona = Column(Integer, primary_key=True,autoincrement=True) 
    tipodocumento = Column(Integer, ForeignKey('maestro.parametrodet.idparametrodet'))
    nrodocumento = Column(String(30))  
    nombre = Column(String(30))
    apepaterno= Column(String(30))
    apematerno= Column(String(30))
    sexo = Column(String(1))
    fnacimiento = Column(Date) 
    registroactivo = Column(Integer,default=1)
    eliminado=Column(String(1),default="N")
    ucreacion = Column(Integer) 
    fcreacion = Column(DateTime) 
    umodificacion =Column(Integer) 
    fmodificacion =Column(DateTime)  
    #
    parametroDet = relationship('ParametroDet')
    
        
    
"""
class Socio(Base):
    __tablename__ = 'socio'
    __table_args__ = dict(schema="maestro")
    idSocio = Column(Integer, primary_key=True,autoincrement=True) 
    idpersona =  Column(Integer, ForeignKey('maestro.persona.idparametro'))
    idpais =  Column(Integer, ForeignKey('maestro.pais.idpais'))  
    idubigeo =  Column(Integer, ForeignKey('maestro.paisubigeo.idubigeo')) 
    idzona =  Column(Integer, ForeignKey('maestro.zonaubigeo.idzona'))
    direccion  = Column(String(100))
    registroactivo = Column(Integer,default=1)
    eliminado=Column(String(1),default="N")
    ucreacion = Column(Integer) 
    fcracion = Column(DateTime) 
    umodifcacion =Column(Integer) 
    fmodicacion =Column(DateTime) 
   #
    persona = relationship('Persona')   
    pais = relationship('Pais')
    ubigeo = relationship('PaisUbigeo')
    zona = relationship('ZonaUbigeo')
"""