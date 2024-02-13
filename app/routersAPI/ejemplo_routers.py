from fastapi import APIRouter
from pydantic import BaseModel # tipo de datos 

ejemploRouter = APIRouter(
    prefix="/api/ejemplo",
    tags= ["Ejemplo"]
)

lstEjemplos = []
# posts model
class Ejemplo(BaseModel):
    id: int
    title: str
    author: str         
    
@ejemploRouter.get('/')
def get_ejemplo():
    return lstEjemplos

@ejemploRouter.post('/')
def save_ejemplo(ejemplo:Ejemplo):    
    lstEjemplos.append(ejemplo.dict())   
    return lstEjemplos[-1] 
#ultimo registro posts[-1] 