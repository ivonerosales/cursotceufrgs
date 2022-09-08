"""Programa soma
Descrição: 
Este programa soma dois números dados pelo usuário.
autor: Ivone Rosales
Versão: 0.0.06
Data: 11/08/2022
"""

# Entrada

lista_numeros = [] # cria uma lista de números vazia # listas começam do zero.
i = 0  # contador, que é uma variável para contar quantos números foram digitados.

while i < 2:
    lista_numeros.append(int(input ("Entre com o primeiro numero que você quer somar.")))
    i+=1


# Processamento de dados

soma = lista_numeros [0] + lista_numeros [1]

# Saída de dados

print(f"O resultado da soma do {lista_numeros [0]} com o {lista_numeros [1]} é igual a {soma}.")



