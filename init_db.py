from app.db.database import engine,Base
from app.models.maestro import Empresa

Base.metadata.create_all(bind=engine)