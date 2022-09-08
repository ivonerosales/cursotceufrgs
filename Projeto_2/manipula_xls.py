
"""
Módulo manipula_xls
Descrição: Este módulo oferece funções para manipular arquivos no formato xls.
Autora: Ivone Rosales
Data: 08.09.2022
Versão: 0.0.1
"""

# Importação de pacotes

from openpyxl import workbook


def cria_xls()-> workbook:
    '''Esta função cria uma pasta de trabaho MS-Excel.'''
    pasta = workbook()
    return pasta

def cria_planilha(nome_planilha: str, pasta: workbook)-> None:
    pasta.active
    pasta.create_sheet(nome_planilha)
