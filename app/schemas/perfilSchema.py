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
     
