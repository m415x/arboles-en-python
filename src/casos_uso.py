import sys
import codecs

from arbol_listas import crear_nodo_raiz, insertar_hijo_izquierdo, insertar_hijo_derecho
from operaciones_basicas import (
    visualizar_arbol,
    recorrer_preorden,
    recorrer_inorden,
    recorrer_postorden,
    altura_arbol,
    peso_arbol,
)

# Reconfiguración de sys.stdout (salida estándar):
# sys.stdout.detach(): Crea un flujo de bytes sin codificación a partir del buffer de salida
# codecs.getwriter("utf-8"): Crea un escritor que codifica a UTF-8
# La combinación fuerza a la salida estándar a usar UTF-8 de manera consistente
# Esto resuelve problemas de visualización con caracteres especiales (└──, ├──, │)
# en terminales/configuraciones donde UTF-8 no está habilitado por defecto
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


# Árbol de ejemplo
# fmt: off
arbol_ejemplo: list = [
    "A",
    [
        "B", 
        [
            "D", 
            ["H",[],[]], 
            ["I",[],[]]
        ], 
        ["E", [], []]
    ],
    [
        "C", 
        ["F", [], []], 
        ["G", [], []]
    ]
]
# fmt: on

# Definir un árbol vacío
arbol: list = []

# Crear un árbol binario de ejemplo
arbol = crear_nodo_raiz("A")
insertar_hijo_izquierdo(arbol, "B")
insertar_hijo_derecho(arbol, "C")
insertar_hijo_izquierdo(arbol[1], "D")
insertar_hijo_derecho(arbol[1], "E")
insertar_hijo_izquierdo(arbol[2], "F")
insertar_hijo_derecho(arbol[2], "G")
insertar_hijo_izquierdo(arbol[1][1], "H")
insertar_hijo_derecho(arbol[1][1], "I")

# Mostrar el árbol y sus recorridos
print("\n=== VISUALIZACIÓN DEL ÁRBOL ===\n")
visualizar_arbol(arbol)
print("\n=== RECORRIDOS ===")
print("\nPreorden:")
recorrer_preorden(arbol)
print("\nInorden:")
recorrer_inorden(arbol)
print("\nPostorden:")
recorrer_postorden(arbol)
print("\n\n=== PROPIEDADES ===")
print(f"\nAltura del árbol -> {altura_arbol(arbol)}")
print(f"Peso del árbol -> {peso_arbol(arbol)}")
