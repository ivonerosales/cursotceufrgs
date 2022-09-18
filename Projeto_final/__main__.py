"""
Programa Projeto_final
Descrição: Este módulo principal para manipular dados no formato xls.
Autora: Ivone Rosales
Data: 17.09.2022
Versão: 0.0.7
"""


# Importando os pacotes

import requests
import pandas as pd

from openpyxl import Workbook,load_workbook

import manipula_xlsx


def main():
    endereco = "http://dados.tce.rs.gov.br/dados/municipal/balancete-despesa/2022.csv" 
    dados = requests.get(endereco)
    manipula_xlsx.save
    
    print("Balancetes salvos com sucesso!")
    input("Tecle Enter para SAIR.")

    
if __name__== "__main__":
    main()
 
    






