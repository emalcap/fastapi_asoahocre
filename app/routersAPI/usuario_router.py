from fastapi import APIRouter,HTTPException,status
from app.db.database  import Session, engine
from app.models.seguridad  import Usuario
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import joinedload
from app.schemas.usarioSchema import usuarioSchema

usuarioRouters = APIRouter(
    prefix="/api/usuario",
    tags= ["Usuario"]
)
session = Session(bind=engine)

@usuarioRouters.get('/')
async def get_usuarioAll():
   
    try:  
        lstDataUsuario = []       
        results = session.query(Usuario).options(joinedload(Usuario.persona)).filter(Usuario.eliminado=="N").all()            
        for usuario in results:
            #print (f"Listing usaurio {usuario.codigo} // {usuario.persona.nrodocumento}")
            dataUsuario = usuarioSchema(
                idusuario =usuario.idusuario,
                idpersona =  usuario.idpersona,
                tipodocumento = usuario.persona.tipodocumento,
                nrodocumento = usuario.persona.nrodocumento,
                nombre = usuario.persona.nombre,
                apepaterno= usuario.persona.apepaterno,
                apematerno= usuario.persona.apematerno,
                sexo = usuario.persona.sexo,
                fnacimiento  =  usuario.persona.fnacimiento,         
                codigo = usuario.codigo,
                clave= usuario.clave,   
                fcaducidad= usuario.fcaducidad,            
                registroactivo = usuario.registroactivo
            )
            lstDataUsuario.append(dataUsuario)
           
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="NOT_FOUND"
        ) 
    return  jsonable_encoder(lstDataUsuario)

 
@usuarioRouters.get('/login')
async def get_login(codigo:str,pasword:str):
    try:   
        dataUario =session.query(Usuario).filter(Usuario.codigo == codigo,Usuario.clave ==pasword,Usuario.registroactivo==1 ).first()
        print(dataUario.idusuario)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="not found user"
        ) 
    return  jsonable_encoder(dataUario)

@usuarioRouters.get('/{id}')
async def get_usuarioById(id:int):
    try:
        #usuario=session.query(Usuario).filter(Usuario.idusuario==id,Usuario.eliminado == "N").first()
        usuario = session.query(Usuario).options(joinedload(Usuario.persona)).filter(Usuario.idusuario==id).first() 
        if usuario :
            dataUsuario = usuarioSchema(
                    idusuario =usuario.idusuario,
                    idpersona =  usuario.idpersona,
                    tipodocumento = usuario.persona.tipodocumento,
                    nrodocumento = usuario.persona.nrodocumento,
                    nombre = usuario.persona.nombre,
                    apepaterno= usuario.persona.apepaterno,
                    apematerno= usuario.persona.apematerno,
                    sexo = usuario.persona.sexo,
                    fnacimiento  =  usuario.persona.fnacimiento,         
                    codigo = usuario.codigo,
                    clave= usuario.clave,   
                    fcaducidad= usuario.fcaducidad,            
                    registroactivo = usuario.registroactivo
                )           
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="NOT_FOUND"
        )       
    return jsonable_encoder(dataUsuario)

""" 
@usuarioRouters.put('/{id}/')
async def update_usuarioById(id:int,usario:usuarioSchema):
    
    try:
        usuarioById= session.query(Usuario).filter(Usuario.idusuario==id,Usuario.eliminado == "N").first()  
        id = usuarioById.idempresa
        ruc = usuarioById.ruc
        
        usuarioById.idempresa = id
        usuarioById.ruc = ruc
        usuarioById.razonsocial =usario.razonsocial
        usuarioById.domiciliolegal=usario.domiciliolegal
        usuarioById.registroactivo=usario.registroactivo
        #print(empresaById)
        session.commit()
        response={
                "idempresa":usuarioById.idempresa,
                "ruc":usuarioById.ruc,
                "razonsocial":usuarioById.razonsocial,
                "domiciliolegal":usuarioById.domiciliolegal,
                "registroactivo":usuarioById.registroactivo,
                    }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
             detail="company not found with the given ID"
        )    
    return jsonable_encoder(response)

@usuarioRouters.post('/',status_code=status.HTTP_201_CREATED)
async def post_empresa(usuario:usuarioSchema):
        dataUsuario = usuarioSchema(
                idusuario =usuario.idusuario,
                idpersona =  usuario.idpersona,
                tipodocumento = usuario.persona.tipodocumento,
                nrodocumento = usuario.persona.nrodocumento,
                nombre = usuario.persona.nombre,
                apepaterno= usuario.persona.apepaterno,
                apematerno= usuario.persona.apematerno,
                sexo = usuario.persona.sexo,
                fnacimiento  =  usuario.persona.fnacimiento,         
                codigo = usuario.codigo,
                clave= usuario.clave,   
                fcaducidad= usuario.fcaducidad,            
                registroactivo = usuario.registroactivo
            )   
        session.add(dataUsuario)
        session.commit()

        response={
            "ruc":dataUsuario.ruc,
            "razonsocial":dataUsuario.razonsocial,
            "domiciliolegal":dataUsuario.domiciliolegal,
            "registroactivo":dataUsuario.registroactivo
        }
        return jsonable_encoder(response)
"""