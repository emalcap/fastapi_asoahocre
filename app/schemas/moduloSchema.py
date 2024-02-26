from pydantic import BaseModel
from typing import Optional

class moduloSchema(BaseModel):    
   idmodulo: Optional[int]
   codigo :str
   nombre :str
   registroactivo :int
   umantenimiento: Optional[int]
   
class moduloSchemaLista(BaseModel):    
   idmodulo: int
   codigo :str
   nombre :str
   registroactivo :str