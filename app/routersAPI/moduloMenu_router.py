from fastapi import APIRouter,HTTPException,status,Header
from app.db.database  import Session, engine
from app.models.seguridad import Modulo,ModuloMenu
from app.schemas.moduloSchema import moduloSchema,moduloSchemaLista
from fastapi.encoders import jsonable_encoder
from datetime import datetime

moduloRouter = APIRouter(
    prefix="/api/modulo",
    tags= ["Modulo Menu"]
)
session = Session(bind=engine)

@moduloRouter.get('')
async def moduloAll():
    try:   
        lst =session.query(Modulo).filter(Modulo.eliminado == "N").all()         
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="module not found"
        ) 
    return  jsonable_encoder(lst)

@moduloRouter.get('/{id}')
async def moduloById(id:int):
    try:
        datModulo =session.query(Modulo).filter(Modulo.idmodulo==id).first() 
        if not datModulo: 
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found verify module id"
        )      
              
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found"
        )       
    return jsonable_encoder(datModulo)

@moduloRouter.put('/{id}/')
async def update_moduloById(id:int,modulo:moduloSchema):
    try:     
        moduloById = session.query(Modulo).filter(Modulo.idmodulo ==id ).first() 
        if not moduloById:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail="not found module id"
            )
        if moduloById:
            moduloById.idmodulo = id      
            moduloById.codigo = modulo.codigo
            moduloById.nombre = modulo.nombre       
            moduloById.registroactivo = modulo.registroactivo          
            moduloById.umodificacion = modulo.umantenimiento      
            moduloById.fmodificacion = datetime.now()   
            session.commit()  
                   
            response={
                "status":"OK",
                "Mesaje":"Update Module"
                }      
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
             detail="not found"
        )   
    return jsonable_encoder(response)

@moduloRouter.post('')
async def post_modulo(modulo:moduloSchema):
    try:    
        idModuloCount = session.query(Modulo.idmodulo).count()
        idModuloCount = idModuloCount+1 
        
        newModulo = Modulo(
            idmodulo = idModuloCount,        
            codigo = modulo.codigo,
            nombre = modulo.nombre,        
            registroactivo = modulo.registroactivo, 
            ucreacion=  modulo.umantenimiento,      
            fcreacion  = datetime.now() 
        )     
        #print (jsonable_encoder(newModulo))           
        session.add(newModulo)
        session.commit()  
                 
        response={
            "status":"OK",
            "Mesaje":"Register Module"
            }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
             detail="not found module"
        )   
    return jsonable_encoder(response)

@moduloRouter.delete('/{id}/',status_code=status.HTTP_204_NO_CONTENT)
async def delete_module(id:int):  
    
    moduloById= session.query(Modulo).filter(Modulo.idmodulo==id,Modulo.eliminado == "N").first()  
    if not moduloById:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST ,                           
                        detail="module not found with  ID"
                    ) 
    try:  
        moduloById.idempresa = id       
        moduloById.eliminado ='S'
        session.commit()  
        
        response={
            "status":"OK",
            "Mesaje":"Delete Module"
            }  
        
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,                           
                        detail="NOT_FOUND"
                    ) 
    return response
