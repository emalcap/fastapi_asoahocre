from fastapi import APIRouter,HTTPException,status,Header
from app.db.database  import Session, engine
from app.models.seguridad  import Usuario
from fastapi.encoders import jsonable_encoder
from app.schemas.usarioSchema import usuarioSchemaLogin
from fuc_jwt.function_jwt import write_token
from fastapi.responses import JSONResponse

from fuc_jwt.function_jwt import validate_token


loginRouter = APIRouter(
    prefix="/api/Login",
    tags= ["Login"]
)
session = Session(bind=engine)

@loginRouter.post('')
async def get_login(login: usuarioSchemaLogin):      
    dataUario =session.query(Usuario).filter(Usuario.codigo == login.codigo,Usuario.clave ==login.clave).first()
    if not dataUario: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="not found user"  
        )
    if dataUario:
        if dataUario.registroactivo == 0:
            raise HTTPException(status_code=status.HTTP_423_LOCKED,
                        detail="user not active"  
            )    
    try:  
        """ 
        if dataUario.codigo == "emalcap":
            return write_token(login.dict())
        else:
            return JSONResponse(content={"message":"User not found"}, status_code=404)
        """
        dataToke = write_token(login.dict())
       #lsistaMOdulos = {codigo usuario}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="not generate token"
        ) 
    return  jsonable_encoder(dataToke)
  
@loginRouter.post('/verify/token')
async def verify_token(authorization:str = Header(None)): 
    #obtener solo el token    
    token = authorization.split(" ")[1]
    #print(authorization)
    return validate_token(token, output=True)
   

    