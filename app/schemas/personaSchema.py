from pydantic import BaseModel
from typing import Optional
from datetime import date,datetime

class personaShema(BaseModel):   
    idpersona :Optional[int]=None
    tipodocumento:Optional[int]=None
    nrodocumento :str
    nombre :str
    apepaterno:str
    apematerno:str
    sexo :str
    fnacimiento:date
    umantenimiento:int
    #ucreacion
    #fcreacion
    #umantenimiento
    #fmantenimiento