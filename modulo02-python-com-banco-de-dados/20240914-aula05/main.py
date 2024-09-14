
from config import Base, connection
from models import Usuario, Perfil

if __name__ == "__main__":
    Base.metadata.create_all(connection)
