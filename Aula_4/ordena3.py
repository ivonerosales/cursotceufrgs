"""
Programa retira_repeticao
Requisitos: Dada uma lista de dados do usuário, retire os dados.
Coloque na tela a lista sem repetição.  repetidos
Autor: Ivone Rosales
Data: 18.08.2022
Versão: 0.0.1
"""

#entrada

i = 0
j = 0
k = 0
lista = []

while i < 3:
    numero = float(input("digite um número: "))
    lista.append(numero)
    i+=1


#processamento de dados

while j < 3:
    while k < 3:
        if lista[k] > lista[k +1]:
            lista[k] = lista [k+1]
        k+=1
    j+=1

# Saída de dados
print(lista)
