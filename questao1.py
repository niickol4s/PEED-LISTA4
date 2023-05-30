# Questão 1 - Implemente uma fila simples e as operações básicas: 
# inserir, remover e mostrar o elemento da frente.

from fila import Fila

fila = Fila()

for i in range(5):
    fila.enqueue(input('Valor: '))
    
print(fila)
print(f'Retirado: {fila.dequeue()}')
print(f'Próximo: {fila.peek()}')
