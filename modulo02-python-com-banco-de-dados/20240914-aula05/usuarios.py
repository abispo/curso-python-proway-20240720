
from config import session
from models import Usuario, Perfil


def listar_usuarios():
    return session.query(Usuario).all()


if __name__ == "__main__":
    pass