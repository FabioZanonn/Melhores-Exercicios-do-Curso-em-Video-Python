#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

lista_completa = []
numero_individual = []

print('')
for valores in range(0, 9):
    numeros = int(input(f'Digite o {valores+1}° valor: '))
    numero_individual.append(numeros)
    lista_completa.append(numero_individual[:])
    numero_individual.clear()

for matriz in range(0, len(lista_completa)):
    if matriz % 3 == 0:
        print('')
    print(f'[ {lista_completa[matriz][0]} ]', end= '')
print('\n')