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

    datas_convertidas = pd.to_datetime(
        df_limpo["data_venda"],
        errors="coerce"
    )
    datas_invalidas = int(
        datas_convertidas.isna().sum()
    )
    datas_validas = int(
        datas_convertidas.notna().sum()
    )
    df_limpo["data_venda"] = datas_convertidas
    df_limpo = df_limpo.dropna(
        subset=["data_venda"]
    )
    return (df_limpo,datas_validas,datas_invalidas)

def ajustar_tipos(df_bruto):
    df_limpo = df_bruto.copy()
    df_limpo["quantidade"] = df_limpo["quantidade"].astype(int)
    df_limpo["preco_unitario"] = df_limpo["preco_unitario"].astype(float)
    return df_limpo

def gerar_relatorio_tratamento(df_bruto,
    df_limpo,
    datas_validas,
    datas_invalidas,
    quantidade_convertida,
    preco_convertido
    ):
   
    registros_iniciais = len(df_bruto)  
    registros_finais = len(df_limpo)
    registros_removidos = registros_iniciais - registros_finais
    relatorio = {
        "Registros iniciais": registros_iniciais,
        "Datas convertidas": datas_validas,
        "Datas inválidas removidas": datas_invalidas,
        "Registros removidos": registros_removidos,
        "Registros finais": registros_finais,
        "Registros com quantidade convertida": quantidade_convertida,
        "Registros com preço convertido": preco_convertido,
    }
    
    print("\n=== RELATÓRIO DE LIMPEZA ===")
    
    for descricao, quantidade in relatorio.items():
        print(f"{descricao}: {quantidade}")
    return relatorio

def tratar_dados(df_bruto):
    df_limpo = remover_espacos_colunas(df_bruto)
    df_limpo, datas_validas, datas_invalidas = tratar_datas(df_limpo)
    quantidade_convertida = int(df_limpo["quantidade"].notna().sum())
    preco_convertido = int(df_limpo["preco_unitario"].notna().sum())
    df_limpo = ajustar_tipos(df_limpo)
    relatorio = gerar_relatorio_tratamento(
        df_bruto,
        df_limpo,
        datas_validas,
        datas_invalidas,
        quantidade_convertida,
        preco_convertido,
    )
    return df_limpo, relatorio