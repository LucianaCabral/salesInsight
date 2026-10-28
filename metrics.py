import pandas as pd

def calcular_metricas_por_mes(df):
    metricas = (
        df.groupby(["mes"])
        .agg(
            receita_total=("receita_total", "sum"),
            quantidade=("quantidade", "sum"),
            n_vendas=("produto", "count")
        )
        .reset_index()
    )
    return metricas

def calcular_top_produtos(df):
    metricas = (
        df.groupby("produto")
        .agg(receita_total=("receita_total", "sum"))
        .sort_values("receita_total", ascending=False)
        .head(5)
        .reset_index()
    )
    return metricas

def calcular_metricas_por_categoria(df):
    metricas = (
        df.groupby("categoria")
        .agg(receita_total=("receita_total", "sum"))
        .reset_index()
    )
    return metricas