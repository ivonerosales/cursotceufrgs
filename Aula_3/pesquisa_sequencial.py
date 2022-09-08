"""
Programa pesquisa_sequencial
Requisitos:Este programa procura um elemento dentro de uma lista Python.
Autor: Ivone Rosales
Data: 16/08/2022
Versão: 0.0.1

"""

# Entrada
indice = 0
L= [1, 2, 3, 7, 8, 9]

numero = int (input("\nDigite o número a procurar: "))

encontrado = False

# Processamento

while indice < len(L):
    if L[indice] == numero:
        encontrado = True
        break
    indice += 1

if encontrado:
    print (f"O valor  {numero} foi encontrado na posição {indice}.")
else:
    print(f"\nO valor  {numero} não foi encontrado.")
# Saída