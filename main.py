from fastapi import FastAPI
from app.routersAPI.ubigeo_router import paisRouter,paisUbigeoRouter,zonaUbigeoRouter
from app.routersAPI.empresa_routers import empresaRouters
from app.routersAPI.parametro_router import parametroRouter,parametroDetRouter
from app.routersAPI.ejemplo_routers import ejemploRouter
from app.routersAPI.usuario_router import usuarioRouters

app = FastAPI()


app.include_router(paisRouter) 
app.include_router(paisUbigeoRouter) 
app.include_router(zonaUbigeoRouter) 

app.include_router(usuarioRouters) 


app.include_router(parametroRouter) 
app.include_router(parametroDetRouter)
app.include_router(empresaRouters)

"""
app.include_router(ejemploRouter)
"""