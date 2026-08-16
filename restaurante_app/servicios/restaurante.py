from typing import List, Set, Optional
from modelos.producto import Producto
from modelos.usuario import Usuario

class Restaurante:
    """Servicio encargado de la lógica de negocio y administración de colecciones."""

    def __init__(self) -> None:
        # LIST: Colecciones dinámicas de objetos
        self._productos: List[Producto] = []
        self._usuarios: List[Usuario] = []

    # --- MÉTODOS PARA PRODUCTOS ---

    def registrar_producto(self, producto: Producto) -> bool:
        """Registra un producto validando que el código no esté duplicado."""
        if self.buscar_producto(producto.codigo) is not None:
            return False  # Código duplicado
        self._productos.append(producto)
        return True

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        """Busca un producto por su código."""
        for p in self._productos:
            if p.codigo.lower() == codigo.lower():
                return p
        return None

    def actualizar_producto(self, codigo: str, nuevo_nombre: str, nueva_categoria: str, nuevo_precio: float) -> bool:
        """Actualiza la información de un producto existente."""
        producto = self.buscar_producto(codigo)
        if producto:
            producto.nombre = nuevo_nombre
            producto.categoria = nueva_categoria
            producto.precio = nuevo_precio
            return True
        return False

    def eliminar_producto(self, codigo: str) -> bool:
        """Elimina un producto por su código."""
        producto = self.buscar_producto(codigo)
        if producto:
            self._productos.remove(producto)
            return True
        return False

    def listar_productos(self) -> List[Producto]:
        """Devuelve la lista completa de productos."""
        return self._productos

    # --- MÉTODOS PARA USUARIOS ---

    def registrar_usuario(self, usuario: Usuario) -> bool:
        """Registra un usuario validando que la identificación no esté duplicada."""
        if self.buscar_usuario(usuario.identificacion) is not None:
            return False  # ID duplicado
        self._usuarios.append(usuario)
        return True

    def buscar_usuario(self, identificacion: str) -> Optional[Usuario]:
        """Busca un usuario por su identificación."""
        for u in self._usuarios:
            if u.identificacion == identificacion:
                return u
        return None

    def listar_usuarios(self) -> List[Usuario]:
        """Devuelve la lista completa de usuarios."""
        return self._usuarios

    # --- USO DE CONJUNTO (SET) ---

    def obtener_categorias_unicas(self) -> Set[str]:
        """
        SET: Utiliza un conjunto para extraer y retornar las categorías 
        únicas de los productos registrados, eliminando duplicados.
        """
        return {p.categoria.title() for p in self._productos}