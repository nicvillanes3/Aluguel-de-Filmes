nome = (input("Digite seu Nome: "))
cpf = (input("Digite seu CPF: "))
idade = int(input("Digite sua idade: "))
plano = (input("Digite o seu plano (Bronze, Prata, Ouro) ")).upper()
print("\nBEM-VINDO À LOCADORA")
print("Cliente: " + nome)
print("CPF: " + cpf)
print("Idade: " + str(idade))
print("Plano: " + plano)

print("\nFILMES DISPONÍVEIS:\n")

filmes_basicos = [
"Forrest Gump",
"Toy Story",
"O Rei Leão",
"Jurassic Park",
"Titanic",
"Harry Potter e a Pedra Filosofal",
"De Volta para o Futuro",
]

filmes_prata_ouro = [
"Matrix",
"Gladiado",
"Os Vingadores",
]

filmes_ouro = [
"Interestelar",
"Clube da Luta",
"A Origem",
]

filmes_18 = [
    "O Exorcista",
    "It — A Coisa",
]

if plano == "BRONZE":

    print("\nFilmes disponíveis:")

    for filme in filmes_basicos:
        print("-", filme)

elif plano == "PRATA" or plano == "OURO":

    print("\nFilmes disponíveis:")

    for filme in filmes_basicos:
        print("-", filme)

    for filme in filmes_prata_ouro:
        print("-", filme)

    if plano == "OURO":

        for filme in filmes_ouro:
            print("-", filme)

    if idade >= 18:

        print("\nFilmes de terror:")

        for filme in filmes_18:
            print("-", filme)

else:
    print("Erro: plano inválido!")