if __name__ == '__main__':
    cont = 0
    nome_melhor_tempo = ""
    melhor_tempo = 0
    pior_tempo = 0
    pior_desempenho = ""
    tempo_medio = 0.0
    soma_tempo = 0
    tempo12_15 = 0

    while cont < 7:
        nome = input("Digite o nome do aluno: ")
        tempo = input("Digite o tempo em segundos do aluno: ")

        if cont == 0:
            nome_melhor_tempo = nome
            melhor_tempo = int(tempo)
            pior_tempo = int(tempo)
            pior_desempenho = nome
        else:
            if melhor_tempo > int(tempo):
                melhor_tempo = int(tempo)
                nome_melhor_tempo = nome

            if pior_tempo < int(tempo):
                pior_tempo = int(tempo)
                pior_desempenho = nome

        if 12 < int(tempo) < 15:
            tempo12_15 += 1

        soma_tempo += int(tempo)
        cont += 1

    tempo_medio = soma_tempo/cont

    print("melhor nadador: ", nome_melhor_tempo)
    print("pior desempenho: ", pior_desempenho)
    print("tempo medio nadadores: ", tempo_medio)
    print("quantidade  entre 12  e 15 ", tempo12_15)

