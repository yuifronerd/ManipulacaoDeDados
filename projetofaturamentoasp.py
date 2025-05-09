import pandas as pd

dados_texto1 = pd.read_excel("dados1.xlsx")
dados_texto2 = pd.read_excel("dados2.xlsx")

dados_completos = pd.concat([dados_texto1, dados_texto2], ignore_index=True)

dados_completos.to_excel("dados_completos.xlsx", index=False, engine="openpyxl")

print("Dados dos dois PDFs combinados em dados_completos.xlsx")
