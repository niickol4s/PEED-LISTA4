# Questão 10 - Implemente uma lista encadeada dupla e as operações básicas: 
# inserir no início, inserir no final, remover do início, remover do final e exibir a lista.

from listaDupla import ListaEncadeadaDupla

listaDupla = ListaEncadeadaDupla()

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
            listaDupla.inserir_ini(int(input('Valor: ')))
        case 2:
            listaDupla.inserir_fin(int(input('Valor: ')))
        case 3:
            listaDupla.remover_ini()
        case 4:
            listaDupla.remover_fin()
        case 5:
            if listaDupla.is_empyt():
                print('Lista vazia.')
            print(listaDupla)
        case 0:
            print('Programa encerrado.')
            break
        case _:
            print('Opção inválida.')
            opcao = int(input('Opção: '))
        