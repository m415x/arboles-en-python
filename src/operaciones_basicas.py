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

    # Constantes con caracteres Unicode para la visualización
    RAMA = "├── "
    ULTIMO = "└── "
    VERTICAL = "│   "
    ESPACIO = "    "

    # Si el árbol existe
    if arbol:
        # Mostrar el nodo actual
        if es_raiz:
            # Si es el nodo raíz, imprimirlo sin prefijo ni decoración
            print(arbol[0])

            # Reiniciar el prefijo para los hijos de la raíz
            nuevo_prefijo: str = ""
        else:
            # Para nodos no raíz:
            # 1. Imprimir el prefijo acumulado (indentación)
            # 2. Usar ULTIMO (└──) si es el último hijo de su padre, RAMA (├──) si no
            # 3. Añadir el valor del nodo actual
            print(prefijo + (ULTIMO if es_ultimo else RAMA) + str(arbol[0]))

            # Calcular nuevo prefijo para los hijos:
            # - Si es último hijo: añadir espacios en blanco ("    ")
            # - Si no: añadir barra vertical ("│   ") para conectar visualmente
            nuevo_prefijo: str = prefijo + (ESPACIO if es_ultimo else VERTICAL)

        # Obtener el hijo derecho (se procesa primero para efecto espejo)
        hijo_primero: list = arbol[2]

        # Obtener el hijo izquierdo
        hijo_segundo: list = arbol[1]

        # Procesar hijos en el orden determinado
        hijos: list = []

        # Si existe hijo derecho
        if hijo_primero:
            hijos.append(hijo_primero)

        # Si existe hijo izquierdo
        if hijo_segundo:
            hijos.append(hijo_segundo)

        # Recorrer todos los hijos para procesarlos recursivamente
        for i, hijo in enumerate(hijos):
            # Determinar si es el último hijo para usar el conector adecuado
            ultimo_hijo: bool = i == len(hijos) - 1

            # Llamada recursiva
            visualizar_arbol(hijo, nuevo_prefijo, ultimo_hijo, False)


def recorrer_preorden(arbol: list) -> None:
    """
    Realiza un recorrido en preorden del árbol (raíz → izq → der)
    e imprime los valores de los nodos en ese orden.

    Args:
        arbol (list): Árbol binario representado con listas anidadas.

    Returns:
        None: Llama recursivamente a la función para recorrer el árbol.
    """
    if arbol:
        print(arbol[0], end=" ")
        recorrer_preorden(arbol[1])
        recorrer_preorden(arbol[2])


def recorrer_inorden(arbol: list) -> None:
    """
    Realiza un recorrido en inorden del árbol (izq -> raíz -> der)
    e imprime los valores de los nodos en ese orden.

    Args:
        arbol (list): Árbol binario representado con listas anidadas.

    Returns:
        None: Llama recursivamente a la función para recorrer el árbol.
    """
    if arbol:
        recorrer_inorden(arbol[1])
        print(arbol[0], end=" ")
        recorrer_inorden(arbol[2])


def recorrer_postorden(arbol: list) -> None:
    """
    Realiza un recorrido en postorden del árbol (izq -> der -> raíz)
    e imprime los valores de los nodos en ese orden.

    Args:
        arbol (list): Árbol binario representado con listas anidadas.

    Returns:
        None: Llama recursivamente a la función para recorrer el árbol.
    """
    if arbol:
        recorrer_postorden(arbol[1])
        recorrer_postorden(arbol[2])
        print(arbol[0], end=" ")


def altura_arbol(arbol: list) -> int:
    """
    Calcula la altura máxima de un árbol binario representado con listas anidadas.

    La altura de un árbol se define como el número de aristas en el camino más largo
    desde el nodo raíz hasta una hoja. Un árbol vacío tiene altura 0.

    Args:
        arbol (list): Árbol binario representado como lista anidada.

    Returns:
        int: Altura del árbol. Retorna 0 para árbol vacío o solo con raíz.
    """
    # Caso base 1: árbol vacío
    if not arbol:
        return 0  # Altura 0 para árbol vacío por convención en esta implementación

    # Caso recursivo: 1 (nodo actual) + máximo entre alturas de subárboles
    return 1 + max(
        altura_arbol(arbol[1]),  # Altura subárbol izquierdo
        altura_arbol(arbol[2]),  # Altura subárbol derecho
    )


def peso_arbol(arbol: list) -> int:
    """
    Calcula el número total de nodos en un árbol binario representado con listas anidadas.

    El peso de un árbol es la cantidad total de nodos que contiene.
    Un árbol vacío tiene peso 0.

    Args:
        arbol (list): Lista que representa el árbol en formato [valor, hijo_izquierdo, hijo_derecho]
            o lista vacía [] para árbol vacío.

    Returns:
        int: Cantidad total de nodos en el árbol.
    """
    # Caso base: árbol vacío
    if not arbol:
        return 0

    # Caso recursivo: 1 (nodo actual) + peso subárbol izquierdo + peso subárbol derecho
    return 1 + peso_arbol(arbol[1]) + peso_arbol(arbol[2])
