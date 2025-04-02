print('Informe 3 lados inteiros de um triângulo para eu dizer que tipo de triângulo é.')
lado1 = input('Primeiro lado: ')
lado2 = input('Segundo lado: ')
lado3 = input('Terceiro lado: ')

try:
    lado_a = int(lado1)
    lado_b = int(lado2)
    lado_c = int(lado3)
    lados = sorted([lado_a, lado_b, lado_c], reverse= True)

    if lados[0] < lados[1] + lados[2] :
        if lados[0] == lados[1] == lados[2] :
            print('O triângulo é equilátero.')
        elif lados[0] != lados[1] and lados[0] != lados[2] and lados[1] != lados[2]:
            print('O triângulo é escaleno.')
        else:
            print('O triângulo é isóceles.') 
    else:
        print('Os lados não são válidos pra formar um triângulo.')

except: 
    print ('Os valores informados são inválidos para formar um triângulo.')