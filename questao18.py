# Questão 18 - Crie uma função que receba duas listas de números e 
# retorne uma nova lista contendo apenas os elementos que estão presentes em ambas as listas.

def valoresiguais(list1, list2):
    listaValoresIguais = []
    
    for i in list1:
        if i in list2:
            listaValoresIguais.append(i)
    
    return listaValoresIguais

tam = int(input('Tamanho: '))

lista1 = list()

print('Lista 1:')
for i in range(tam):
    lista1.append(int(input('Valor: ')))

lista2 = list()

print('Lista 2:')
for i in range(tam):
    lista2.append(int(input('Valor: ')))

print(f'{valoresiguais(lista1, lista2)}')
