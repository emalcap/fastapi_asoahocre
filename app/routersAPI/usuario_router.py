from fastapi import APIRouter,HTTPException,status
from app.db.database  import Session, engine
from app.models.seguridad  import Usuario
from app.models.maestro  import Persona
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import joinedload
from app.schemas.usarioSchema import usuarioSchema,usuarioSchemaLista,usuarioSchemaLogin
from datetime import datetime
from fuc_jwt.function_jwt import write_token

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
        if not results:
                  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="NOT_FOUND user"
        ) 
                      
        for item in results:
            #print (f"Listing usaurio {item.codigo} // {item.persona.nrodocumento}")            
            dataUsuario = usuarioSchemaLista(
                idusuario =item.idusuario,
                idpersona =  item.idpersona,
                tipodocumento = item.persona.tipodocumento,
                nrodocumento = item.persona.nrodocumento,
                nombre = item.persona.nombre,
                apepaterno= item.persona.apepaterno,
                apematerno= item.persona.apematerno,
                sexo = item.persona.sexo,
                fnacimiento  =  item.persona.fnacimiento,                       
                codigo = item.codigo,
                clave= item.clave,   
                fcaducidad= item.fcaducidad,  
                email=item.email,          
                registroactivo = item.registroactivo                
            )
            lstDataUsuario.append(dataUsuario)                       
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="NOT_FOUND"
        ) 
    return  jsonable_encoder(lstDataUsuario)
 

@usuarioRouters.get('/{nrodocumento}')
async def get_usuarioNroDocumento(nrodocumento:str):  
    try:   
        dataUsaurio =[]
        person_exists = session.query(Persona).filter(Persona.nrodocumento==nrodocumento).first()
        #print(jsonable_encoder(person_exists))
        if person_exists:
            suario_exist = session.query(Usuario).options(joinedload(Usuario.persona)).filter(Usuario.idpersona==person_exists.idpersona).first()     
            if suario_exist:               
                usuario = usuarioSchemaLista(
                    idusuario =suario_exist.idusuario,
                    idpersona =  suario_exist.idpersona,
                    tipodocumento = suario_exist.persona.tipodocumento,
                    nrodocumento = suario_exist.persona.nrodocumento,
                    nombre = suario_exist.persona.nombre,
                    apepaterno= suario_exist.persona.apepaterno,
                    apematerno= suario_exist.persona.apematerno,
                    sexo = suario_exist.persona.sexo,
                    fnacimiento  =  suario_exist.persona.fnacimiento,                       
                    codigo = suario_exist.codigo,
                    clave= suario_exist.clave,   
                    fcaducidad= suario_exist.fcaducidad,  
                    email=suario_exist.email,          
                    registroactivo = suario_exist.registroactivo  
                )
                dataUsaurio.append(usuario)
            else:
                print(2)
                
                datUsuario = usuarioSchemaLista(
                    idusuario =0,
                    idpersona =  person_exists.idpersona,
                    tipodocumento = person_exists.tipodocumento,
                    nrodocumento = person_exists.nrodocumento,
                    nombre = person_exists.nombre,
                    apepaterno= person_exists.apepaterno,
                    apematerno= person_exists.apematerno,
                    sexo = person_exists.sexo,
                    fnacimiento  =  person_exists.fnacimiento,                       
                    codigo = None,
                    clave= None ,
                    fcaducidad= None,
                    email=None,          
                    registroactivo = None
                )
                dataUsaurio.append(datUsuario)
                #print(jsonable_encoder(dataUsaurio))
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail="not found person"
            )       
                                            
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="NOT FOUND"
        )       
    return jsonable_encoder(dataUsaurio)
           
@usuarioRouters.get('/{id}')
async def get_usuarioById(id:int):
    try:        
        usuario = session.query(Usuario).options(joinedload(Usuario.persona)).filter(Usuario.idusuario==id).first() 
        if not usuario:         
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found verify user id"
            )
            
        if usuario :
            dataUsuario = usuarioSchemaLista(
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
                email=usuario.email,          
                registroactivo = usuario.registroactivo                
            )     
                       
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="NOT FOUND"
        )       
    return jsonable_encoder(dataUsuario)

