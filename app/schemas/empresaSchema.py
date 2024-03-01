from pydantic import BaseModel
from typing import Optional

#Empresa Model 
class EmpresaSchema(BaseModel): #schema     
    idempresa: Optional[int]
    idpais :int
    idubigeo :int 
    idzona :int
    ruc :str
    razonsocial:str
    domiciliolegal:str
    registroactivo :int   
    umantenimiento : int
    #ucreacion = Column(Integer) 
    #fcreacion = Column(DateTime) 
    #umodificacion =Column(Integer) 
    #fmodificacion =Column(DateTime) 
    
    
class EmpresaSchemaLista(BaseModel): #schema     
    idempresa : Optional[int]
    idpais :int
    pais :str
    idubigeo :int
    ubigeo:str
    idzona : int
    zona:str
    ruc : Optional[str]
    razonsocial:str
    domiciliolegal:str
    registroactivo :int 
    umantenimiento : int

