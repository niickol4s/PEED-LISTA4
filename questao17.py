# Questão 17 - Implemente uma função que receba uma lista de strings e 
# retorne uma nova lista contendo apenas as strings que possuem mais de 5 caracteres.

def string(list):
    strLista = []
    
    for i in list:
        if len(i) > 5:
            strLista.append(i)
    return strLista

tam = int(input('Tamanho: '))

lista = list()

for i in range(tam):
    lista.append((input('Palavra: ')))

print(f'{string(lista)}')
