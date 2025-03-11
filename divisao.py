import os
while True:
    while True:
        try:
            valorA = int(input("Digite o valor para A: "))
            valorB = int(input("Digite o valor para B: "))
            break
        except ValueError:
            print("Entrada invalida, digite apenas numeros inteiros!")
    while True:
        if valorA != 0 and valorB != 0:
            if valorA < valorB:
                print("\no valor de A é menor que o valor de B, a divisão nao pode acontecer")
                break
            else:
                quo = valorA // valorB
                resto = valorA % valorB
                print(f"\nO quociente da divisão de {valorA} por {valorB} é: {quo}")
                print(f"O resto da divisão de {valorA} por {valorB} é: {resto}")
                break
        else:
            print("\nNão é possivel dividir por 0, insira numeros inteiros e diferentes de 0")
            break
    while True:
        resp = input("\ntentar denovo? (s/n): ")
        os.system("cls")
        if resp == "s" or resp == "n":
            break
        else:
            print("Entrada invalida, responda com s para sim e n para não")
    if resp == "n":
        break