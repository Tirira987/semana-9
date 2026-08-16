class Producto:
    """Clase que representa un producto del restaurante."""

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        self.codigo: str = codigo
        self.nombre: str = nombre
        self.categoria: str = categoria
        self.precio: float = precio

    def __str__(self) -> str:
        return f"[{self.codigo}] {self.nombre} | Categoría: {self.categoria} | Precio: ${self.precio:.2f}"