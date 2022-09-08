
"""
Programa Cria_planilhas
Descrição: Este módulo principal para manipular arquivos no formato xls.
Autora: Ivone Rosales
Data: 08.09.2022
Versão: 0.0.1
"""

# Importação de pacotes

## Primeiro importe o que vier da biblioteca padrão

import random

## Depois importe o que vier de pacotes de terceiros

from openpyxl import workbook

## Por fim, importe os pacotes que você desenvolveu

import manipula_xls


def main():
    lista_planilhas = ['receitas','despesas', 'resultado']
    pasta = manipula_xls.cria_xls()
    pasta.active
    for planilha in lista_planilhas:
        manipula_xls.cria_planilha(planilha,pasta)
    pasta.save("orcamento.xls")
    

if __name__== "__main__":
    main()
