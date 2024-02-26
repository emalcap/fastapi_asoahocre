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
    #print (lst)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="module not found"
        ) 
    return  jsonable_encoder(lst)

@moduloRouter.get('/{id}')
async def moduloById(id:int):
    try:
        modulo =session.query(Modulo).filter(Modulo.idmodulo==id).first()        
        if modulo :
            dataModulo = moduloSchemaLista(
                idmodulo=dataModulo.idmodulo,
                codigo =dataModulo.codigo,
                nombre =dataModulo.nombre,
                registroactivo =dataModulo.registroactivo                          
            )
        else: 
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found verify module id"
            )
        
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found"
        )       
    return jsonable_encoder(modulo)

@moduloRouter.put('/{id}/')
async def update_moduloById(id:int,modulo:moduloSchema):
    try:     
        moduloById = session.query(Modulo.idmodulo).filter(Modulo.idmodulo ==id ).first() 
        if moduloById:
            moduloById.idmodulo = modulo.idmodulo       
            moduloById.codigo = modulo.codigo
            moduloById.nombre = modulo.nombre       
            moduloById.registroactivo = modulo.registroactivo          
            moduloById.umodifcacion = modulo.umantenimiento      
            moduloById.fmodicacion = datetime.now()    
                   
            session.commit()            
            response={
                "status":"OK",
                "Mesaje":"Update Module"
                }
        else:
             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
             detail="not found with the given ID"
        )    
        
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
             detail="not found with the given ID"
        )   
        
    return jsonable_encoder(response)

@moduloRouter.post('')
async def post_modulo(modulo:moduloSchema):
    try:     
        newModulo = Modulo(
            idmodulo = modulo.idmodulo,        
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
            "Mesaje":"Update Module"
            }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
             detail="not found module"
        )    
        
    return jsonable_encoder(response)