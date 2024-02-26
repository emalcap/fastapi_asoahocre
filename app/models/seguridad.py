from app.db.database import Base
from sqlalchemy import Column,Integer,String,ForeignKey,DateTime,Float,Date
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.sql import func
from app.models.maestro import Persona

class Usuario(Base):
    __tablename__ = 'usuario'
    __table_args__ = dict(schema="seguridad")    
    idusuario = Column(Integer, primary_key=True,autoincrement=True)  
    idpersona = Column(Integer, ForeignKey('maestro.persona.idpersona'))  
    codigo = Column(String(60),unique=True)
    clave= Column(String(30))
    fcaducidad= Column(Date)  
    email= Column(String(60))
    registroactivo = Column(Integer,default=1)
    eliminado=Column(String(1),default="N")
    ucreacion = Column(Integer) 
    fcracion = Column(DateTime) 
    umodificacion =Column(Integer) 
    fmodificacion =Column(DateTime)         
    #
    persona = relationship('Persona')
 
class Modulo(Base):
    __tablename__ = 'modulo'
    __table_args__ = dict(schema="seguridad")    
    idmodulo= Column(Integer, primary_key=True,autoincrement=True)
    codigo = Column(String(20))
    nombre = Column(String(60),unique=True)
    registroactivo = Column(Integer,default=1)
    eliminado=Column(String(1),default="N")
    ucreacion = Column(Integer) 
    fcreacion = Column(DateTime) 
    umodificacion =Column(Integer) 
    fmodificacion =Column(DateTime)   
   
class ModuloMenu(Base): 
    __tablename__ = 'modulomenu'
    __table_args__ = dict(schema="seguridad")    
    idmodulomenu = Column(Integer, primary_key=True,autoincrement=True)
    idmodulo = Column(Integer, ForeignKey('seguridad.modulo.idmodulo'))
    codigo =Column(String(20))
    nombre =Column(String(60))
    registroactivo = Column(Integer,default=1)
    eliminado=Column(String(1),default="N")
    ucreacion = Column(Integer) 
    fcreacion = Column(DateTime) 
    umodificacion =Column(Integer) 
    fmodificacion =Column(DateTime)  
    #
    modulo = relationship('Modulo')
   
class Perfil(Base):
    __tablename__ = 'perfil'
    __table_args__ = dict(schema="seguridad")    
    idperfil = Column(Integer, primary_key=True,autoincrement=True)
    codigo =Column(String(20))
    nombre =Column(String(60))
    registroactivo = Column(Integer,default=1)
    eliminado=Column(String(1),default="N")
    ucreacion = Column(Integer) 
    fcreacion = Column(DateTime) 
    umodificacion =Column(Integer) 
    fmodificacion =Column(DateTime)   
   
class UsuarioPerfil(Base):
    __tablename__ = 'usuarioperfil'
    __table_args__ = dict(schema="seguridad")        
    idusuario = Column(Integer, ForeignKey('seguridad.usuario.idusuario'),primary_key=True)
    idperfil = Column(Integer, ForeignKey('seguridad.perfil.idperfil'),primary_key=True)
    registroactivo = Column(Integer,default=1)
    ucreacion = Column(Integer) 
    fcreacion = Column(DateTime) 
    umodificacion =Column(Integer) 
    fmodificacion =Column(DateTime)  
    # 
    usuario = relationship('Usuario')
    perfil  = relationship('Perfil')
     
class PerfilMenu(Base):
    __tablename__ = 'perfilmenu'
    __table_args__ = dict(schema="seguridad")  
    idperfilmenu = Column(Integer, primary_key=True,autoincrement=True)
    idmodulo = Column(Integer, ForeignKey('seguridad.modulo.idmodulo'))  
    idmenu = Column(Integer, ForeignKey('seguridad.modulomenu.idmodulomenu'))   
    idperfil = Column(Integer, ForeignKey('seguridad.perfil.idperfil'))    
    consulta =  Column(Integer,default=1)
    crea = Column(Integer,default=1)
    modifica = Column(Integer,default=1)
    elimina = Column(Integer,default=1)
    exporta = Column(Integer,default=1)    
    registroactivo = Column(Integer,default=1)
    ucreacion = Column(Integer) 
    fcreacion = Column(DateTime) 
    umodificacion =Column(Integer) 
    fmodificacion =Column(DateTime)   
    # 
    modulo = relationship('Modulo')
    menu = relationship('ModuloMenu')
    perfil  = relationship('Perfil')

