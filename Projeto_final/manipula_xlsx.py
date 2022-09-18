"""
Programa Projeto_final
Descrição: Este módulo oferece funções para manipular dados no formato xls.
Autora: Ivone Rosales
Data: 17.09.2022
Versão: 0.0.7
"""


# Importando os pacotes

import requests
import pandas as pd


from openpyxl import Workbook,load_workbook


# Lendo a página de Dados TCE
def page_reader(endereco):
    dados = requests.get (endereco)
    return dados


# Gravando o arquivo com as informações da variável:
def save(dados):
    with open('balancete.csv', 'wb') as arquivo:
           for texto in dados.iter_content():
            arquivo.write(texto)
            arquivo.close()


#Usando o Pandas e Openpyxl para transformar em .xlsx
def manipula_xlsx(dados):
    balancete = pd.read_csv("balancete.csv", index_col=None)
    balancete.to_excel("balancete.xlsx", sheet_name="Consolidado_despesas_2022", index = False)
    novo_balancete = load_workbook(filename = 'balancete.xlsx')
    novo_balancete.save("novo_balancete.xlsx")

    
