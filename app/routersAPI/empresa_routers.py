from fastapi import APIRouter,HTTPException,status,Header
from app.db.database  import Session, engine
from app.models.maestro  import Empresa
from app.schemas.empresaSchema import empresaSchema,empresaSchemaLista
from fastapi.encoders import jsonable_encoder
from datetime import datetime

empresaRouters = APIRouter(
    prefix="/api/empresa",
    tags= ["Empresa"]
)
session = Session(bind=engine)

@empresaRouters.get('/')
async def get_empresaAll(): 
    lstEmpresa = []    
    try:
        connection = engine.raw_connection()
        cursor_obj = connection.cursor()
        cursor_obj.callproc("maestro.empresa_lista", [0])
        #results = list(cursor_obj.fetchall())
        results = cursor_obj.fetchall()
        for item in results:
            #print (f"Listing usaurio {item[0]}// {item[2]}")  
            datEmpresa = empresaSchemaLista(
                idempresa       = item[0],	
                ruc             = item[1],
                razonsocial     = item[2],
                idpais          = item[3],
                pais            = item[4],		
                idubigeo        = item[5],
                ubigeo          = item[6],
                codigoubigeo    = item[7],
                idzona          = item[8],
                zona            = item[9],
                domiciliolegal  = item[10],	 
                registroactivo  = item[11]
            )
            lstEmpresa.append(datEmpresa)           
        cursor_obj.close()
        connection.commit()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found company"
        )    
    finally:
        connection.close()
    return jsonable_encoder(lstEmpresa)

@empresaRouters.get('/{id}')
async def get_empresaById(id:int):
    lstEmpresa = []    
    try:
        connection = engine.raw_connection()
        cursor_obj = connection.cursor()
        cursor_obj.callproc("maestro.empresa_lista", [id])
        #results = list(cursor_obj.fetchall())
        results = cursor_obj.fetchall()
        for item in results:
            #print (f"Listing usaurio {item[0]}// {item[2]}")  
            datEmpresa = empresaSchemaLista(
                idempresa       = item[0],	
                ruc             = item[1],
                razonsocial     = item[2],
                idpais          = item[3],
                pais            = item[4],		
                idubigeo        = item[5],
                ubigeo          = item[6],
                codigoubigeo    = item[7],
                idzona          = item[8],
                zona            = item[9],
                domiciliolegal  = item[10],	 
                registroactivo  = item[11]
            )
            lstEmpresa.append(datEmpresa)           
        cursor_obj.close()
        connection.commit()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found company Id"
        )    
    finally:
        connection.close()
    return jsonable_encoder(lstEmpresa)

@empresaRouters.put('/{id}/')
async def update_empresaById(id:int,empresa:empresaSchema):
    empresaById= session.query(Empresa).filter(Empresa.idempresa==id).first()
    if not empresaById:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail="not found company id"
    )
    ruc_exist = session.query(Empresa).filter(Empresa.idempresa != empresa.idempresa ,Empresa.ruc == empresa.ruc).first() 
    if ruc_exist:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
            detail="CONFLICT: Ruc already registered"
        )
        
    try:         
        #ruc = empresaById.ruc        
        empresaById.idempresa=id,
        empresaById.idpais=empresa.idpais,
        empresaById.idubigeo=empresa.idubigeo,
        empresaById.idzona=empresa.idzona,
        empresaById.ruc=empresa.ruc,
        empresaById.razonsocial=  empresa.razonsocial,
        empresaById.domiciliolegal=empresa.domiciliolegal,
        empresaById.registroactivo=empresa.registroactivo,           
        empresaById.umodificacion= empresa.umantenimiento,
        empresaById.fmodificacion= datetime.now()        
        session.commit()
        response={
                "status":"OK",
                "Mesaje":"Update company"
        }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
             detail="company not found Id"
        )    
    return jsonable_encoder(response)


@empresaRouters.post('',status_code=status.HTTP_201_CREATED)
async def post_empresa(empresa:empresaSchema):
      
    ruc_exist  =  session.query(Empresa).filter(Empresa.ruc ==empresa.ruc).first()
    if ruc_exist:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                detail="CONFLICT: ruc  already registered"
            )
    try:   
        idEmpresaCount = session.query(Empresa.idempresa).count()
        idEmpresaCount = idEmpresaCount+1           
        newEmpresa = Empresa(
            idempresa=idEmpresaCount,
            idpais=empresa.idpais,
            idubigeo=empresa.idubigeo,
            idzona=empresa.idzona,
            ruc=empresa.ruc,
            razonsocial=  empresa.razonsocial,
            domiciliolegal=empresa.domiciliolegal,
            registroactivo=empresa.registroactivo,            
            ucreacion= empresa.umantenimiento,
            fcreacion= datetime.now()
        )
        #print(jsonable_encoder(newEmpresa))          
        session.add(newEmpresa)
        session.commit()
        response={
                "status":"OK",
                "Mesaje":"Register company"
        }
        
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
             detail="not found"
        )   
    return jsonable_encoder(response)

"""
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
""" 

# funcion postgresq Lista  
""" 
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
   
    newEmpresa ={
        "p_mantenimiento" :'I',
        "idempresa" : empresa.idempresa,
        "ruc":'12345678902',
        "razonsocial":'Empresa 02',
        "domiciliolegal":'los tres rios02',
        "registroactivo" :empresa.registroactivo  
    }      
    
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
"""


