import os
from tkinter.filedialog import askdirectory

# abre o popup de selecionar uma pasta no windows
caminho = askdirectory(title="Selecione uma pasta")

# mostra todos os arquivos que estao dentro do Caminho
lista_arquivos = os.listdir(caminho)

locais = {
    "imagens": [".png", ".jpg", ".gif", ".webp", ".jpeg"],
    "audio": [".mp3", ".wav", ".m4a"],
    "video": [".mp4", ".wmv", ".mov"],
    "documentos": [".pdf", ".csv", ".txt", ".xlsx", ".docx", ".TXT"],
    "arquivos_zip": [".zip"],
    "aplicativos": [".exe"],
}

for arquivo in lista_arquivos:
    # 01. Arquivo.pdf
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):  # se nao existe a pasta
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")
