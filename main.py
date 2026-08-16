from typing import Tuple, Dict, Callable
from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante

# TUPLE: Información estable del menú principal (inmutable)
OPCIONES_MENU: Tuple[str, ...] = (
    "1. Registrar producto",
    "2. Buscar producto",
    "3. Actualizar producto",
    "4. Eliminar producto",
    "5. Listar productos",
    "6. Registrar usuario",
    "7. Listar usuarios",
    "8. Mostrar categorías únicas",
    "9. Salir"
)

# Instancia global del servicio
servicio_restaurante = Restaurante()


def pedir_texto_no_vacio(mensaje: str) -> str:
    """Solicita un texto y valida que no esté vacío."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("❌ Error: El campo no puede estar vacío. Intente de nuevo.")


def pedir_float_positivo(mensaje: str) -> float:
    """Solicita un número flotante y valida que sea mayor a 0."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            print("❌ Error: El precio debe ser un número positivo mayor a 0.")
        except ValueError:
            print("❌ Error: Debe ingresar un valor numérico válido.")


# --- FUNCIONES DE CONTROL DE MENÚ ---

def opc_registrar_producto() -> None:
    print("\n--- Registrar Producto ---")
    codigo = pedir_texto_no_vacio("Código del producto: ")
    nombre = pedir_texto_no_vacio("Nombre del producto: ")
    categoria = pedir_texto_no_vacio("Categoría: ")
    precio = pedir_float_positivo("Precio ($): ")

    nuevo_prod = Producto(codigo, nombre, categoria, precio)
    if servicio_restaurante.registrar_producto(nuevo_prod):
        print("✅ Producto registrado correctamente.")
    else:
        print("❌ Error: Ya existe un producto registrado con ese código.")


def opc_buscar_producto() -> None:
    print("\n--- Buscar Producto ---")
    codigo = pedir_texto_no_vacio("Ingrese el código a buscar: ")
    prod = servicio_restaurante.buscar_producto(codigo)
    if prod:
        print(f"\n🔍 Encontrado: {prod}")
    else:
        print("❌ Producto no encontrado.")


def opc_actualizar_producto() -> None:
    print("\n--- Actualizar Producto ---")
    codigo = pedir_texto_no_vacio("Ingrese el código del producto a actualizar: ")
    prod = servicio_restaurante.buscar_producto(codigo)
    if prod:
        print(f"Producto actual: {prod}")
        nuevo_nombre = pedir_texto_no_vacio("Nuevo nombre: ")
        nueva_categoria = pedir_texto_no_vacio("Nueva categoría: ")
        nuevo_precio = pedir_float_positivo("Nuevo precio ($): ")

        servicio_restaurante.actualizar_producto(codigo, nuevo_nombre, nueva_categoria, nuevo_precio)
        print("✅ Producto actualizado con éxito.")
    else:
        print("❌ No se encontró ningún producto con ese código.")


def opc_eliminar_producto() -> None:
    print("\n--- Eliminar Producto ---")
    codigo = pedir_texto_no_vacio("Ingrese el código del producto a eliminar: ")
    if servicio_restaurante.eliminar_producto(codigo):
        print("✅ Producto eliminado exitosamente.")
    else:
        print("❌ No existe un producto con dicho código.")


def opc_listar_productos() -> None:
    print("\n--- Lista de Productos ---")
    productos = servicio_restaurante.listar_productos()
    if not productos:
        print("📭 No hay productos registrados.")
    else:
        for p in productos:
            print(f"  • {p}")


def opc_registrar_usuario() -> None:
    print("\n--- Registrar Usuario ---")
    identificacion = pedir_texto_no_vacio("Número de Identificación/Cédula: ")
    nombre = pedir_texto_no_vacio("Nombre completo: ")
    correo = pedir_texto_no_vacio("Correo electrónico: ")

    nuevo_usr = Usuario(identificacion, nombre, correo)
    if servicio_restaurante.registrar_usuario(nuevo_usr):
        print("✅ Usuario registrado con éxito.")
    else:
        print("❌ Error: Ya existe un usuario con esa identificación.")


def opc_listar_usuarios() -> None:
    print("\n--- Lista de Usuarios ---")
    usuarios = servicio_restaurante.listar_usuarios()
    if not usuarios:
        print("📭 No hay usuarios registrados.")
    else:
        for u in usuarios:
            print(f"  • {u}")


def opc_mostrar_categorias() -> None:
    print("\n--- Categorías Únicas de Productos ---")
    categorias = servicio_restaurante.obtener_categorias_unicas()
    if not categorias:
        print("📭 No hay categorías registradas aún.")
    else:
        print("Categorías disponibles:")
        for cat in sorted(categorias):
            print(f"  • {cat}")


def opc_salir() -> None:
    print("\n¡Gracias por usar Sistema Restaurante! Hasta luego.")


# DICT: Mapeo de la clave de opción con su correspondiente función ejecutante
ACCIONES_MENU: Dict[str, Callable[[], None]] = {
    "1": opc_registrar_producto,
    "2": opc_buscar_producto,
    "3": opc_actualizar_producto,
    "4": opc_eliminar_producto,
    "5": opc_listar_productos,
    "6": opc_registrar_usuario,
    "7": opc_listar_usuarios,
    "8": opc_mostrar_categorias,
    "9": opc_salir
}


def mostrar_menu() -> None:
    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE        ")
    print("========================================")
    for opcion in OPCIONES_MENU:
        print(opcion)
    print("========================================")


def main() -> None:
    opcion = ""
    while opcion != "9":
        mostrar_menu()
        opcion = input("Seleccione una opción (1-9): ").strip()
        
        # Ejecución dinámica desde el Diccionario
        accion = ACCIONES_MENU.get(opcion)
        if accion:
            accion()
        else:
            print("❌ Opción no válida. Ingrese un número entre 1 y 9.")


if __name__ == "__main__":
    main()