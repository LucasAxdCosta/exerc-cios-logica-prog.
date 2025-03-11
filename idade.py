import os
nome = input("Qual seu nome?: ")
while True:
    try:
        idade = int(input("Qual sua idade?: "))
        if idade >= 1:
            if idade >= 18:
                print(f"Seu nome é {nome} e voce é maior de idade")
            else:
                print(f"Seu nome é {nome} e voce é menor de idade")
            break
        else:
            os.system("cls")
            print("Informe uma idade válida")
    except ValueError:
        print("digite uma idade válida")