#import uvicorn

from fastapi import FastAPI

from app.routersAPI.ubigeo_router import paisRouter,paisUbigeoRouter,zonaUbigeoRouter
from app.routersAPI.empresa_routers import empresaRouters
from app.routersAPI.parametro_router import parametroRouter,parametroDetRouter
from app.routersAPI.ejemplo_routers import ejemploRouter
from app.routersAPI.usuario_router import usuarioRouters
from app.routersAPI.login_router import loginRouter
from app.routersAPI.moduloMenu_router import moduloRouter
from fastapi.middleware.cors import CORSMiddleware
#jwt 
from dotenv import load_dotenv

app = FastAPI()
app.title="FastAPI sisahocre"
#jwt 
load_dotenv()
#CORS
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#CORS
app.include_router(loginRouter) 
app.include_router(usuarioRouters) 

app.include_router(moduloRouter) 
app.include_router(paisRouter) 
app.include_router(paisUbigeoRouter) 
app.include_router(zonaUbigeoRouter) 

app.include_router(parametroRouter) 
app.include_router(parametroDetRouter)
app.include_router(empresaRouters)
 

#app.include_router(ejemploRouter)
""" 
if __name__ == "__main__":
    uvicorn.run("app.api:app", host="0.0.0.0", port=8081, reload=True)
"""