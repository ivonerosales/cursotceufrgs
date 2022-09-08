"""
Programa retira_repeticao
Requisitos: Dada uma lista de dados do usuário, retire os dados repetidos.
Coloque na tela a lista sem repetição.  
Autor: Ivone Rosales
Data: 18.08.2022
Versão: 0.0.2
"""
#entrada
#leitura de lista de dados do usuário

lista = []
resultado_lista = []

while True:
    elemento = input("\nDigite um elemento  da sua lista. Ou, digite X para encerrar:  ")
    if elemento == elemento.upper()== "X":
        break
    lista.append(elemento)


for elementos in lista:
    if elementos not in resultado_lista:
        resultado_lista.append(elementos)

# Saída de dados
print(f"\n A lista sem numeros repetidos é: {resultado_lista}")
