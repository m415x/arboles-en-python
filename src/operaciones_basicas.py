def visualizar_arbol(arbol, prefijo="", es_ultimo=True, es_raiz=True):
    if arbol:
        if es_raiz:
            print(arbol[0])

            nuevo_prefijo = ""
        else:
            print(prefijo + ("└── " if es_ultimo else "├── ") + str(arbol[0]))

            nuevo_prefijo = prefijo + ("    " if es_ultimo else "│   ")

        hijos = []

        if arbol[1]:
            hijos.append(arbol[1])

        if arbol[2]:
            hijos.append(arbol[2])

        for i, hijo in enumerate(hijos):
            ultimo_hijo = i == len(hijos) - 1

            visualizar_arbol(hijo, nuevo_prefijo, ultimo_hijo, False)
