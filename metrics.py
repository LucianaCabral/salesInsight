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