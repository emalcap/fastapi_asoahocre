from fastapi import APIRouter,HTTPException,status
from pydantic import BaseModel # tipo de datos 
from app.db.database  import Session, engine
from app.models.maestro  import Empresa
from app.schemas.empresaSchema import EmpresaSchema
from fastapi.encoders import jsonable_encoder
from sqlalchemy import text,func

empresaRouters = APIRouter(
    prefix="/api/empresa",
    tags= ["Empresa"]
)
session = Session(bind=engine)

@empresaRouters.get('/')
async def get_empresaAll():
    try:   
        lstEmpresas =session.query(Empresa).filter(Empresa.eliminado == "N").all()
    #print (lstEmpresas)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="company not found with the given ID"
        ) 
    return  jsonable_encoder(lstEmpresas)

@empresaRouters.get('/{id}')
async def get_empresaById(id:int):
    try:
        empresa=session.query(Empresa).filter(Empresa.idempresa==id,Empresa.eliminado == "N").first() 
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found"
        )       
    return jsonable_encoder(empresa)

@empresaRouters.put('/{id}/')
async def update_empresaById(id:int,empresa:EmpresaSchema):
    
    try:
        empresaById= session.query(Empresa).filter(Empresa.idempresa==id,Empresa.eliminado == "N").first()  
        id = empresaById.idempresa
        ruc = empresaById.ruc
        
        empresaById.idempresa = id
        empresaById.ruc = ruc
        empresaById.razonsocial =empresa.razonsocial
        empresaById.domiciliolegal=empresa.domiciliolegal
        empresaById.registroactivo=empresa.registroactivo
        #print(empresaById)
        session.commit()
        response={
                "idempresa":empresaById.idempresa,
                "ruc":empresaById.ruc,
                "razonsocial":empresaById.razonsocial,
                "domiciliolegal":empresaById.domiciliolegal,
                "registroactivo":empresaById.registroactivo,
                    }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
             detail="company not found with the given ID"
        )    
    return jsonable_encoder(response)


@empresaRouters.post('/',status_code=status.HTTP_201_CREATED)
async def post_empresa(empresa:EmpresaSchema):
    newEmpresa=Empresa(
        ruc=empresa.ruc,
        idpais =empresa.idpais,
        idubigeo =empresa.idubigeoruc,
        idzona =empresa.idzona,
        razonsocial=empresa.razonsocial,
        domiciliolegal=empresa.domiciliolegal,
        registroactivo =empresa.registroactivo,
        eliminado="N",
        ucreacion =empresa.usuario        
    )   
    session.add(newEmpresa)
    session.commit()

    response={
        "ruc":newEmpresa.ruc,
        "razonsocial":newEmpresa.razonsocial,
        "domiciliolegal":newEmpresa.domiciliolegal,
        "registroactivo":newEmpresa.registroactivo
    }
    return jsonable_encoder(response)

@empresaRouters.delete('/{id}/',status_code=status.HTTP_204_NO_CONTENT)
async def delete_Empresa(id:int):  
    try:
        empresaById= session.query(Empresa).filter(Empresa.idempresa==id,Empresa.eliminado == "N").first()  
        empresaById.idempresa = id       
        empresaById.eliminado ='S'
        session.commit()    
        
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST ,                           
                            detail="company not found with the given ID"
                        )   
    return {"OK":id}


# funcion postgresq Lista  

@empresaRouters.get('/funcion/{id}')
async def get_f_empresaAll(id:int):  
    connection = engine.raw_connection()
    try:
        cursor_obj = connection.cursor()
        cursor_obj.callproc("maestro.empresalista", [id])
        results = list(cursor_obj.fetchall())
        #print(results)
        cursor_obj.close()
        connection.commit()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found"
        )    
    finally:
        connection.close()
    return  jsonable_encoder(results)

@empresaRouters.post('/mantenimiento')
async def post_empresaMantl(empresa:EmpresaSchema): 
    """
    newEmpresa ={
        "p_mantenimiento" :'I',
        "idempresa" : empresa.idempresa,
        "ruc":'12345678902',
        "razonsocial":'Empresa 02',
        "domiciliolegal":'los tres rios02',
        "registroactivo" :empresa.registroactivo  
    }      
    """ 
    domiciliolegal= 'los tres rios04',      
    connection = engine.raw_connection()
    try:
        cursor_obj = connection.cursor()
        cursor_obj.callproc("maestro.empresamat", ['U',0,'12345678904','Empresa 04',domiciliolegal,1])     
        results = list(cursor_obj.fetchall())
        print(results)
        cursor_obj.close()
        connection.commit()
    finally:
        connection.close()
    return  jsonable_encoder(results)



