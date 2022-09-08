"""
Programa acessa_lista
Requisito: Este programa acessa elementos de uma lista com os números 1,4,7.
Autor: Ivone Rosales
Versão: 0.0.5 introduz a estrutura de controle for com range
Data: 16/08/2022

"""
# Entrada de dados

lista = [1,4,7]

# Processamento de dados


# Saída de Dados 
"""
while i < 3:
    print (f"\nO elemento {i + 1} da lista é: {lista[i]}")
    i+ = 1
"""

for i in list(range(3)):
    print (f"\nO elemento {i} da lista é {lista[i]}.")

