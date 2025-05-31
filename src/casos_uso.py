from operaciones_basicas import visualizar_arbol, recorrer_preorden

# Árbol de ejemplo
# fmt: off
arbol_ejemplo = [
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

# Demostración
print("Visualización:")
visualizar_arbol(arbol_ejemplo)

print("\nRecorrido preorden:")
recorrer_preorden(arbol_ejemplo)
