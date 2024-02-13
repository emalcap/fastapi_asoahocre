from fastapi import FastAPI
from app.routersAPI.ejemplo_routers import ejemploRouter
from app.routersAPI.empresa_routers import empresaRouters

app = FastAPI()
app.include_router(ejemploRouter)
app.include_router(empresaRouters) 