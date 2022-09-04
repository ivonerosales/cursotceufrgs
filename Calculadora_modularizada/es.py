""" Programa_calculadora_modularizada
Descrição: Este módulo mostra o resultado da operação para o usuário.
Autora: Ivone Rosales
Versão: 0.0.4
Data: 03/09/2022
"""

def entrada() -> list:
    """
    Esta função entra com os dois números digitados pelo usuário.
    """
    num_1 = float(input("\nDigite o primeiro número: "))
    num_2 = float(input("\nDigite o segundo número: ")) 
    return [num_1, num_2]


def saida(valor: float):
    """
    Esta função mostra na tela o resultado da operação.
    """
    print(f"\nO resultado da operação é {valor}.")

    



        

    



