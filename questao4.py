from operator import itemgetter

clientes = {}
adicionar = True

while adicionar:
    razao_social = input("Digite a razao social do cliente: ")
    valor_compra = input("Digite o valor total de compra do cliente: ")

    clientes.update({razao_social: valor_compra})

    add =  input("Deseja continuar? [s/n] ")
    if add == "s":
        adicionar = True
    else :
        break

print(clientes)
#itemgetter indica que a ordenação sera pelo valor e nao chave e o reverse coloca em decrescente
for razao_social, valor in sorted(clientes.items(), key=itemgetter(1), reverse=True):
    print("cliente {} valor {} ".format(razao_social, valor))
