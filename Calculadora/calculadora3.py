"""
Programa_calculadora
Descrição: Este programa calcula usando as 4 operações
Autora: Ivone Rosales
Versão: 0.0.3
Data: 24/08/2022
"""


def welcome():
    print('''
Bem-vindo(a) à Calculadora!
''')


# Definindo a função
def calculate():
    operacao = input ("""
Digite a operação matemática:
+ para adição
- para subtração
* para multiplicação
/ para divisão
 \n """)

    numero_1 = int(input("Digite o primeiro número: "))
    numero_2 = int(input("Digite o segundo número: "))

# Adição
    if operacao == "+":
        print("{} + {} = ".format(numero_1, numero_2))
        print(numero_1 + numero_2)

# Subtração
    elif operacao == "-":
        print("{} - {} = ".format(numero_1, numero_2))
        print(numero_1 - numero_2)

# Multiplicação
    elif operacao == "*":
        print("{} * {} = ".format(numero_1, numero_2))
        print(numero_1 * numero_2)

# Divisão
    elif operacao == "/":
        print("{} / {} = ".format(numero_1, numero_2))
        print(numero_1 / numero_2)
        

    else:
        print("Você não digitou um operador válido, execute o programa novamente.")

# Adicionando a função again() à função calculate()
    again()

def again():
    calc_again = input("""
Deseja calcular novamente?
Digite S para SIM ou N para NÃO.
""")

    if calc_again.upper() == "S":
        calculate()
    elif calc_again.upper() == "N":
        print("Até logo!")
    else:
        again()
        
# Fechando função Welcome
welcome()
# Fechando a função calculate()
calculate()
