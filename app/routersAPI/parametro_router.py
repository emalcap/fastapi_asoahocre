from fastapi import APIRouter,HTTPException,status
from pydantic import BaseModel # tipo de datos 
from app.db.database  import Session, engine
from app.models.maestro  import Parametro,ParametroDet
from app.schemas.parametroSchema import parametroSchema,parametroSchemaLista
from app.schemas.parametroSchema import parDetSchema,parDetSchemaLista,parDetCodSchemaLista
from fastapi.encoders import jsonable_encoder
from sqlalchemy import text,func
from datetime import datetime
from sqlalchemy.orm import joinedload

parametroRouter = APIRouter(
    prefix="/api/parametro",
    tags= ["Parametro"]
)

parametroDetRouter = APIRouter(
    prefix="/api/parametroDet",
    tags= ["ParametroDet"]
)
session = Session(bind=engine)

@parametroRouter.get('')
async def get_parametroAll():
    try:   
        lst = session.query(Parametro).all()
        if not list: 
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found  parameter"
        ) 
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found"
        ) 
    return  jsonable_encoder(lst)

@parametroRouter.get('/codigo')
async def get_parametroAll(p_codigosplit:str):
    lstParDetCodigo =[]
    try:
        connection = engine.raw_connection()
        cursor_obj = connection.cursor()
        cursor_obj.callproc("maestro.parametrocodigo_lista", [p_codigosplit])        
        #results = list(cursor_obj.fetchall())
        results = cursor_obj.fetchall()
        for item in results:   
            #print (f"Listing usaurio {item[0]}// {item[2]}") 
            parDetCodigo = parDetCodSchemaLista(
                idparametrodet  = item[0],
                idparametro     = item[1],
                codigo          = item[2],
                nombre          = item[3],
                valorint        = item[4],
                valor           = item[5],
                otrovalor       = item[6],
                codigosplit     = item[7]       
            )          
            lstParDetCodigo.append(parDetCodigo) 
        cursor_obj.close()
        connection.commit()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found"
        )    
    finally:
        connection.close()
    return jsonable_encoder(lstParDetCodigo) 

@parametroRouter.get('/{id}')
async def get_empresaById(id:int):
    try:
        parametro=session.query(Parametro).filter(Parametro.idparametro==id).first()         
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found parameter Id"
        )       
    return jsonable_encoder(parametro)

@parametroRouter.post('')
async def post_Parametro(parametro:parametroSchema):
    try:    
        idParametroCount = session.query(Parametro.idparametro).count()
        idParametroCount = idParametroCount+1 
        
        newParametro = Parametro(
            idparametro=idParametroCount,
            tipo = parametro.tipo,
            codigo = parametro.codigo,
            nombre =  parametro.nombre,          
            ucreacion =parametro.umantenimiento,
            fcreacion = datetime.now()
        )     
        #print (jsonable_encoder(newModulo))           
        session.add(newParametro)
        session.commit()  
                 
        response={
            "status":"OK",
            "Mesaje":"Register Parameter"
            }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
             detail="not found Parameter"
        )   
    return jsonable_encoder(response)

@parametroRouter.put('{id}')
async def update_parameterById(id:int,parametro:parametroSchema):
    try:     
        parametroById = session.query(Parametro).filter(Parametro.idparametro ==id ).first() 
        if not parametroById:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail="not found parameter ID"
            )
        if parametroById:
            parametroById.idparametro=id,
            parametroById.tipo = parametro.tipo,
            parametroById.codigo = parametro.codigo,
            parametroById.nombre =  parametro.nombre,          
            parametroById.umodifcacion = parametro.umantenimiento      
            parametroById.fmodicacion = datetime.now()   
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


# *************************************************************************************************
# parametroDetalle
@parametroDetRouter.get('/{idparametro}')
async def get_parametroDetAll(idparametro:int):
    try:   
        lst =session.query(ParametroDet).filter(ParametroDet.idparametro ==idparametro,ParametroDet.eliminado == "N").all()
    #print (lst)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found"
        ) 
    return  jsonable_encoder(lst)

@parametroDetRouter.get('/id/{id}')
async def get_parDetById(id:int):
    try:        
        parametroDet =session.query(ParametroDet).filter(ParametroDet.idparametrodet==id,ParametroDet.eliminado == "N").first() 
        if not parametroDet:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found parameter Det"
            )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found"
        )       
    return jsonable_encoder(parametroDet)

@parametroDetRouter.post('')
async def post_ParametroDet(parDet:parDetSchema):
    try:    
        idParDetCount = session.query(ParametroDet.idparametrodet).count()
        idParDetCount = idParDetCount+1 
        
        newParDet = ParametroDet(
            idparametrodet = idParDetCount,
            idparametro =  parDet.idparametro ,
            codigo = parDet.codigo,
            nombre = parDet.nombre,
            valorint = parDet.valorint,
            valor = parDet.valor,
            otrovalor = parDet.otrovalor,
            registroactivo =parDet.registroactivo,
            eliminado = 'N',
            ucreacion = parDet.umantenimiento,
            fcreacion = datetime.now()            
        )       
         
        #print (jsonable_encoder(newParDet))           
        session.add(newParDet)
        session.commit()  
                 
        response={
            "status":"OK",
            "Mesaje":"Register Parameter Det"
            }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
             detail="not found Parameter Det"
        )   
    return jsonable_encoder(response)

@parametroDetRouter.put('/{id}/')
async def update_parDetById(id:int,parDet:parDetSchema):
    try:     
        parDetById = session.query(ParametroDet).filter(ParametroDet.idparametrodet ==id ).first() 
        if not parDetById:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail="not found parameter det Id"
            )
        if parDetById:            
            parDetById.idparametrodet = id,
            parDetById.idparametro =  parDet.idparametro ,
            parDetById.codigo = parDet.codigo,
            parDetById.nombre = parDet.nombre,
            parDetById.valorint = parDet.valorint,
            parDetById.valor = parDet.valor,
            parDetById.otrovalor = parDet.otrovalor,
            parDetById.registroactivo =parDet.registroactivo,
            parDetById.umodificacion = parDet.umantenimiento,
            parDetById.fmodificacion = datetime.now()              
            session.commit()            
            response={
                "status":"OK",
                "Mesaje":"Update Parameter Det"
                }      
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
             detail="not found"
        )   
    return jsonable_encoder(response)
