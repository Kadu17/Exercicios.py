import math

n1 = int(input("n1: "))
n2 = int(input("n2: "))
deci = input("Escolha uma das operações\n[ + ]- Adição)"
             "\n [ - ]- Subtração\n [ m ]- multiplicação\n [ / ]- Divisão\n""[ ** ]- Potenciação\n [ r ]-Raiz quadrada\n:")
if deci == '+':
    soma = n1 + n2
    print(f"A soma de ambos é {soma}")
elif deci =='-':
    soma = n1 - n2
    print(f"A soma de ambos é {soma}")
elif deci == 'm':
    soma = n1 * n2
    print(f"A soma de ambos é {soma}")
elif deci =='/':
    soma = n1 / n2
    print(f"A soma de ambos é {soma}")
elif deci == '**':
    soma = n1 ** n2
    print(f"A soma de ambos é {soma}")
elif deci == 'r':
    soma = n1 + n2
    soma = math.sqrt((n1 + n2))
    print(f"A raiz quadrada é {soma}")


