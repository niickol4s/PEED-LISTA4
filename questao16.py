# Questão 16 - Escreva uma função que receba uma lista de números e retorne a soma de todos os elementos.

def soma(list):
    return sum(list)

tam = int(input('Tamanho: '))

lista = list()

for i in range(tam):
    lista.append(int(input('Valor: ')))
    
print(f'{soma(lista)}')
