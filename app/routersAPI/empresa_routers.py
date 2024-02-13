from fastapi import APIRouter,status
from pydantic import BaseModel # tipo de datos 
from app.db.database  import Session, engine
from app.models.maestro  import Empresa
from app.schemasBE.empresa import EmpresaBE
from fastapi.encoders import jsonable_encoder
from sqlalchemy import text,func

empresaRouters = APIRouter(
    prefix="/api/empresa",
    tags= ["APIEmpresa"]
)
session = Session(bind=engine)

@empresaRouters.get('/')
async def get_empresaAll():   
    lstEmpresas =session.query(Empresa).all()
    print (lstEmpresas)
    return  jsonable_encoder(lstEmpresas)

@empresaRouters.get('/{id}')
async def get_empresaById(id:int):
    empresa=session.query(Empresa).filter(Empresa.idempresa==id).first()
    return jsonable_encoder(empresa)

@empresaRouters.put('/{id}/')
async def update_empresaById(id:int,empresa:EmpresaBE):
  empresaById=session.query(Empresa).filter(Empresa.idempresa==id).first()
  id = empresaById.idempresa
  ruc = empresaById.ruc
  
  empresaById.idempresa = id
  empresaById.ruc = ruc
  empresaById.razonsocial =empresa.razonsocial
  empresaById.domiciliolegal=empresa.domiciliolegal
  empresaById.registroactivo=empresa.registroactivo
  print(empresaById)
  session.commit()
  response={
                "idempresa":empresaById.idempresa,
                "ruc":empresaById.ruc,
                "razonsocial":empresaById.razonsocial,
                "domiciliolegal":empresaById.domiciliolegal,
                "registroactivo":empresaById.registroactivo,
            }

  return jsonable_encoder(response)


@empresaRouters.post('/',status_code=status.HTTP_201_CREATED)
async def post_empresa(empresa:EmpresaBE):
    newEmpresa=Empresa(
        ruc=empresa.ruc,
        razonsocial=empresa.razonsocial,
        domiciliolegal=empresa.domiciliolegal,
        registroactivo =1
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

# funcion postgresq Lista  
"""
@empresaRouters.get('/funcion/{id}')
async def get_f_empresaAll(id:int):  
    pct_stmt = text('SELECT * FROM maestro.empresalista(:p_idempresa)', {'p_idempresa': id})
    print(pct_stmt)
    lstEmpresas =session.execute(pct_stmt) 
   
    return  jsonable_encoder(lstEmpresas)
"""
"""
def retrieve_pct(id: int):
    pct_func = func.maestro.empresalista(id).table_valued(
        column("pid", Integer),
        column("horse_nm", String),
        column("p", Numeric(70,67)),
        column("crop", Integer),
        column("color", Enum(Colour)),
        column("sex", String))
    pct_stmt = select(pct_func)
    pct_result = db.execute(pct_stmt)
    db.commit
    return pct_result
""" 

