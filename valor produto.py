import os

def outroproduto ():
    while True:
        print("Quer conferir o valor de outro produto? (s/n)")
        resp = input("R:").lower()
        if resp == "s" or resp == "n":
            return resp
        else:
            os.system("cls")
            print("Resposta incorreta. Responda somente com (s) para sim e (n) para não.")
while True:
    while True:
        try:
            valor = float(input("digite o valor do produto: "))
            break
        except ValueError:
            os.system("cls")
            print("Erro! Digite um valor válido.") 
    while True:
        print("Qual sera a forma de pagamento?\n\nÀ vista (Dinheiro ou PIX) = 1\nÀ Vista no cartão de crédito = 2"
        "\nParcelado no cartão em duas vezes = 3\nParcelado no cartão em três vezes ou mais = 4")
        while True:
            forma = int(input("R:"))
            if forma == 1:
                nvalor = valor - (valor * 0.15)
                print(f"\nO valor final fica em: R${nvalor}\n\n")
                resp = outroproduto()
                os.system("cls")
                if resp != "s":
                    break
            elif forma == 2:
                nvalor = valor - (valor * 0.1)
                print(f"\nO valor final fica em: R${nvalor}\n\n")
                resp = outroproduto()
                os.system("cls")
                if resp != "s":
                    break
            elif forma == 3:
                print(f"\nO valor final fica em: R${valor}\n\n")
                resp = outroproduto()
                os.system("cls")
                if resp != "s":
                    break
            elif forma == 4:
                nvalor = valor + (valor * 0.10)
                print(f"\nO valor final fica em: R${nvalor}\n\n")
                resp = outroproduto()
                os.system("cls")
                if resp != "s":
                    break
            else:
                os.system("cls")
                print("Resposta incorreta, atente-se aos numeros de cada forma de pagamento e tente novamente")
            if forma != 1 or forma != 2 or forma != 3 or forma != 4:
                break
        if forma == 1 or forma == 2 or forma == 3 or forma == 4:
            break
    if resp == "n":
        print("Certo, boas compras\n")
        break