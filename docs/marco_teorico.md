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

| Función                     | Complejidad | Descripción                                       |
| --------------------------- | ----------- | ------------------------------------------------- |
| `crear_nodo_raiz()`         | O(1)        | Crea nodo hoja                                    |
| `insertar_hijo_izquierdo()` | O(1)        | Inserta hijo izquierdo                            |
| `insertar_hijo_derecho()`   | O(1)        | Inserta hijo derecho                              |
| `recorrer_preorden()`       | O(n)        | Visita todos los nodos (raíz → izq → der)         |
| `recorrer_inorden()`        | O(n)        | Visita todos los nodos (izq -> raíz -> der)       |
| `recorrer_postorden()`      | O(n)        | Visita todos los nodos (izq -> der -> raíz)       |
| `visualizar_arbol()`        | O(n)        | Visualiza un árbol binario de manera estructurada |
| `peso_arbol()`              | O(n)        | Cuenta todos los nodos del árbol                  |

## 5. Complejidad Computacional

| Operación     | Complejidad | Descripción |
| ------------- | ----------- | ----------- |
| Creación      | O(1)        | Constante   |
| Inserción     | O(1)        | Constante   |
| Recorrido     | O(n)        | Lineal      |
| Búsqueda      | O(n)        | Lineal      |
| Visualización | O(n)        | Lineal      |
