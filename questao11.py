# Questão 11 - Escreva um programa que leia uma lista de nomes e 
# crie uma lista encadeada dupla com esses nomes em ordem alfabética.

from listaDupla import ListaEncadeadaDupla

lista = list()
listaOrdenada = ListaEncadeadaDupla()

tam = int(input('Tamanho: '))

for i in range(tam):
    lista.append(input('Nome: '))
lista.sort(reverse=True)

for i in lista:
    listaOrdenada.inserir_ini(i)
print(listaOrdenada)
