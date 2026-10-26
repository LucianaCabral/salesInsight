import pandas as pd

def remover_espacos_colunas(df_bruto):
    df_limpo =df_bruto.copy()   
    colunas_texto = df_limpo.select_dtypes(
        include=["object", "string"]
    ).columns
    
    for coluna in colunas_texto:
            df_limpo[coluna] = df_limpo[coluna].str.strip()
    return df_limpo
