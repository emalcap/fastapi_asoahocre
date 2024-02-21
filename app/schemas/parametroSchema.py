from pydantic import BaseModel
from typing import Optional

class ParametroSchema(BaseModel):      
    idparametro : Optional[int]   
    tipo :Optional[str]
    codigo :str
    nombre: str
    registroactivo :int
    usuario : int
    
class ParametroDetSchema(BaseModel):      
    idparametrodet :Optional[int] 
    idparametro :int
    codigo :str
    valorint :str
    valor :str
    otrovalor :str
    registroactivo :int
    usuario : int