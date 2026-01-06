#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

lista_completa = []
linha1 = []
linha2 = []
linha3 = []

print('')
for valores in range(0, 9):
    numeros = int(input(f'Digite o {valores+1}° valor: '))
    if valores < 3:
        linha1.append(numeros)
    elif valores < 6:
        linha2.append(numeros)
    else:
        linha3.append(numeros)
    
lista_completa.append(linha1[:])
lista_completa.append(linha2[:])
lista_completa.append(linha3[:])

print('')
for matriz in range(0, len(lista_completa)):
    for linhas in lista_completa[matriz]:
        print(f'[ {linhas} ]', end = '')
        if linhas % 3 == 0:
            print('')
print('')