# Questão 4 - Escreva um programa que leia uma frase do usuário e 
# verifique se ela é um palíndromo 
# (ou seja, pode ser lida da mesma forma tanto da esquerda 
# para a direita quanto da direita para a esquerda). 
# Utilize uma fila para armazenar os caracteres da frase.
        
from fila import Fila

fila = Fila()

def verificarpolindromo(frs):
    
    aux = []
    string = ''
    
    for i in frs:
        fila.enqueue(i)
    while not fila.isEmpty():
        aux.append(fila.dequeue())
    aux.reverse()
    for i in aux:
        fila.enqueue(i)
    while not fila.isEmpty():
        string += fila.dequeue()
    if string == frs:
        return True
    else:
        return False
    
frase = input('Frase: ')
print(verificarpolindromo(frase))
