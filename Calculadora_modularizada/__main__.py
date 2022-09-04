"""Programa_calculadora_modularizada
Descrição: Este programa calcula valores de dois números usando as 4 operações aritméticas básicas. 
Autora: Ivone Rosales
Data: 03/09/2022
Versão: 0.0.4
"""

# Função de boas-vindas

def welcome():
    print("""
Bem-vindo(a) à Calculadora!
""")

welcome()

# Importação de módulo

import aritmetico
import es

# Definição das operações

def main():
    lista_numeros = es.entrada()
    operacao = input("""Qual operação você deseja?  Digite:
             + para adição,
             - para subtração,
             * para multiplicação ou
             / para divisão\n""")
    
    if operacao == "+":
        valor = aritmetico.adicao(lista_numeros[0], lista_numeros[1])
    elif operacao == "-":
        valor = aritmetico.subtracao(lista_numeros[0], lista_numeros[1])
    elif operacao == "*":
        valor = aritmetico.multiplicacao(lista_numeros[0], lista_numeros[1])
    elif operacao == "/":
        valor = aritmetico.divisao(lista_numeros[0], lista_numeros[1])
    else:
        valor = "impossível de ser calculada nesta calculadora."
    es.saida(valor)

if __name__ == "__main__":
    main()

