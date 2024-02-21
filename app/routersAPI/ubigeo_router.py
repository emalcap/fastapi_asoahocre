from fastapi import APIRouter,HTTPException,status
from pydantic import BaseModel # tipo de datos 
from app.db.database  import Session, engine
from app.models.maestro  import Pais,PaisUbigeo,ZonaUbigeo
from app.schemas.parametroSchema import ParametroSchema
from fastapi.encoders import jsonable_encoder
from sqlalchemy import text,func


paisRouter = APIRouter(
    prefix="/api/pais",
    tags= ["Pais"]
)

paisUbigeoRouter = APIRouter(
    prefix="/api/paisubigeo",
    tags= ["Pais Ubigeo"]
)
zonaUbigeoRouter = APIRouter(
    prefix="/api/zonaubigeo",
    tags= ["Zona Ubigeo"]
)
session = Session(bind=engine)

@paisRouter.get('/')
async def get_Pais():
    try:   
        lstPais =session.query(Pais).filter(Pais.eliminado == "N").all()
        #lstPais =session.query(Pais).all()
    #print (lstEmpresas)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found"
        ) 
    return  jsonable_encoder(lstPais)
#https://community.snowflake.com/s/article/How-to-Join-2-tables-using-SQL-Alchemy
@paisUbigeoRouter.get('/{idPais}')
async def get_paisubigeo(idPais:int):
    
    try:   
         lstPaisubigeo = session.get(PaisUbigeo, idPais)
   
        
        #lstPaisubigeo = session.query(PaisUbigeo).join(Pais, PaisUbigeo.idpais==Pais.idpais).filter(PaisUbigeo.idpais == idPais).all()
        #print("My Join Query: ",str(lstPaisubigeo))      
        #lstPaisubigeo = session.query(PaisUbigeo,Pais).join(Pais).all()        
        #for PaisUbigeoBE,PaisBE in lstPaisubigeo:
        #   print ('ok')
               
        #lstPaisubigeo = session.query(Pais, PaisUbigeo).filter(Pais.idpais==PaisUbigeo.idpais).filter(PaisUbigeo.idpais ==1).all()     
        #lstPaisubigeo = session.query(Pais).join(PaisUbigeo, Pais.idpais == PaisUbigeo.idpais).all()
        #lstPaisubigeo=session.query(PaisUbigeo).filter(PaisUbigeo.idpais==idPais, PaisUbigeo.eliminado == "N").all()
    #print (lstEmpresas)
       
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found"
        ) 
        
    return  jsonable_encoder(lstPaisubigeo)


@zonaUbigeoRouter.get('/{idubigeo}')
async def get_zonaUbigeo(idubigeo:int):
    try:   
        lstZonaUbigeo =session.query(ZonaUbigeo).filter(ZonaUbigeo.idubigeo == idubigeo).all()
    #print (lstEmpresas)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found"
        ) 
    
        
    return  jsonable_encoder(lstZonaUbigeo)
  