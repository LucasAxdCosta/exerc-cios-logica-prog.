#--------------------------------------------------------------------------------------------------------------
while True:
    try:
        ano_atual = int(input("em que ano estamos?: "))
        mes_atual = int(input("em que mês estamos? (1 a 12): "))
        dia_atual = int(input("em que dia estamos? (1 a 30): "))
        if ano_atual > 1 and 1 <= mes_atual <= 12 and 1 <= dia_atual <= 30:
            break
        else:
            print("Por favor, insira uma data válida")
    except ValueError:
        print("Entrada inválida! Digite números inteiros.")
#--------------------------------------------------------------------------------------------------------------
while True:
    try:
        ano_nasc = int(input("\nem que ano voce nasceu?: "))
        mes_nasc = int(input("em que mês voce nasceu? (1 a 12): "))
        dia_nasc = int(input("em que dia voce nasceu? (1 a 30): "))
        if ano_nasc > 0 and ano_nasc <= ano_atual and 1 <= mes_nasc <= 12 and 1 <= dia_nasc <= 30:
            break
        else:
            print("Por favor, insira uma data válida")
    except ValueError:
        print("Entrada inválida! Digite números inteiros.")
#--------------------------------------------------------------------------------------------------------------
anos_vividos = ano_atual - ano_nasc
meses_vividos = mes_atual - mes_nasc
dias_vividos = dia_atual - dia_nasc

if dias_vividos < 0:
    dias_vividos += 30
    meses_vividos -= 1
if meses_vividos < 0:
    meses_vividos += 12
    anos_vividos -= 1

print(f"Você já viveu aproximadamente:")
print(f"{anos_vividos} anos, {meses_vividos} meses e {dias_vividos} dias.")
