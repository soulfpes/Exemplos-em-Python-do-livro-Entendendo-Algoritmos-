# Algoritmo de Ordenação por Seleção
# Serve para colocar os números de uma lista em ordem crescente.

def encontra_menor(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

def ordenacao_por_selecao(arr):
    novo_arr = []
    for i in range(len(arr)):
        menor = encontra_menor(arr)
        novo_arr.append(arr.pop(menor))
    return novo_arr

print("Lista ordenada:", ordenacao_por_selecao([5, 3, 6, 2, 10]))
