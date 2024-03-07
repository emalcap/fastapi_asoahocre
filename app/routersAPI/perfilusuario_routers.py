from fastapi import APIRouter,HTTPException,status,Header
from app.db.database  import Session, engine
from app.models.seguridad  import Perfil,UsuarioPerfil
from app.schemas.perfilSchema import perfilSchema,usuPerSchema,usuPerSchemaMant
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

## usuario Perfil 
@perfilUsuarioRouter.get('/usuario/{iduser}')
async def get_perfilUsuario(iduser:int):    
    lstPerUsuario = []    
    try:
        connection = engine.raw_connection()
        cursor_obj = connection.cursor()
        cursor_obj.callproc("seguridad.perfilusuario_lista", [iduser])
        #results = list(cursor_obj.fetchall())
        results = cursor_obj.fetchall()
        for item in results:
            #print (f"Listing usaurio {item[0]}// {item[2]}")  
            datUsuPer = usuPerSchema(                
                idperfil    =item[0],
                idusaurio   =item[1],
                codigo      =item[2],
                nombre      =item[3],
                registroactivo=item[4]
            )
            lstPerUsuario.append(datUsuPer)           
        cursor_obj.close()
        connection.commit()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found Perfil user"
        )    
    finally:
        connection.close()
    return jsonable_encoder(lstPerUsuario)

@perfilUsuarioRouter.post('/usuario')
async def post_perfil(usuPer:usuPerSchemaMant):
    try:             
        newUsuPer = UsuarioPerfil(  
            idusuario = usuPer.idusuario, 
            idperfil =usuPer.idperfil,            
            registroactivo= usuPer.registroactivo,
            ucreacion = usuPer.umantenimiento,
            fcreacion = datetime.now()        
        ) 
        #print( jsonable_encoder(newUsuPer))               
        session.add(newUsuPer)
        session.commit() 
        response={
            "status":"OK",
            "Mesaje":"Register User Perfil"
            }
        
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
             detail="not found"
        )   
    return jsonable_encoder(response)


@perfilUsuarioRouter.put('Usuario/')
async def update_perfilById(usuPer: usuPerSchemaMant):
    try:     
        usuPerById = session.query(UsuarioPerfil).filter(UsuarioPerfil.idusuario == usuPer.idusuario,UsuarioPerfil.idperfil == usuPer.idperfil).first() 
        if not usuPerById:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail="not found perfil Id"
            )
        print(jsonable_encoder(usuPerById))
         
        if usuPerById:
            usuPerById.idusuario = usuPer.idusuario 
            usuPerById.idperfil= usuPer.idperfil         
            usuPerById.registroactivo= usuPer.registroactivo               
            usuPerById.umodificacion = usuPer.umantenimiento      
            usuPerById.fmodificacion = datetime.now()   
            session.commit()            
        
        response={
            "status":"OK",
            "Mesaje":"Update user Perfil"
            }    
              
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
             detail="not found"
        )   
    return jsonable_encoder(response)
