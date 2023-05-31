# Questão 2 - Crie um programa que exibe ao usuário um menu com as seguintes opções: 
# adicionar número na fila; remover número da fila; tamanho da fila; mostrar fila. 
# Todas as opções devem funcionar conforme a ação que ela descreve.

from fila import Fila

fila = Fila()

while True:
    
    print('Escolha uma opção:')
    print('1 - Adicionar;')
    print('2 - Remover;')
    print('3 - Mostrar;')
    print('4 - Sair')
    opcao = int(input('Opção: '))
    
    match opcao:
        case 1:
            fila.enqueue(int(input('Valor: ')))
        case 2:
            print(f'Removido: {fila.dequeue()}')
        case 3:
            if fila.isEmpty():
                print('Fila vazia.')
            fila.mostrar()
        case 4:
            print('Programa encerrado.')
            break
        case _:
            print('Opção inválida.')
            opcao = int(input('Opção: '))
        