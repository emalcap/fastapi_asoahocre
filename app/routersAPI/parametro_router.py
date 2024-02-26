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
        lst = session.query(Parametro).filter(Parametro.eliminado == "N").all()
    #print (lstEmpresas)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found"
        ) 
    return  jsonable_encoder(lst)

@parametroRouter.get('/{id}')
async def get_empresaById(id:int):
    try:
        parametro=session.query(Parametro).filter(Parametro.idparametro==id).first()         
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found parameter Id"
        )       
    return jsonable_encoder(parametro)

    """ 
        @parametroRouter.post('')
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
        @moduloRouter.put('/{id}/')
        async def update_moduloById(id:int,modulo:moduloSchema):
            try:     
                moduloById = session.query(Modulo.idmodulo).filter(Modulo.idmodulo ==id ).first() 
                if moduloById:
                    moduloById.idmodulo = modulo.idmodulo,        
                    moduloById.codigo = modulo.codigo,
                    moduloById.nombre = modulo.nombre,        
                    moduloById.registroactivo = modulo.registroactivo,           
                    moduloById.umodifcacion = modulo.umantenimiento,        
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

        """




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