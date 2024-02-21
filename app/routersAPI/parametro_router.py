from fastapi import APIRouter,HTTPException,status
from pydantic import BaseModel # tipo de datos 
from app.db.database  import Session, engine
from app.models.maestro  import Parametro,ParametroDet
from app.schemas.parametroSchema import ParametroSchema
from fastapi.encoders import jsonable_encoder
from sqlalchemy import text,func

parametroRouter = APIRouter(
    prefix="/api/parametro",
    tags= ["Parametro"]
)

parametroDetRouter = APIRouter(
    prefix="/api/parametroDet",
    tags= ["ParametroDet"]
)
session = Session(bind=engine)

@parametroRouter.get('/')
async def get_parametroAll():
    try:   
        lstParametro =session.query(Parametro).filter(Parametro.eliminado == "N").all()
    #print (lstEmpresas)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found"
        ) 
    return  jsonable_encoder(lstParametro)

@parametroRouter.get('/{id}')
async def get_empresaById(id:int):
    try:
        parametro=session.query(Parametro).filter(Parametro.idparametro==id,Parametro.eliminado == "N").first() 
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found"
        )       
    return jsonable_encoder(parametro)

# parametroDetalle
@parametroDetRouter.get('/{idparametro}')
async def get_parametroDetAll(idparametro:int):
    try:   
        lstParametroDet =session.query(ParametroDet).filter(ParametroDet.idparametro ==idparametro,ParametroDet.eliminado == "N").all()
    #print (lstEmpresas)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found"
        ) 
    return  jsonable_encoder(lstParametroDet)

@parametroDetRouter.get('/{id}')
async def get_empresaById(id:int):
    try:
        parametroDet =session.query(ParametroDet).filter(ParametroDet.idparametrodet==id,ParametroDet.eliminado == "N").first() 
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found"
        )       
    return jsonable_encoder(parametroDet)