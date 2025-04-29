print('Irei calcular o que você pedir.\n' \
'Os números digitados podem ser inteiros ou decimais e informe o operador corretamente.')

operadores = ['somar', 'soma', 'multiplicar', 'multiplicação',
            'dividir', 'divisão', 'subtrair', 'subtração', '+', '-', '*', '/']

while True:
    numero1 = input('Digite um número: ')
    numero2 = input('Digite outro número: ')
    operacao = input('Diga se quer somar, subtrair, dividir ou multiplicar: ')
    operacao = operacao.lower().strip()

    try:
        num1 = float(numero1)
        num2 = float(numero2)

        if operacao not in operadores:
            print('Operador inválido.')
            continue

        elif operacao == 'somar' or operacao == 'soma' or operacao == '+':
            resultado1 = num1 + num2
            print(f'O resultado da soma entre {num1} e {num2} é {resultado1}.')

        elif operacao == 'subtrair' or operacao == 'subtração' or operacao == '-':
            resultado2 = num1 - num2
            print(f'O resultado da subtração entre {num1} e {num2} é {resultado2}.')

        elif operacao == 'dividir' or operacao == 'divisão' or operacao == '/':
            resultado3 = num1 // num2
            print(f'O resultado da divisão de {num1} por {num2} é {resultado3}.')

        elif operacao == 'multiplicar' or operacao == 'multiplicação' or operacao == '*':
            resultado4 = num1 * num2
            print(f'O resultado da multiplicação entre {num1} e {num2} é {resultado4}.')
            
        else: 
            print('Erro desconhecido.')
            continue

    except:
        print('Algum ou ambos os números digitados é inválido.')
        continue
    
    sair = input('Digite [sair] se quiser parar a calculadora: ')
    sair = sair.lower().strip()
    if sair == 'sair' :
        break
    
print('Fim dos cálculos.')
