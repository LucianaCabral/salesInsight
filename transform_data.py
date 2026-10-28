import pandas as pd

def calcular_receita_total(df):
    df = df.copy()
    df["receita_total"] = df["quantidade"] * df["preco_unitario"]
    return df
