# Tentativa de calcular o IMC pedindo as informações do usuário 
nome = input(f"Digite seu nome: ")
idade = int(input(f"{nome}, digite sua idade: "))
peso = float(input(f"Agora, digite seu peso (em kg): "))
altura = float(input(f"Por último, digite sua alta (em metros): "))

imc = peso / (altura ** 2)
abc = f"{nome}, já que você pesa {peso} kgs e tem {altura: .2f} de altura,"

if imc < 18.5 and imc > 0 :
    print (abc)
    print (f"seu imc é {imc: .2f} e você está abaixo do peso.")
elif imc < 24.9 and imc >= 18.5 :
    print (abc)
    print (f"seu imc é {imc: .2f} e seu peso está normal.")
elif imc >= 25 :
    print (abc)
    print (f"seu imc é {imc: .2f} e você está acima do peso.")
else :
    print ("Os dados informados não levaram a um resultado.")