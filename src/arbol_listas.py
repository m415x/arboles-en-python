def crear_nodo_raiz(valor: str) -> list:
    """
    Crea y retorna un nodo raíz con el valor proporcionado.

    El nodo se representa como una lista de tres elementos:
    [valor, hijo_izquierdo, hijo_derecho], donde ambos hijos
    son listas vacías al inicio.

    Args:
        valor (str): Valor que contendrá el nodo raíz.

    Returns:
        list: Nodo raíz representado como lista anidada.
    """

    return [valor, [], []]


def insertar_hijo_izquierdo(arbol: list, valor: str) -> list:
    """
    Inserta un nuevo nodo como hijo izquierdo del nodo actual.

    Si ya existe un hijo izquierdo, este pasará a ser hijo izquierdo
    del nuevo nodo insertado.

    Args:
        arbol (list): Árbol o subárbol donde se insertará el hijo izquierdo.
        valor (str): Valor del nuevo nodo.

    Returns:
        list: Árbol actualizado con el nuevo nodo insertado.
    """
    if not arbol:
        print("Árbol vacío")
        return
    subarbol_izq: list = arbol.pop(1)
    arbol.insert(1, [valor, subarbol_izq, []])
    return arbol


def insertar_hijo_derecho(arbol: list, valor: str) -> list:
    """
    Inserta un nuevo nodo como hijo derecho del nodo actual.

    Si ya existe un hijo derecho, este pasará a ser hijo derecho
    del nuevo nodo insertado.

    Args:
        arbol (list): Árbol o subárbol donde se insertará el hijo derecho.
        valor (str): Valor del nuevo nodo.

    Returns:
        list: Árbol actualizado con el nuevo nodo insertado.
    """
    if not arbol:
        print("Árbol vacío")
        return
    subarbol_der: list = arbol.pop(2)
    arbol.insert(2, [valor, [], subarbol_der])
    return arbol