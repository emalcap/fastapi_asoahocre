from pydantic import BaseModel
from typing import Optional
from datetime import date,datetime

class usuarioSchemaLogin(BaseModel):  
    codigo:str
    clave:str


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
    email:str 
    registroactivo:int
    umantenimiento: Optional[int]
# no esta todos los campo genera error   
class usuarioSchemaLista(BaseModel):          
    idusuario : int   
    idpersona : int 
    tipodocumento :Optional[int]
    nrodocumento : str
    nombre :str
    apepaterno:str
    apematerno:str
    sexo :str
    fnacimiento:date
    #
    codigo : Optional[str]
    clave: Optional[str]  
    fcaducidad:Optional[date] 
    email:Optional[str]
    registroactivo:Optional[int]
   
    
        

