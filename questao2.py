from fila import Fila


fila = Fila()
while True:
    
    valoresFila = []
    
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
            valor = int(input('Valor: '))
            
            if valor in valoresFila:
                fila.dequeue(valor)
            else:
                print('Valor não encontrado.')
        case 3:
            fila.peek()
        case 4:
            print('Programa encerrado.')
            break
        case _:
            print('Opção inválida.')
            opcao = int(input('Opção: '))
    
        