import pandas as pd

# Carregar os dados dos dois arquivos Excel
dados_texto1 = pd.read_excel("dados1.xlsx")
dados_texto2 = pd.read_excel("dados2.xlsx")

# Concatenar os DataFrames
dados_completos = pd.concat([dados_texto1, dados_texto2], ignore_index=True)

# Salvar no formato Excel
dados_completos.to_excel("dados_completos.xlsx", index=False, engine="openpyxl")

print("Dados dos dois PDFs combinados em dados_completos.xlsx")