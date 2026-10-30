import pandas as pd

def calcular_receita_total(df):
    """
    Calcula a receita total de cada venda.

    A receita é obtida multiplicando a quantidade vendida
    pelo preço unitário.

    Args:
        df: DataFrame com as colunas quantidade e preco_unitario.

    Returns:
        DataFrame com a coluna receita_total adicionada.
    """

    df = df.copy()
    df["receita_total"] = df["quantidade"] * df["preco_unitario"]
    return df

def extrair_dados_temporais(df):
    
    """
    Extrai informações temporais a partir da data da venda.

    Cria as colunas mes, mes_nome, trimestre e ano.

    Args:
        df: DataFrame com a coluna data_venda no formato datetime.

    Returns:
        DataFrame com as colunas temporais adicionadas.
    """

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

def processar_coluna(df, coluna, funcao_transformacao, nome_saida=None):
    """
    Aplica uma função aos valores de uma coluna do DataFrame.
    Args:
        df: DataFrame de entrada.
        coluna: Nome da coluna a ser processada.
        funcao_transformacao: Função aplicada a cada valor.
        nome_saida: Nome da coluna resultante.
    Returns:
        DataFrame com a nova coluna.
    """

    df = df.copy()
    nome_saida = nome_saida or f"{coluna}_transformado"
    df[nome_saida] = df[coluna].apply(funcao_transformacao)
    return df

def classificar_receita_item(df):
    """
    Classifica cada venda conforme sua faixa de receita.

    As classificações são:
    - Baixo Valor: receita inferior a 500.
    - Medio Valor: receita entre 500 e 4.999,99.
    - Alto Valor: receita igual ou superior a 5.000.

    Args:
        df: DataFrame com a coluna receita_total.

    Returns:
        DataFrame com a coluna faixa_receita_item adicionada.
    """

    def classificar(valor):
        if valor < 500:
            return "Baixo Valor"
        elif valor < 5000:
            return "Medio Valor"
        else:
            return "Alto Valor"
    return processar_coluna(
        df,
        "receita_total",
        classificar,
        "faixa_receita_item"
    )

def criar_colunas_derivadas(df_limpo):
    """
    Executa o fluxo de criação das colunas derivadas.

    Calcula a receita total, extrai os dados temporais
    e classifica as vendas por faixa de receita.

    Args:
        df_limpo: DataFrame previamente tratado, contendo as
            colunas necessárias para as transformações.

    Returns:
        DataFrame com as colunas derivadas adicionadas.
    """

    df = calcular_receita_total(df_limpo)
    df = extrair_dados_temporais(df)
    df = classificar_receita_item(df)

    return df
