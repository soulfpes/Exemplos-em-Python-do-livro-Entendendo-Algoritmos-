# Implementação simples de busca binária
# Serve para encontrar a posição de um número em uma lista ORDENADA.

def busca_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

numeros = [1, 3, 5, 7, 9, 11]
print("Lista:", numeros)
print("Posição do número 7:", busca_binaria(numeros, 7))
