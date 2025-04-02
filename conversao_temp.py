# Teste para temperaturas 
temperatura = input("Qual a temperatura que você deseja converter? ")
unidade = input("Essa temperatura é em graus Celsius (C) ou Fahrenheit (F)? ")
calculo1 = (float(temperatura) - 32) / 1.8 # Numero do usuario em F
calculo2 = (float(temperatura) * 1.8) + 32 # Numero do usuario em C

if unidade == "C" or unidade == "c":
    print(f"O resultado de {temperatura} graus Celsius em Fahrenheit é {calculo2: .2f} graus.")
elif unidade == "F" or unidade == "f":
    print(f"O resultado de {temperatura} graus Fahrenheit em Celsius é {calculo1: .2f} graus.")
else:
    print("A temperatura ou unidade selecionada é incompatível.")