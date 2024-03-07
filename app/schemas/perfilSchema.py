from pydantic import BaseModel
from typing import Optional

class perfilSchema(BaseModel):
    idperfil :  Optional[int]
    codigo : str
    nombre :str
    registroactivo:int 
    umantenimiento: Optional[int]
    #ucreacion 
    #fcreacion 
    #umodificacion 
    #fmodificacion

class usuPerSchema(BaseModel):
    idperfil :  int
    idusuario :  int
    codigo : str
    nombre :str
    registroactivo:int   
    
class usuPerSchemaMant(BaseModel):
    idusuario :  int
    idperfil :  int       
    registroactivo:int 
    umantenimiento: Optional[int]