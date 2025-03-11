import os
while True:

    while True:
        try:
            ladoA = int(input("valor do lado A: "))
            ladoB = int(input("valor do lado B: "))
            ladoC = int(input("valor do lado C: "))
            if all(lado >= 1 for lado in [ladoA, ladoB, ladoC]):
                break
            else:
                os.system("cls")
                print("Todos os lados devem ser maiores ou iguais a 1!")
        except ValueError:
            print("Entrada de dados invalida!!!")

    if ladoA == ladoB == ladoC:
        print("\nEste é um triângulo equilatero (tem 3 lados iguais)")
    elif ladoA == ladoB != ladoC:
        print("\nEste é um triângulo isosceles (tem 2 lados iguais)")
    elif ladoA == ladoC != ladoB:
        print("\nEste é um triângulo isosceles (tem 2 lados iguais)")
    elif ladoB == ladoC != ladoA:
        print("\nEste é um triângulo isosceles (tem 2 lados iguais)")
    else:
        print("\nEste é um triângulo escaleno (nenhum dos lados iguais)")

    while True:
        resp = input("\nQuer conferir outro triângulo? (s/n): ")
        if resp == "s" or resp == "n":
            os.system("cls")
            break
        else:
            os.system("cls")
            print("\nResposta incorreta. Responda somente com (s) para sim e (n) para não.")
    if resp == "n":
        break