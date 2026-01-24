#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

lista_completa = [[], [], []]

print('')
for valores in range(0, 9):
    numeros = int(input('Digite um valor: '))

    if valores < 3:
        lista_completa[0].append(numeros)
    elif valores < 6:
        lista_completa[1].append(numeros)
    else:
        lista_completa[2].append(numeros)

print('\nMatriz completa:\n')
for matriz in range(0, len(lista_completa)):
    for linhas in lista_completa[matriz]:
        print(f'[ {linhas} ]', end = '')
    print('')
print('')