from pydantic import BaseModel
from typing import Optional

#Empresa Model 
class EmpresaBE(BaseModel): #schema     
    idempresa : Optional[int]  
    ruc : Optional[str]
    razonsocial:str
    domiciliolegal:str
    registroactivo :int 