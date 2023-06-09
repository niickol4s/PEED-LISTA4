# Questão 8 - Escreva um programa que leia uma lista de números inteiros 
# e crie uma lista encadeada simples com esses números em ordem inversa.

from lista import Lista

tam = int(input('Tamanho: '))

lista = Lista()
listaInversa = Lista()

for i in range(tam):
    lista.inserir_final(int(input('Valor: ')))

lista.mostrar()

while not lista.isEmpty():
    listaInversa.inserir_final(lista.remover_final())

listaInversa.mostrar()
