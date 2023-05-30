# Questão 3 - Escreva um programa que leia uma sequência de números inteiros e 
# insira-os em uma fila até que um número negativo seja digitado. 
# Em seguida, remova todos os elementos da fila e exiba-os na ordem em que foram inseridos.

from fila import Fila

fila = Fila()

while True:
    
    valor = int(input('Valor: '))
    if valor < 0:
        break
    fila.enqueue(valor)
    
while not fila.isEmpty():
    print(fila.dequeue())
print(f'{fila}')
