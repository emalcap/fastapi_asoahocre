from app.db.database import engine,Base
from app.models.maestro import Parametro
from app.models.maestro import ParametroDet
from app.models.maestro import Continente
from app.models.maestro import Pais
from app.models.maestro import PaisUbigeo
from app.models.maestro import ZonaUbigeo
from app.models.maestro import Empresa
from app.models.maestro import EmpresaSede
from app.models.maestro import Persona
from app.models.seguridad import Usuario
from app.models.seguridad import Modulo
from app.models.seguridad import ModuloMenu
from app.models.seguridad import Perfil
from app.models.seguridad import UsuarioPerfil
from app.models.seguridad import PerfilMenu

#from app.models.ejemplo import Blog
#from app.models.ejemplo import User
#from app.models.ejemplo import Country
#clearfrom app.models.ejemplo import City
Base.metadata.create_all(bind=engine)
