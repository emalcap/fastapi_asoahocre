from pydantic import BaseModel
from typing import Optional

class parametroSchema(BaseModel):      
    idparametro : Optional[int]   
    tipo :Optional[str]
    codigo :str
    nombre: str
    registroactivo :int
    umantenimiento: Optional[int]
    
class parametroSchemaLista(BaseModel):      
    idparametro : Optional[int]   
    tipo :Optional[str]
    codigo :str
    nombre: str
    registroactivo :int
      
    
class parDetSchema(BaseModel):      
    idparametrodet :Optional[int] 
    idparametro :int    
    codigo :str
    nombre :str
    valorint :str
    valor :str
    otrovalor :str
    registroactivo :int
    umantenimiento: Optional[int]
    
class parDetSchemaLista(BaseModel):      
    idparametrodet :Optional[int] 
    idparametro :int    
    codigo :str
    nombre :str
    valorint :str
    valor :str
    otrovalor :str
    registroactivo :int
    umantenimiento: Optional[int]
    
class parDetCodSchemaLista (BaseModel): 
    idparametrodet:int 
    idparametro:int
    codigo:str
    nombre:str 
    valorint:str 
    valor:str
    otrovalor:str 					
    codigosplit:str