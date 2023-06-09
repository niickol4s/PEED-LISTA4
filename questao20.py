# Questão 20 - Escreva uma função que receba uma lista de dicionários, 
# onde cada dicionário representa um aluno com as chaves "nome" e "nota". 
# A função deve retornar o nome do aluno com a maior nota.

def alunomaiornota(list):
    
    maiorNota = 0
    nomeAlunoMaiorNota = ''
    
    for i in list:
        if i['Nota'] >= maiorNota:
            maiorNota = i['Nota']
            nomeAlunoMaiorNota = i
    return nomeAlunoMaiorNota

listaAlunos = list()
dctAluno = dict()

while True:
    
    print('Escolha uma opção:')
    print('1 - Adicionar aluno;')
    print('2 - Mostrar lista;')
    print('3 - Mostrar aluno com maior nota;')
    print('0 - Sair')
    opcao = int(input('Opção: '))
    
    match opcao:
        case 1:
            dctAluno.clear()
            dctAluno['Aluno'] = input('Nome: ')
            dctAluno['Nota'] = float(input('Nota: '))
            listaAlunos.append(dctAluno.copy())
        case 2:
            print(listaAlunos)
        case 3:
            print(alunomaiornota(listaAlunos))
        case 0:
            print('Programa encerrado.')
            break
        case _:
            print('Opção inválida.')
            opcao = int(input('Opção: '))        
