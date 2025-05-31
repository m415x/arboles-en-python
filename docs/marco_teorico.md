# Marco Teórico: Árboles en Python

## 1. Introducción

- Importancia de los árboles en estructuras de datos
- Aplicaciones prácticas (bases de datos, sistemas de archivos, IA)
- Objetivos del trabajo

## 2. Tipos de Árboles

- Árboles binarios
- Árboles binarios de búsqueda (BST)
- Árboles AVL (balanceados)
- Árboles B/B+ (para sistemas de almacenamiento)
- Árboles de segmentación (aplicaciones avanzadas)

## 3. Representación con Listas Anidadas

**Ventajas**:

- Conceptualmente simple
- No requiere conocimientos de POO
- Adecuado para introducción a árboles

**Limitaciones**:

- Dificultad para árboles grandes
- Operaciones de modificación complejas

## 4. Operaciones Básicas

| Función               | Complejidad | Descripción            |
| --------------------- | ----------- | ---------------------- |
| `crear_nodo()`        | O(1)        | Crea nodo hoja         |
| `insertar_izq()`      | O(1)        | Inserta hijo izquierdo |
| `recorrer_preorden()` | O(n)        | Visita todos los nodos |
