def visualizar_arbol(
    arbol: list,
    prefijo: str = "",
    es_ultimo: bool = True,
    es_raiz: bool = True,
) -> None:
    """
    Visualiza un árbol binario de manera estructurada.

    Args:
        arbol (list): Lista que representa el árbol [valor, izquierdo, derecho]
        prefijo (str): Prefijo para la indentación
        es_ultimo (bool): Si es el último hijo de su padre
        es_raiz (bool): Si es el nodo raíz

    Returns:
        None: Llama recursivamente a la función para visualizar el árbol.
    """
    if arbol:
        # Mostrar el nodo actual
        if es_raiz:
            print(arbol[0])
            nuevo_prefijo: str = ""
        else:
            print(prefijo + ("└── " if es_ultimo else "├── ") + str(arbol[0]))
            nuevo_prefijo: str = prefijo + ("    " if es_ultimo else "│   ")

        hijo_primero: list = arbol[2]
        hijo_segundo: list = arbol[1]

        # Procesar hijos en el orden determinado
        hijos: list = []
        if hijo_primero:
            hijos.append(hijo_primero)
        if hijo_segundo:
            hijos.append(hijo_segundo)

        for i, hijo in enumerate(hijos):
            ultimo_hijo: bool = i == len(hijos) - 1
            visualizar_arbol(hijo, nuevo_prefijo, ultimo_hijo, False)