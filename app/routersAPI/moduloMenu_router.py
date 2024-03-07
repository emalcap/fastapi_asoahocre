from fastapi import APIRouter,HTTPException,status,Header
from app.db.database  import Session, engine
from app.models.seguridad import Modulo,ModuloMenu
from app.schemas.moduloSchema import moduloSchema,moduloSchemaLista,menuSchema
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

# modulo menu 

@moduloRouter.get('/menu/{idmodulo}')
async def menuByIdModulo(idmodulo:int):
    try:
        datMemu =session.query(ModuloMenu).filter(ModuloMenu.idmodulo==idmodulo).first() 
        if not datMemu: 
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found menu idmodulo"
        )               
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found"
        )       
    return jsonable_encoder(datMemu)

@moduloRouter.get('/menu/{idmenu}')
async def menuById(idmenu:int):
    try:
        datMemu =session.query(ModuloMenu).filter(ModuloMenu.idmodulomenu==idmenu).first() 
        if not datMemu: 
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found menu idmenu"
        )               
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found"
        )       
    return jsonable_encoder(datMemu)

@moduloRouter.put('/menu')
async def update_menuById(menu:menuSchema):
    try:     
        menuById = session.query(ModuloMenu).filter(ModuloMenu.idmodulomenu == menu.idmodulomenu).first() 
        if not moduloById:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail="not found menu id"
            )
        if moduloById:                
            moduloById.registroactivo = menuById.registroactivo          
            moduloById.umodificacion = menuById.umantenimiento      
            moduloById.fmodificacion = datetime.now()   
            session.commit()  
                   
            response={
                "status":"OK",
                "Mesaje":"Update menu"
                }      
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
             detail="not found"
        )   
    return jsonable_encoder(response)

@moduloRouter.post('/menu')
async def post_menu(menu:menuSchema):
    try:    
        idMenuCount = session.query(ModuloMenu.idmodulo).count()
        idMenuCount = idMenuCount+1 
        
        newMenu = ModuloMenu(                
            registroactivo = menu.registroactivo, 
            ucreacion=  menu.umantenimiento,      
            fcreacion  = datetime.now() 
        )     
        #print (jsonable_encoder(newMenu))           
        session.add(newMenu)
        session.commit()  
                 
        response={
            "status":"OK",
            "Mesaje":"Register menu"
            }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
             detail="not found menu"
        )   
    return jsonable_encoder(response)


