#Crie um programa que leie o nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

lista_completa = []
lista_nome = []
lista_notas = []

while True:
    nome = str(input('\nDigite o nome do aluno: ')).strip().upper()

    nota1 = float(input(f'Qual a primeira nota do(a) {nome}? '))
    while nota1 < 0 or nota1 >= 11:
        nota1 = float(input(f'Nota inválida! Qual a primeira nota de {nome}? '))

    nota2 = float(input(f'Qual a segunda nota do(a) {nome}? '))
    while nota2 < 0 or nota2 >= 11:
        nota2 = float(input(f'Nota inválida! Qual a segunda nota de {nome}? '))
    
    lista_nome.append(nome)
    lista_notas.append(nota1)
    lista_notas.append(nota2)
    lista_nome.append(lista_notas[:])

    lista_completa.append(lista_nome[:])
    lista_nome.clear()
    lista_notas.clear()

    continuar = str(input('\nDeseja continuar [S/N]? ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Opção inválida! Deseja continuar [S/N]? ')).strip().upper()[0]
    
    if continuar in 'N':
        print('-' * 30)
        print(f'{'Número':<10}{'Nome':^10}{'Média':>10}')
        print('-' * 30)

        for primeira_percorrida in range(0, len(lista_completa)):
            soma = 0
            media = 0
            for segunda_percorrida in lista_completa[primeira_percorrida][1]: 
                soma += segunda_percorrida
                media = soma / 2
            print(f'{primeira_percorrida:<10}{lista_completa[primeira_percorrida][0]:^10}{media:>10}')
        print('-' * 30)

        while True:
            escolher = int(input('\nQual boletim deseja ver (999 para parar o programa)? '))
            if escolher == 999:
                print('\nVocê parou o programa!\n')
                break
            else:
                if escolher >= len(lista_completa) or escolher < 0:
                    print('Aluno inexistente! Qual boletim deseja ver (999 para parar o programa)? ')
                else:
                    print('-' * 30)
                    print(f'Notas de {lista_completa[escolher][0]}: {lista_completa[escolher][1]}')
                    print('-' * 30)
        break