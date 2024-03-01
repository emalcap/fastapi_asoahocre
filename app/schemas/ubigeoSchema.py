from pydantic import BaseModel
from typing import Optional

class paisSchema(BaseModel):    
    idpais : Optional[int]  
    nombre : str
    isoAlfaUno : str
    isoAlfaDos : str    
    registroactivo :int
    umantenimiento : int
    #ucreacion
    #fcreacion
    #umodificacion
    #fmodificacion
    
class paisUbiSchema(BaseModel):     
    idubigeo :Optional[int]    
    idpais : Optional[int]  
    nombre : str
    codigoDepartamento : str
    codigoDistrito : str
    codigoProvincia : str
    codigo: str
    registroactivo :int
    umantenimiento : int
    
class zonaUbiSchema(BaseModel):     
    idzona : int
    idubigeo :int
    nombre :str
    registroactivo :int
    umantenimiento : int
# usado para rl ejemplo
class citySchema(BaseModel): 
    id :int
    name :str
    countryId : int
    countryName :str
    