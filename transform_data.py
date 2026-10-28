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

def classificar_receita_item(df):
    df = df.copy()

    condicoes = [
        df["receita_total"] < 500,
        (df["receita_total"] >= 500) & (df["receita_total"] < 5000),
        df["receita_total"] >= 5000
    ]

    faixas = ["Baixo Valor", "Medio Valor", "Alto Valor"]

    df["faixa_receita_item"] = "Nao Classificado"

    for condicao, faixa in zip(condicoes, faixas):
        df.loc[condicao, "faixa_receita_item"] = faixa

    return df

def criar_colunas_derivadas(df_limpo):
    df = calcular_receita_total(df_limpo)
    df = extrair_dados_temporais(df)
    df = classificar_receita_item(df)

    return df
