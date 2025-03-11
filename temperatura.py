import os
while True:
    while True:
        try:
            print("\nPara comparação 32°F é igual a 0°C "
            "e 212°F sao iguais a 100°C")
            grauF = int(input("\nTemperatura em Fahrenheit: "))
            grauC = float(5*(grauF - 32) / 9)
            print(f"{grauF}°F em Celsius é aproximadamente: {grauC:.2f}°C")
            break
        except ValueError:
            os.system("cls")
            print("Entrada de dados invalida!!!")
    while True:
        resp = input("\nQuer conferir outra temperatura? (s/n): ")
        if resp == "s" or resp == "n":
            os.system("cls")
            break
        else:
            os.system("cls")
            print("\nResposta incorreta. Responda somente com (s) para sim e (n) para não.")
    if resp == "n":
        break