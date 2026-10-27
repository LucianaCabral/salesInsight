import pandas as pd

def remover_espacos_colunas(df_bruto):
    df_limpo =df_bruto.copy()   
    colunas_texto = df_limpo.select_dtypes(
        include=["object", "string"]
    ).columns
    
    for coluna in colunas_texto:
            df_limpo[coluna] = df_limpo[coluna].str.strip()
    return df_limpo

def tratar_datas(df_bruto):
    df_limpo = df_bruto.copy()

    df_limpo["data_venda"] = pd.to_datetime(
        df_limpo["data_venda"],
        errors="coerce"
    )

    df_limpo = df_limpo.dropna(subset=["data_venda"])

    return df_limpo

def ajustar_tipos(df_bruto):
    df_limpo = df_bruto.copy()

    df_limpo["quantidade"] = df_limpo["quantidade"].astype(int)
    df_limpo["preco_unitario"] = df_limpo["preco_unitario"].astype(float)

    return df_limpo