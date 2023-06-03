# Questão 7 - Implemente uma lista encadeada simples e as operações básicas: 
# inserir no início, inserir no final, remover do início, remover do final e exibir a lista.

from lista import Lista

lista = Lista()

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
            lista.inserir_inicio(int(input('Valor: ')))
        case 2:
            lista.inserir_final(int(input('Valor: ')))
        case 3:
            lista.remover_inicio()
        case 4:
            lista.remover_final()
        case 5:
            if lista.isEmpty():
                print('Lista vazia.')
            lista.mostrar()
        case 0:
            print('Programa encerrado.')
            break
        case _:
            print('Opção inválida.')
            opcao = int(input('Opção: '))
          