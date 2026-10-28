import pandas as pd

def calcular_receita_total(df):
    df = df.copy()
    df["receita_total"] = df["quantidade"] * df["preco_unitario"]
    return df

def extrair_dados_temporais(df):
    df = df.copy()

    df["mes"] = df["data_venda"].dt.month

    meses = {
        1: "Janeiro", 2: "Fevereiro", 3: "Março",
        4: "Abril", 5: "Maio", 6: "Junho",
        7: "Julho", 8: "Agosto", 9: "Setembro",
        10: "Outubro", 11: "Novembro", 12: "Dezembro"
    }

    df["mes_nome"] = df["mes"].map(meses)
    df["trimestre"] = "Q" + df["data_venda"].dt.quarter.astype(str)
    df["ano"] = df["data_venda"].dt.year

    return df

