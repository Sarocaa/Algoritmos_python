print('Irei calcular o que você pedir.')
while True:
    numero1 = input('Digite um número: ')
    numero2 = input('Digite outro número: ')
    operacao = input('Diga se quer somar, subtrair, dividir ou multiplicar. ')


    try:
        num1 = float(numero1)
        num2 = float(numero2)

        if operacao != 'somar' or operacao != 'Somar'\
        or operacao != 'subtrair' or operacao != 'Subtrair'\
        or operacao != 'dividir' or operacao != 'Dividir'\
        or operacao != 'multiplicar' or operacao != 'Multiplicar':
            print('Operador inválido.')
            continue

        elif operacao == 'somar' or operacao == 'Somar':
            resultado1 = num1 + num2
            print(f'O resultado da soma entre {num1} e {num2} é {resultado1}.')

        elif operacao == 'subtrair' or operacao == 'Subtrair':
            resultado2 = num1 - num2
            print(f'O resultado da subtração entre {num1} e {num2} é {resultado2}.')

        elif operacao == 'dividir' or operacao == 'Dividir':
            resultado3 = num1 // num2
            print(f'O resultado da divisão de {num1} por {num2} é {resultado3}.')

        elif operacao == 'multiplicar' or operacao == 'Multiplicar':
            resultado4 = num1 * num2
            print(f'O resultado da multiplicação entre {num1} e {num2} é {resultado4}.')
            
        else: 
            print('Erro desconhecido.')
            continue

    except:
        print('Algum ou ambos os números digitados é inválido.')
        continue
    
    sair = input('Digite [sair] se quiser parar a calculadora: ')
    if sair == 'sair' :
        break
    
print('Fim dos cálculos.')