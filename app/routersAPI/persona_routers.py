from fastapi import APIRouter,HTTPException,status,Header
from app.db.database  import Session, engine
from app.models.maestro  import Persona
from app.schemas.personaSchema import personaShema
from datetime import datetime
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

personaRouter = APIRouter(
    prefix="/api/Persona",
    tags= ["Persona"]
)
session = Session(bind=engine)

@personaRouter.get('')
async def get_perfil():    
    try:   
        lst =session.query(Persona).filter(Persona.eliminado == "N").all()       
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found"
        ) 
    return  jsonable_encoder(lst)

@personaRouter.get('/{id}')
async def get_personaById(id:int):
    try:
        datPersona =session.query(Persona).filter(Persona.idpersona==id).first()   
        if not datPersona:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail="not found person Id"
            )       
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found"
        )       
    return jsonable_encoder(datPersona)

@personaRouter.post('')
async def post_persona(persona:personaShema):
    try:    
        idPersonaCount = session.query(Persona.idpersona).count()
        idPersonaCount = idPersonaCount+1 
        
        newPersona = Persona(   
            idpersona =idPersonaCount,
            tipodocumento=persona.tipodocumento,
            nrodocumento=persona.nrodocumento,
            nombre=persona.nombre,
            apepaterno=persona.apepaterno,
            apematerno=persona.apematerno,
            sexo=persona.sexo,
            fnacimiento=persona.fnacimiento,             
            ucreacion =persona.umantenimiento,
            fcreacion = datetime.now()
        )          
        session.add(newPersona)
        session.commit() 
        response={
            "status":"OK",
            "Mesaje":"Register Person"
            }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
             detail="not found "
        )   
    return jsonable_encoder(response)

@personaRouter.put('{id}')
async def update_PersonaById(id:int,persona:personaShema):
    try:     
        personaById = session.query(Persona).filter(Persona.idpersona ==id ).first() 
        if not personaById:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail="not found person Id"
            )
        if personaById:
            personaById.idpersona =id,
            personaById.tipodocumento=persona.tipodocumento,
            personaById.nrodocumento=persona.nrodocumento,
            personaById.nombre=persona.nombre,
            personaById.apepaterno=persona.apepaterno,
            personaById.apematerno=persona.apematerno,
            personaById.sexo=persona.sexo,
            personaById.fnacimiento=persona.fnacimiento,            
            personaById.umodificacion = persona.umantenimiento      
            personaById.fmodificacion = datetime.now()   
            session.commit()            
            response={
                "status":"OK",
                "Mesaje":"Update Person"
                }      
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
             detail="not found"
        )   
    return jsonable_encoder(response)
