# este código é sobre o desafio lançado da escola Vai na Web.

# 1° Missão:  Restaurando as Regras Escolares 

nota = float(input("Digite a nota do aluno: "))

if nota >= 6:
    print("Aluno aprovado!")
elif nota <= 5:
    print("Aluno reprovado!")

# 2° Missão: O sistema eleitoral secreto

idade = int(input("Digite a sua idade: "))

if idade >= 16:
    print("Você pode votar!")
else:
    print("Você não pode votar.")

# 3° Missão: Recuperando o sistema de notas

nota = float(input("Digite a nota do aluno: "))

if 90 <= nota <= 100:
    print("Parabéns, você tirou A!")
elif 80 <= nota < 90:
    print("Muito bem, você tirou B.")
elif 70 <= nota < 80:
    print("Bom trabalho, você tirou C.")
elif 60 <= nota < 70:
    print("Fique atento, você tirou D.")
else:
    print("Estude um pouco mais, você tirou F.")

# 4° Missão: Restaurando a indentificação de numeros

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

soma = numero1 + numero2

print("A soma dos dois números é:", soma)

# 5° Missão: Recuperando o cofre de segurança

senha = input("Digite a senha: ")

if senha == "Python123":
    print("Senha correta! Acesso permitido.")
else:
    print("Senha incorreta! Acesso negado.")

# 6° Missão: Reforçando a Segurança e a Contagem do Sistema

numero = 1

while numero <= 10:
    print(numero)
    numero += 1

# 7° Missão: Organizando a Lista

numeros = [8, 3, 10, 1, 5]

numeros.sort()

print("Os números em ordem crescente são:", numeros)

# 8° Missão:  Acessando os Registros de Alunos

nomes = ("Ana", "Bruno", "Carla", "Daniel", "Eduardo")

print("Primeiro nome:", nomes[0])
print("Último nome:", nomes[-1])

# 9° Missão:  Calculando Dobro de um Número

numero = float(input("Digite um número: "))

print(f"O dobro de {numero} é {numero * 2}")

#10° Missão: Contando Letras

nome = input("Digite seu nome: ")

quantidade_letras = len(nome)
print(f"O nome {nome} tem {quantidade_letras} letras.")