@usuarioRouters.put('/{id}/')
async def update_usuarioById(id:int,usuario:usuarioSchema):
     
    #usuario  no se debe actualizar datos de persona solo usuario     
    usuarioById = session.query(Usuario).filter(Usuario.idusuario ==id,Usuario.idpersona==usuario.idpersona ).first() 
    if usuarioById:        
        documento_exist = session.query(Persona).filter(Persona.idpersona != usuarioById.idpersona ,Persona.nrodocumento == usuario.nrodocumento).first()
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="not found verify person and user id"
        )   
        
    if documento_exist:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
            detail="CONFLICT: Document already registered"
        )
            
    codigo_existe = session.query(Usuario).filter(Usuario.idusuario !=id,Usuario.codigo ==usuario.codigo).first()
    if codigo_existe:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
        detail="CONFLICT: User code already registered"
        ) 
     
    try:   
        usuarioById.idusuario = usuario.idCountUsu,        
        usuarioById.codigo = usuario.codigo,
        usuarioById.clave= usuario.clave,
        usuarioById.fcaducidad= usuario.fcaducidad,   
        usuarioById.registroactivo = usuario.registroactivo,           
        usuarioById.umodifcacion = usuario.umantenimiento,        
        usuarioById.fmodicacion = datetime.now()            
        session.commit()
        #persona
        personaById = session.query(Persona).filter(Persona.idpersona ==usuarioById.idpersona).first()
        personaById.idpersona = usuario.idPerCount,
        #personaById.tipodocumento = usuario.tipodocumento,
        personaById.nrodocumento = usuario.nrodocumento,
        personaById.nombre = usuario.nombre,
        personaById.apepaterno= usuario.apepaterno,
        personaById.apematerno= usuario.apematerno,
        personaById.sexo = usuario.sexo,
        personaById.fnacimiento =usuario.fnacimiento,
        personaById.registroactivo = usuario.registroactivo ,  
        personaById.umodifcacion = usuario.umantenimiento,
        personaById.fmodicacion = datetime.now()            
        session.commit()
         
        response={
            "status":"OK",
            "Mesaje":"Update User"
            }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
             detail="not found with the given ID"
        )    
        
    return jsonable_encoder(response)

@usuarioRouters.post('/',status_code=status.HTTP_201_CREATED)
async def post_usuario(usuario:usuarioSchema):   
    if usuario.idpersona == 0:       
        documento_exist = session.query(Persona).filter(Persona.nrodocumento ==usuario.nrodocumento).first()
        if documento_exist:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
            detail="CONFLICT: Document already registered"
        )  
              
    codigo_exist  =  session.query(Usuario).filter(Usuario.codigo ==usuario.codigo).first()
    if codigo_exist:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
            detail="CONFLICT: User code already registered"
    )  
                   
    """ 
    email_exist  =  session.query(Usuario).filter(Usuario.codigo ==usuario.email).first()
    if email_exist:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                detail="CONFLICT: User email already registered"
            )  
    """         
    idPerCount = session.query(Persona.idpersona).count()
    idPerCount = idPerCount+1 
    #print(idPerCount)  
    
    try:
        if usuario.idpersona == 0:
            newPersona = Persona(
                    idpersona = idPerCount,
                    #tipodocumento = usuario.tipodocumento,
                    nrodocumento = usuario.nrodocumento,
                    nombre = usuario.nombre,
                    apepaterno= usuario.apepaterno,
                    apematerno= usuario.apematerno,
                    sexo = usuario.sexo,
                    fnacimiento =usuario.fnacimiento,
                    registroactivo = usuario.registroactivo ,  
                    ucreacion = usuario.umantenimiento,
                    fcreacion = datetime.now()
            )
            #print(jsonable_encoder(newPersona))
            session.add(newPersona)
            session.commit()
        
        idUsuCount = session.query(Usuario.idusuario).count()
        idUsuCount = idUsuCount+1 
        #print("USuario:",idUsuCount)   
        if usuario.idpersona > 0:
          idPerCount == usuario.idpersona
          
        newusuario = Usuario(
                idusuario = idUsuCount,
                idpersona = 1,
                codigo = usuario.codigo,
                clave= usuario.clave,
                fcaducidad= usuario.fcaducidad,
                email= usuario.email,
                registroactivo = usuario.registroactivo,
                ucreacion = usuario.umantenimiento,
                fcracion = datetime.now()
            )  
        #print(jsonable_encoder(newusuario))
        session.add(newusuario)
        session.commit()  
        
        response={
                    "status":"OK",
                    "Mesaje":"Register User"
                    }
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
             detail="NOT FOUND"
        )    
        
    return jsonable_encoder(response)


