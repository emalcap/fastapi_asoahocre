from pydantic import BaseModel
from typing import Optional

class PaisSchema(BaseModel):    
    idpais : Optional[int]  
    nombre : str
    isoAlfaUno : str
    isoAlfaDos : str    
    registroactivo :int
    usuario : int
    
class PaisUbigeoSchema(BaseModel):     
    idubigeo :Optional[int]    
    idpais : Optional[int]  
    nombre : str
    codigoDepartamento : str
    codigoDistrito : str
    codigoProvincia : str
    codigo: str
    registroactivo :int
    usuario : int
    
class zonaUbigeoSchema(BaseModel):     
    idubigeo :Optional[int]    
    idpais : Optional[int]  
    nombre : str
    codigoDepartamento : str
    codigoDistrito : str
    codigoProvincia : str
    codigo: str
    registroactivo :int
    usuario : int
# usado para rl ejemplo
class citySchema(BaseModel): 
    id :int
    name :str
    countryId : int
    countryName :str
    