class Usuario:
    """Clase que representa a un usuario registrado en el sistema."""

    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        self.identificacion: str = identificacion
        self.nombre: str = nombre
        self.correo: str = correo

    def __str__(self) -> str:
        return f"ID: {self.identificacion} | Nombre: {self.nombre} | Correo: {self.correo}"