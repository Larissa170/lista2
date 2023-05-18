if __name__ == '__main__':

    idade = int(input("Digite uma idade: "))
    maior_idade = int(idade)
    menor_idade = int(idade)

    while idade > 0:
        idade = int(input("Digite uma idade: "))

        if maior_idade < int(idade):
            maior_idade = int(idade)

        if menor_idade > int(idade):
            menor_idade - int(idade)

    print("Maior idade: ", maior_idade)
    print("Menor Idade: ", menor_idade)
    print("Media entre a maior e menor idade: ", (maior_idade + menor_idade) / 2 )