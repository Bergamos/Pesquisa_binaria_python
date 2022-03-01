def buscaMenor(arr):
    menor = arr [0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    
    return menor_indice

def ordenacaoPorSelececao(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    
    return novoArr

arrTeste = [9, 4, 1, 5, 3, 7, 6, 8, 2]
print(ordenacaoPorSelececao(arrTeste))