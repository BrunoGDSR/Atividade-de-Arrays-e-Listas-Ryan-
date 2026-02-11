#Ex1: usaria lista encadeada pois seria mais eficiente 

#Ex2: Usaria Array por conta se ser pesquisa binaria 

#Ex3: Usando Array, obrigatoriamente teria que ordenar a lista para que pudesse fazer a pesquisa binaria, além de terem tamanhos fixos

#Ex4: A estrutura híbrida é mais rápida que arrays para inserções e eliminações e mais rápida que listas encadeadas, pois limita as operações a um subconjunto dos dados.

#Ex5: 

def linear_search(lista, alvo):
    """
    Realiza uma pesquisa linear na lista para encontrar o alvo.
    Retorna o índice da primeira ocorrência ou -1 se não encontrar.
    """
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1

# Lista fornecida
lista = [3, 7, 1, 9, 5]

# Testes
alvos_para_testar = [9, 5, 2] # 9 e 5 estão na lista, 2 não está

print(f"Lista: {lista}")

for alvo in alvos_para_testar:
    resultado = linear_search(lista, alvo)
    if resultado != -1:
        print(f"O número {alvo} foi encontrado no índice: {resultado}")
    else:
        print(f"O número {alvo} não foi encontrado na lista.")

#Ex6: pesquisa linear "O(n)"

def pesquisa_linear(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1

lista = [3, 7, 1, 9, 5]

#Ex7: selection sort "O(n^2)" 

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        indice_min = i
        for j in range(i + 1, n):
            if lista[j] < lista[indice_min]:
                indice_min = j
        lista[i], lista[indice_min] = lista[indice_min], lista[i]
    return lista

lista = [29, 10, 14, 37, 13]
print(selection_sort(lista))

#Ex8: removaer elementos duplicados de uma lista

def remover_duplicados(lista):
    vistos = set()
    resultado = []

    for num in lista:
        if num not in vistos:
            vistos.add(num)
            resultado.append(num)

    return resultado

lista = [4, 2, 9, 4, 3, 2, 8]
print(remover_duplicados(lista))

#Ex9: intersecção de duas listas

def intersecao_listas(lista1, lista2):
    conjunto2 = set(lista2)
    resultado = []

    for num in lista1:
        if num in conjunto2:
            resultado.append(num)

    return resultado

lista1 = [1, 3, 5, 7, 9]
lista2 = [3, 4, 5, 6, 9]
print(intersecao_listas(lista1, lista2))

#Ex10: segundo maior elemento de uma lista

def segundo_maior(lista):
    maior = segundo = float('-inf')

    for num in lista:
        if num > maior:
            segundo = maior
            maior = num
        elif maior > num > segundo:
            segundo = num

    return segundo

lista = [5, 1, 9, 3, 7]
print(segundo_maior(lista))

#Ex11: mover zeros para o final da lista

def mover_zeros(lista):
    resultado = []
    zeros = 0

    for num in lista:
        if num == 0:
            zeros += 1
        else:
            resultado.append(num)

    resultado.extend([0] * zeros)
    return resultado

lista = [0, 1, 0, 3, 12]
print(mover_zeros(lista))
