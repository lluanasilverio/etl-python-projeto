import pandas as pd

def extrair_dados(caminho):
    df = pd.read_csv(caminho)
    return df