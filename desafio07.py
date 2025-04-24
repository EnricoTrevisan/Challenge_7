# O programa deverá receber o nome e a nota dos estudantes pelo teclado e guardar em listas 
# O programa irá parar somente quando a pessoa que tiver realizando o cadastro finalizar 
# O programa deverá calcular a média de cada aluno e guardar em uma lista
# No final apresentar a lista de estudantes  com suas notas e a média

aluno = []
notas1 = []
notas2 = []
notas3 = []
medias = []
resultados = []

while True:
    nome = input("Digite o nome de seu estudante que queira adicionar na lista de estudante. Caso os nomes já tenham sido todos digitados, escreva: 'Terminar': ")
    if nome == "Terminar":
        break

    nota1 = int(input("Digite a primeira nota do/a aluno/a (A nota prática):"))
    nota2 = int(input("Digite a segunda nota do/a aluno/a (A nota oral):"))
    nota3 = int(input("Digite a terceira nota do/a aluno/a (A nota escrita):"))

    aluno.append(aluno)
    notas1.append(nota1)
    notas2.append(nota2)
    notas3.append(nota3)

    resultados = (nota1+nota2+nota3)/3
    medias.append(resultados)

print("Esse é o resultado das informações fornecidas:")
for i in range(len(aluno)):
    print(f"Alunos: {aluno[i]}")
    print(f"Notas: {notas1[i]}, {notas2[i]}, {notas3[i]}")
    print(f"Resultado: {medias[i]}")
