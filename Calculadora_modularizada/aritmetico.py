"""Modulo aritmetico
Descrição: Este módulo fornece as 4 operações aritméticas básicas.
Autora: Ivone Rosales
Data: 02/09/2022
Versão: 0.0.4
"""


def adicao(x: float, y: float) -> float:
    """
    Esta função recebe dois números e retorna a soma.
    """
    return x + y


def subtracao(x: float, y: float) -> float:
   """
   Esta função recebe dois números e retorna a diferença.
   """
   return x - y

def multiplicacao(x: float, y: float) -> float:
    """
    Esta função recebe dois números e retorna o produto
    """
    return x*y


def divisao(x: float, y: float) -> float:
    """
    Esta função recebe dois números e retorna a divisão do primeiro pelo segundo, número este que deve é ser diferente de zero.
    """
    if y == 0:
        return "não se pode dividir por zero."
    return x/y
