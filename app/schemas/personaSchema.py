from pydantic import BaseModel
from typing import Optional
from datetime import date,datetime

class personaShemaMant(BaseModel):   
    idpersona :Optional[int]=None
    tipodocumento:Optional[int]=None
    nrodocumento :str
    nombre :str
    apepaterno:str
    apematerno:str
    sexo :str
    fnacimiento:date
    usumant:str
    fmant:str
    mant:Optional[str]=None