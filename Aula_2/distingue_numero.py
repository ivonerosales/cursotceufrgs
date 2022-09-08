# Programação Estruturada
"""
Programa distingue_numero

Requisitos: 
Este programa deve imprimir na tela uma frase, dizendo se o número digitado pelo usuário é maior que 10 ou menor ou menor ou igual a 10.

Autor: Ivone Rosales
Versão 0.0.1
Data: 11/08/2022
"""

#entrada

frase = "Este número não é maior que 10."

# usuário digita dados

numero = float (input("\nDigite um número: "))


# processamento de dados
#Estrutura de controle de fluxo de execução SELEÇÃO

# descobrir se o número é maior que 10, igual a 10 ou menor que 10.

if numero > 10:
    frase = "Este número é maior que 10"
elif numero == 10:
    frase = "Este número é igual a 10."
else:
    frase = " Este número é menor que 10."

#saída de dados


#programa imprime na tela

print (frase)













