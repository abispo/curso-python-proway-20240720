from django.core.exceptions import ValidationError

class PreRegistroInvalido(ValidationError):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(message="Pré-registro inválido")
