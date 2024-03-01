from fastapi import APIRouter,HTTPException,status
from pydantic import BaseModel # tipo de datos 
from app.db.database  import Session, engine
from app.models.maestro  import Pais,PaisUbigeo,ZonaUbigeo
from app.schemas.ubigeoSchema  import paisSchema,paisUbiSchema,zonaUbiSchema
from datetime import datetime
from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm import joinedload

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
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found"
        ) 
    return  jsonable_encoder(lstPais)

@paisRouter.get('/{id}')
async def get_paisById(id:int):
    try:
        datPais =session.query(Pais).filter(Pais.idpais==id).first()   
        if not datPais:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail="not found country Id"
            )       
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found"
        )       
    return jsonable_encoder(datPais)

@paisRouter.post('')
async def post_pais(pais:paisSchema):
    try:    
        idPaisCount = session.query(Pais.idpais).count()
        idPaisCount = idPaisCount+1 
        
        newPais = Pais(   
            idpais =idPaisCount,
            nombre =pais.nombre,
            isoAlfaUno =pais.isoAlfaUno,
            isoAlfaDos = pais.isoAlfaDos,
            registroactivo =pais.registroactivo,
            ucreacion =pais.umantenimiento, 
            fcreacion = datetime.now()
        )          
        session.add(newPais)
        session.commit() 
        response={
            "status":"OK",
            "Mesaje":"Register coutry"
            }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
             detail="not found "
        )   
    return jsonable_encoder(response)

@paisRouter.put('{id}')
async def update_paisById(id:int,pais:paisSchema):
    try:     
        paisById = session.query(Pais).filter(Pais.idpais ==id ).first() 
        if not paisById:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail="not found pais Id"
            )
        if paisById:
            paisById.idpais=id,          
            paisById.nombre =  pais.nombre,
            paisById.isoAlfaUno =pais.isoAlfaUno,
            paisById.isoAlfaDos = pais.isoAlfaDos,
            paisById.registroactivo =pais.registroactivo,
            paisById.umodificacion = pais.umantenimiento      
            paisById.fmodificacion = datetime.now()  
            session.commit()            
            response={
                "status":"OK",
                "Mesaje":"Update Country"
                }      
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
             detail="not found"
        )   
    return jsonable_encoder(response)


#https://community.snowflake.com/s/article/How-to-Join-2-tables-using-SQL-Alchemy
@paisUbigeoRouter.get('/{idPais}')
async def get_paisUbigeo(idPais:int):    
    try:   
        lstPaisUbigeo = session.get(PaisUbigeo, idPais).all()
        #lstPaisUbigeo = session.query(PaisUbigeo).options(joinedload(PaisUbigeo.pais)).filter(PaisUbigeo.idpais==idPais).filter(PaisUbigeo.eliminado=="N").all() 
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found"
        )         
    return  jsonable_encoder(lstPaisUbigeo)

@paisUbigeoRouter.get('/{id}')
async def get_paisUbigeoById(id:int):
    try:
        datPaisUbigeo =session.query(PaisUbigeo).filter(PaisUbigeo.idubigeo ==id).all()   
        if not datPaisUbigeo:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail="not found city Id"
            )       
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found"
        )       
    return jsonable_encoder(datPaisUbigeo)

@paisUbigeoRouter.post('')
async def post_paisUbigeo(paisUbigeo:paisUbiSchema):
    try:    
        idPaisUbiCount = session.query(PaisUbigeo.idubigeo).count()
        idPaisUbiCount = idPaisUbiCount+1 
        
        newPais = PaisUbigeo(  
            idubigeo =idPaisUbiCount,  
            idpais = paisUbigeo.idpais,  
            nombre = paisUbigeo.nombre, 
            codigoDepartamento = paisUbigeo.codigoDepartamento,
            codigoDistrito = paisUbigeo.codigoDistrito, 
            codigoProvincia = paisUbigeo.codigoProvincia,
            codigo= paisUbigeo.codigo,
            registroactivo =paisUbigeo.registroactivo,
            ucreacion =paisUbigeo.umantenimiento, 
            fcreacion = datetime.now()
        )          
        session.add(newPais)
        session.commit() 
        
        response={
            "status":"OK",
            "Mesaje":"Register city"
            }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
             detail="not found "
        )   
    return jsonable_encoder(response)

@paisUbigeoRouter.put('/{id}')
async def update_paisUbigeoById(id:int,paisUbigeo:paisUbiSchema):
    try:     
        paisUbiById = session.query(PaisUbigeo).filter(PaisUbigeo.idubigeo ==id ).first() 
        #print(jsonable_encoder(paisUbiById))        
        if not paisUbiById:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail="not found ubigeo Id"
            )
        if paisUbiById:
            paisUbiById.idubigeo =id  
            paisUbiById.idpais = paisUbigeo.idpais  
            paisUbiById.nombre = paisUbigeo.nombre 
            paisUbiById.codigoDepartamento = paisUbigeo.codigoDepartamento
            paisUbiById.codigoDistrito = paisUbigeo.codigoDistrito 
            paisUbiById.codigoProvincia = paisUbigeo.codigoProvincia            
            paisUbiById.codigo= paisUbigeo.codigo
            paisUbiById.registroactivo= paisUbigeo.registroactivo
            paisUbiById.umodificacion = paisUbigeo.umantenimiento      
            paisUbiById.fmodificacion = datetime.now()  
            session.commit()            
            response={
                "status":"OK",
                "Mesaje":"Update city"
                }  
           
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
             detail="not found"
        )   
    return jsonable_encoder(response)

##
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
  