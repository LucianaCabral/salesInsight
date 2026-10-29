import pandas as pd

def calcular_metricas_por_mes(df):
    """
    Calcula as métricas de vendas agrupadas por mês.
    Args:
        df: DataFrame contendo mes, receita_total, quantidade e produto.
    Returns:
        DataFrame com receita total, quantidade e número de vendas por mês.
    """
    
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
   def calcular_top_produtos(df):
    """
    Identifica os cinco produtos com maior receita total.
    Args:
        df: DataFrame com os dados das vendas.
    Returns:
        DataFrame com os cinco produtos mais rentáveis.
    """
    metricas = (
        df.groupby("produto")
        .agg(receita_total=("receita_total", "sum"))
        .sort_values("receita_total", ascending=False)
        .head(5)
        .reset_index()
    )

    return metricas

def calcular_metricas_por_categoria(df):
    """
    Calcula a receita total agrupada por categoria.
    Args:
        df: DataFrame contendo categoria e receita_total.
    Returns:
        DataFrame com a receita total de cada categoria.
    """
    metricas = (
        df.groupby("categoria")
        .agg(receita_total=("receita_total", "sum"))
        .reset_index()
    )
    return metricas

def calcular_metricas_por_regiao(df):
    """
    Calcula a receita total e o ticket médio por região.
    Args:
        df: DataFrame contendo regiao e receita_total.
    Returns:
        DataFrame com receita total e média da receita por região.
    """
    metricas = (
        df.groupby("regiao")
        .agg(receita_total=("receita_total", "sum"),
             ticket_medio=("receita_total", "mean"))
        .reset_index()
    )
    return metricas

def calcular_metricas(df):
    """
    Reúne as métricas de vendas em um dicionário.

    Args:
        df: DataFrame de vendas transformado.

    Returns:
        Dicionário com métricas por mês, produto, categoria e região.
    """
    metricas = {
        "por_mes": calcular_metricas_por_mes(df),
        "top_produtos": calcular_top_produtos(df),
        "por_categoria": calcular_metricas_por_categoria(df),
        "por_regiao": calcular_metricas_por_regiao(df)
    }
    return metricas

def exibir_metricas(metricas):
    """
    Exibe no console as métricas calculadas.
    Args:
        metricas: Dicionário retornado por calcular_metricas.
    Returns:
        None.
    """
    print("\n=== POR MÊS ===")
    print(metricas["por_mes"])

    print("\n=== TOP PRODUTOS ===")
    print(metricas["top_produtos"])

    print("\n=== POR CATEGORIA ===")
    print(metricas["por_categoria"])

    print("\n=== POR REGIÃO ===")
    print(metricas["por_regiao"])
    