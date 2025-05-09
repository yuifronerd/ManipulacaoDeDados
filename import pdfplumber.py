import pdfplumber

pdf_texto = ''

with pdfplumber.open(pdf_texto) as pdf:
    texto_extraido = ""
    for page in pdf.pages:
        texto_extraido += page.extract_text()

with open("texto_extraido.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(texto_extraido)

print("Texto extraído e salvo em texto_extraido.txt")

dados_tabelados = pd.read_csv("tabela_extraida.csv")
dados_texto = pd.read_csv("dados_processados.csv")

dados_completos = pd.concat([dados_tabelados, dados_texto], ignore_index=True)

dados_completos.to_csv("dados_completos.csv", index=False)

print("Dados dos dois PDFs combinados em dados_completos.csv")

import pandas as pd

dados_texto1 = pd.read_excel("nomearquivo1.xlsx")
dados_texto2 = pd.read_excel("nomearquivo2.xlsx")

dados_completos = pd.concat([dados_texto1, dados_texto2], ignore_index=True)

dados_completos.to_excel("nomedoarquivoqueestaosdoisjuntos.xlsx", index=False, engine="openpyxl")

print("Dados dos dois PDFs combinados em dados_completos.xlsx")