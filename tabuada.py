import os
while True:
    while True:
        try:
            tabuada = int(input("tabuada de que: "))
            for i in range(1, 11):
                vezes = tabuada * i
                print(f"{tabuada}x{i} = {vezes}")
            break
        except ValueError:
            os.system("cls")
            print("Entrada de dados invalida!!!")
    while True:
        resp = input("\nOutra tabuada? (s/n): ")
        if resp == "s" or resp == "n":
            os.system("cls")
            break
        else:
            os.system("cls")
            print("\nResposta incorreta. Responda somente com (s) para sim e (n) para não.")
    if resp == "n":
        break