from operaciones_basicas import visualizar_arbol
from arbol_listas import crear_nodo_raiz, insertar_hijo_izquierdo, insertar_hijo_derecho
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
"""
    Realizamos la importacion de las funciones creadas
    en arbol_listas para poder llevar a cabo las inserciones
    de los nuevos valores de los nodos y ademas traemos una 
    funcion para poder visualizar el arbol.
"""
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
visualizar_arbol(arbol)