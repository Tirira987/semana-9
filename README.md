# Restaurante App - Semana 9

**Estudiante:** Richard Arturo Tirira Díaz  
**Asignatura:** Programación Orientada a Objetos  
**Tema:** Estructuras de Datos Aplicadas en Python  

---

## 📌 Descripción del Sistema

`restaurante_app` es una aplicación modular en Python diseñada bajo el paradigma de Programación Orientada a Objetos (POO). El sistema permite la administración básica de los objetos `Producto` y `Usuario` de un restaurante, aplicando control de duplicados, validaciones de entrada de datos y una clara separación de responsabilidades entre los modelos, la capa de servicio y la interfaz de consola.

---

## 📁 Estructura del Proyecto

```text
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
├── main.py
└── README.md
