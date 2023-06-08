# Questão 19 - Implemente uma função que receba uma lista de palavras e 
# retorne a palavra mais longa presente na lista.

def palavralonga(list):
    
    listaPalavra = ''
    for i in list:
        if len(i) > len(listaPalavra):
            listaPalavra = i
            
    return listaPalavra

tam  = int(input('Tamanho: '))

lista = list()

for i in range(tam):
    lista.append(input('Palavra: '))

print(f'{palavralonga(lista)}')
