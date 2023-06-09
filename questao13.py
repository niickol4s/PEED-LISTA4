# Questão 13 - Implemente uma lista encadeada circular e as operações básicas: 
# inserir no início, inserir no final, remover do início, remover do final e exibir a lista.

from listaCircular import ListaEncadeadaCircular

listaCircular = ListaEncadeadaCircular()

while True:
    
    print('Escolha uma opção:')
    print('1 - Inserir no início;')
    print('2 - Inserir no final;')
    print('3 - Remover no início;')
    print('4 - Remover no final;')
    print('5 - Mostrar;')
    print('0 - Sair')
    opcao = int(input('Opção: '))
    
    match opcao:
        case 1:
            listaCircular.inserir_ini(int(input('Valor: ')))
        case 2:
            listaCircular.inserir_fin(int(input('Valor: ')))
        case 3:
            if listaCircular.is_empty():
                print('Lista vazia.')
            listaCircular.remover_ini()
        case 4:
            if listaCircular.is_empty():
                print('Lista vazia.')
            listaCircular.remover_fin()
        case 5:
            if listaCircular.is_empty():
                print('Lista vazia.')
            print(listaCircular)
        case 0:
            print('Programa encerrado.')
            break
        case _:
            print('Opção inválida.')
            opcao = int(input('Opção: '))
            