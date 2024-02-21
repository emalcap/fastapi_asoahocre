from pydantic import BaseModel
from typing import Optional

#Empresa Model 
class EmpresaSchema(BaseModel): #schema     
    idempresa : Optional[int]
    idpais :int
    idubigeo :int
    idzona : int
    ruc : Optional[str]
    razonsocial:str
    domiciliolegal:str
    registroactivo :int 
    usuario : int
    

