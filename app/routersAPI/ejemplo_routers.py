from fastapi import APIRouter,HTTPException,status
from fastapi.encoders import jsonable_encoder
#from pydantic import BaseModel # tipo de datos 
from app.db.database  import Session, engine
from app.models.ejemplo import City
#from sqlalchemy.orm import raiseload,lazyload,Load,joinedload
from sqlalchemy.orm import joinedload
#from sqlmodel import select
from app.schemas.ubigeoSchema import citySchema

ejemploRouter = APIRouter(
    prefix="/api/ejemplo",
    tags= ["Ejemplo"]
)

session = Session(bind=engine)

    
@ejemploRouter.get('/')
async def get_blogUSer():
    try:                          
        #results = session.query(City).options(joinedload(City.country)).all() 
        #results = session.query(Country).options(joinedload(Country.cities)).all()        
        #pais = session.query(Country).filter(Country.Code == 'PER').first()
        #ciudades = [ ciudad for ciudad in pais.cities ]
        lstDataCity = []
        results = session.query(City).options(joinedload(City.country)).all()            
        for city in results:                
            #print (f"Listing associated stocks for portfolio {city.name} // {city.country.name}")
            dataCity = citySchema(
                id =city.id,
                name =city.name,
                countryId =city.country_id,
                countryName=city.country.name                  
                )
            lstDataCity.append(dataCity)
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="NOT_FOUND"
        ) 
    return  jsonable_encoder(lstDataCity)


""" 
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
"""