"""
Programa tamanho_lista

Requisitos: Este programa calcula o tamanho de uma lista Python dada pelo usuário e o coloca na tela.
Autor: Ivone Rosales
Data 16/08/2022
Versão: 0.0.2
"""

# Entrada
# entrada do usuário pelo teclado

lista = []
while True:
    elemento = input ("\nDigite um elemento para a sua lista. Quando encerrar, digite X e pressione ENTER.  ")
    if elemento.upper ()== "X":
        break
    lista.append(elemento)

#Processamento de dados
#calcula o tamanho de uma lista Python

tamanho_lista = len(lista)


# Saída de dados
# colocar o tamanho da lista na tela.

print (f"O tamanho da lista digitada é {tamanho_lista}.")

print (f"A lista digitada foi {lista} e seu tamanho é  {tamanho_lista}.")
