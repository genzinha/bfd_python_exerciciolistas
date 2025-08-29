"""
9- Crie uma lista valores = [10, 20, 30, 40]. Use um laço for para calcular manualmente a soma de todos os valores.

10- Use input para receber 3 notas de dois alunos. As notas de cada aluno precisam ser armazenadas em uma lista separada que deve ser armazenada dentro de outra lista chamada notas, exemplo:
notas = [[7, 8, 9], [6, 5, 7]]. No fim, imprima a média de cada aluno.

11- Usando list comprehension, crie um tabuleiro de xadrez vazio e depois adicione todas as peças do jogo na posição inicial. Para melhorar a visualização do tabuleiro, identifique as posições do tabuleiro da seguinte forma:

[ ] - para posições vazias
tor - para a torre
cav - para o cavalo
bis - para o bispo
rai - para a rainha
rei - para o rei
pea - para o peão
Por fim imprima o tabuleiro na tela, deixando cada linha da matriz abaixo da outra. (Dica você pode usar a biblioteca numpy para auxiliar na impressão da matriz)

"""

# 1- Crie uma lista chamada livros contendo 3 livros diferentes e exiba a lista na tela.

livros = ["O Nome da Rosa", "Crime e Castigo", "O Hobbit"]
print(livros)

#2- Usando a lista livros, exiba apenas o primeiro e o último elemento.

print(livros[0],"e", livros[2])

#3- Adicione mais dois livros à lista livros usando o método append() e exiba a lista atualizada.

livros.append("Apanhador no Campo de Centeio")
livros.append("O Guia do Mochileiro das Galáxias") #em sua homenagem, prof
print(livros)

#4- Insira o livro "Duna" na segunda posição da lista livros usando insert().

livros.insert(1, "Duna")
print(livros)

#5- Remova o livro "Silêncio dos inocentes" da lista usando remove(). Se ele não existir, exiba a mensagem "Livro não encontrado".

if "Silêncio dos Inocentes" in livros:
    livros.remove("Silêncio dos Inocentes")
    print(livros)
else:
    print("Livro não encontrado")

#6- Crie uma lista chamada números com os valores [1, 2, 3, 2, 4, 2, 5]. Mostre quantas vezes o número 2 aparece na lista.

numeros = [1, 2, 3, 2, 4, 2, 5]
print(numeros.count(2))

#7- Percorra a lista livros e exiba cada livro com a frase: "O livro <nome do livro> é interessante"

for livro in livros:
    print(f"O nome livro {livro} é interessante")

#8- Dada a lista idades = [12, 18, 25, 14, 30], use um laço para exibir somente as idades maiores ou iguais a 18.

idades = [12, 18, 25, 14, 30]

for idade in idades:
    if idade >= 18:
        print(idade)

# 9- Crie uma lista valores = [10, 20, 30, 40]. Use um laço for para calcular manualmente a soma de todos os valores.

valores = [10, 20, 30, 40]
soma = 0
for valor in valores:
  soma += valor
print(f"A soma dos valores é: {soma}")

# 10- Use input para receber 3 notas de dois alunos. As notas de cada aluno precisam ser armazenadas em uma lista separada que deve ser armazenada dentro de outra lista chamada notas, exemplo:
# notas = [[7, 8, 9], [6, 5, 7]]. No fim, imprima a média de cada aluno.

notas = []

for x in range(2): 
    aluno_notas = []  
    print(f"Digite as notas do aluno {x+1}:")
    for z in range(3): 
        nota = float(input(f"Nota {z+1}: "))
        aluno_notas.append(nota)
    notas.append(aluno_notas) 

print("Notas:", notas)

for i, aluno in enumerate(notas):
    media = sum(aluno) / len(aluno)
    print(f"Média do aluno {i+1}: {media:.2f}")

# 11- Usando list comprehension, crie um tabuleiro de xadrez vazio e depois adicione todas as peças do jogo na posição inicial. Para melhorar a visualização do tabuleiro, identifique as posições do tabuleiro da seguinte forma:

# [ ] - para posições vazias
# tor - para a torre
# cav - para o cavalo
# bis - para o bispo
# rai - para a rainha
# rei - para o rei
# pea - para o peão
# Por fim imprima o tabuleiro na tela, deixando cada linha da matriz abaixo da outra. (Dica você pode usar a biblioteca numpy para auxiliar na impressão da matriz)

import numpy as np

tabuleiro = [['[ ]' for _ in range(8)] for _ in range(8)]

for i in range(8):
    tabuleiro[1][i] = 'pea'
    tabuleiro[6][i] = 'pea'

tabuleiro[0][0] = 'tor'
tabuleiro[0][1] = 'cav'
tabuleiro[0][2] = 'bis'
tabuleiro[0][3] = 'rai'
tabuleiro[0][4] = 'rei'
tabuleiro[0][5] = 'bis'
tabuleiro[0][6] = 'cav'
tabuleiro[0][7] = 'tor'

tabuleiro[7][0] = 'tor'
tabuleiro[7][1] = 'cav'
tabuleiro[7][2] = 'bis'
tabuleiro[7][3] = 'rai'
tabuleiro[7][4] = 'rei'
tabuleiro[7][5] = 'bis'
tabuleiro[7][6] = 'cav'
tabuleiro[7][7] = 'tor'

for linha in tabuleiro:
    print(' '.join(linha))