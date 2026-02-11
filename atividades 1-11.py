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

#Ex6: 

