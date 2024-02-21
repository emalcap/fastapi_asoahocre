from pydantic import BaseModel
from typing import Optional
from datetime import date

class usuarioSchema(BaseModel):          
    idusuario : Optional[int]    
    idpersona : Optional[int]  
    tipodocumento :Optional[int]
    nrodocumento : str
    nombre :str
    apepaterno:str
    apematerno:str
    sexo :str
    fnacimiento:date
    #
    codigo : str
    clave: str
    fcaducidad:date   
    registroactivo :int    
