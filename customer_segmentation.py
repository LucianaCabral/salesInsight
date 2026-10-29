def segmentar_clientes(df):
    """Agrupa as vendas por cliente, calcula o total gasto
    e classifica os clientes em Bronze, Prata ou Ouro.

    Retorna um DataFrame com:cliente, total_gasto e segmento.
    """
    
    clientes = (
        df.groupby("cliente")
        .agg(total_gasto=("receita_total", "sum"))
        .reset_index()
    )

    clientes["segmento"] = clientes["total_gasto"].apply(
        lambda total: (
            "Bronze" if total < 5000
            else "Prata" if total <= 15000
            else "Ouro"
        )
    )

    clientes = clientes.sort_values(
        "total_gasto", ascending=False
    ).reset_index(drop=True)

    return clientes