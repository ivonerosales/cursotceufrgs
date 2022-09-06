import shutil
import os


def cria_dir(nome: str):
    if os.path.exists (nome) == False:
        os.mkdir (nome)


#move o arquivo para o diretório desejado

#def move_arquivo (arquivos: list):


import shutil
import os

def move_arquivo (arquivos: list):
    for arquivo in arquivos:
        if ".xls" in arquivo:
            shutil.move(arquivo, f"./planilhas/{arquivo}")
        elif ".doc" in arquivo:
            shutil.move(arquivo, f"./documentos/{arquivo}")
        elif ".docx" in arquivo:
            shutil.move(arquivo, f"./documentos/{arquivo}")
