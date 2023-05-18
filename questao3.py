import random as rd
nomes = []
continuar = True
while continuar:
    nomes.append(input("Digite um nome: "))
    cont = input("Deseja continuar? [s/n] ")
    if cont == "s":
        continuar = True
    else:
        break

escolha = rd.choice(nomes)
print("Nome escolhido foi: ", escolha)
