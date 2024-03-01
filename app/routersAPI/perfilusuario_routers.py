from fastapi import APIRouter,HTTPException,status,Header
from app.db.database  import Session, engine
from app.models.seguridad  import Perfil
from app.schemas.perfilSchema import perfilSchema
from datetime import datetime
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

perfilUsuarioRouter = APIRouter(
    prefix="/api/Perfil",
    tags= ["Perfil"]
)
session = Session(bind=engine)

@perfilUsuarioRouter.get('')
async def get_perfil():    
    try:   
        lst =session.query(Perfil).filter(Perfil.eliminado == "N").all()       
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found"
        ) 
    return  jsonable_encoder(lst)

@perfilUsuarioRouter.get('/{id}')
async def get_perfilById(id:int):
    try:
        datPerfil =session.query(Perfil).filter(Perfil.idperfil==id).first()   
        if not datPerfil:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail="not found perfil Id"
            )       
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found"
        )       
    return jsonable_encoder(datPerfil)

@perfilUsuarioRouter.post('')
async def post_perfil(perfil:perfilSchema):
    try:    
        idPerfilCount = session.query(Perfil.idperfil).count()
        idPerfilCount = idPerfilCount+1 
        
        newPerfil = Perfil(   
            idperfil= idPerfilCount,     
            codigo= perfil.codigo,
            nombre= perfil.nombre,
            registroactivo= perfil.registroactivo,    
            ucreacion =perfil.umantenimiento,
            fcreacion = datetime.now()
        )          
        session.add(newPerfil)
        session.commit() 
        response={
            "status":"OK",
            "Mesaje":"Register Perfil"
            }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
             detail="not found"
        )   
    return jsonable_encoder(response)

@perfilUsuarioRouter.put('{id}')
async def update_perfilById(id:int,perfil:perfilSchema):
    try:     
        perfilById = session.query(Perfil).filter(Perfil.idperfil ==id ).first() 
        if not perfilById:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail="not found perfil Id"
            )
        if perfilById:
            perfilById.idperfil=id           
            perfilById.codigo = perfil.codigo
            perfilById.nombre =  perfil.nombre          
            perfilById.umodificacion = perfil.umantenimiento      
            perfilById.fmodificacion = datetime.now()   
            session.commit()            
            response={
                "status":"OK",
                "Mesaje":"Update Perfil"
                }      
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
             detail="not found"
        )   
    return jsonable_encoder(response)

@perfilUsuarioRouter.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_perfil(id:int):  
    try:
        perfilById= session.query(Perfil).filter(Perfil.idperfil==id,Perfil.eliminado == "N").first() 
        if not perfilById:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail="not found perfil Id"
            ) 
        perfilById.idempresa = id       
        perfilById.eliminado ='S'
        session.commit()    
        response={
                "status":"OK",
                "Mesaje":"Delete Perfil"
                }     
    except Exception as e:
        raise HTTPException(status_code=status.status.HTTP_404_NOT_FOUND ,                           
                            detail="not found"
                        )   
    return jsonable_encoder(response)
