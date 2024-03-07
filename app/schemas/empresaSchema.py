from pydantic import BaseModel
from typing import Optional

#Empresa Model 
class empresaSchema(BaseModel): #schema     
    idubigeo: int
    ruc: str
    razonsocial: str  
    idpais: int
    idempresa: int
    idzona: int
    domiciliolegal: str 
    registroactivo: int
    #eliminado: str
    umantenimiento:int
    #ucreacion: 
    #fcreacion: 
    #umodificacion: ,    
    #fmodificacion: 
class empresaSchemaLista(BaseModel): #schema     
    idempresa :int		
    ruc :str
    razonsocial :str
    idpais :int
    pais :	str		
    idubigeo :int
    ubigeo :str
    codigoubigeo :str
    idzona:int
    zona:str
    domiciliolegal:str		 
    registroactivo:int

