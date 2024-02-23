from fastapi import APIRouter,HTTPException,status
from app.db.database  import Session, engine
from app.models.seguridad  import Usuario

from fastapi.encoders import jsonable_encoder

from app.schemas.usarioSchema import usuarioSchemaLogin

from fuc_jwt.function_jwt import write_token

loginRouter = APIRouter(
    prefix="/api/Login",
    tags= ["Usuario"]
)
session = Session(bind=engine)

@loginRouter.post('')
async def get_login(login: usuarioSchemaLogin):      
    dataUario =session.query(Usuario).filter(Usuario.codigo == login.codigo,Usuario.clave ==login.clave).first()
    if dataUario:
        if dataUario.registroactivo == 0:
            raise HTTPException(status_code=status.HTTP_423_LOCKED,
                        detail="user not active"  
            )
    else: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="not found user"  
        )
        
    try:   
        #dataToke = write_token(jsonable_encoder(login))
        #print(dataToke)
        modulo =session.query(Usuario).filter(Usuario.codigo == login.codigo,Usuario.clave ==login.clave).first()     
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="not found user"
        ) 
    return  jsonable_encoder(modulo)