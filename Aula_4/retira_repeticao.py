"""
Programa retira_repeticao
Requisitos: Dada uma lista de dados do usuário, retire os dados repetidos.
Coloque na tela a lista sem repetição.  
Autor: Ivone Rosales
Data: 18.08.2022
Versão: 0.0.1
"""
# Entrada
# Leitura de lista de dados do usuário

lista = []

while True:
    elemento = input("\nDigite um elemento  da sua lista. Ou, digite X para encerrar:  ")
    if elemento == elemento.upper()== "X":
        break
    lista.append(elemento)
    
    


# Processamento retire todos os dados repetidos

for i in list(range(len(lista) + 1)):
            for j in list(range(len(lista) + 1)):
                if lista[j] == lista[j+1]:
                            del lista[j+1]
                              


# Saída
# Colocar na tela a lista sem repetição.

print (lista)

