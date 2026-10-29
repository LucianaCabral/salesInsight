from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
  
PALETA = {
    "azul": "#264653",
    "verde": "#2A9D8F",
    "laranja": "#E76F51",
    "amarelo": "#E9C46A",
    "roxo": "#8064A2",
}

CORES_CATEGORIAS = [
    PALETA["azul"],
    PALETA["verde"],
    PALETA["laranja"],
    PALETA["roxo"],
    PALETA["amarelo"],
]

def _preparar_dados(df):
    """Valida e prepara os dados utilizados nos gráficos."""
    colunas = {
        "data_venda",
        "produto",
        "categoria",
        "quantidade",
        "receita_total",
        "regiao",
    }
    ausentes = colunas.difference(df.columns)
    if ausentes:
        raise ValueError(
            f"Colunas ausentes no DataFrame: {sorted(ausentes)}"
        )
    dados = df.copy()
    dados["data_venda"] = pd.to_datetime(
        dados["data_venda"], errors="coerce"
    )
    dados = dados.dropna(subset=["data_venda"])
    return dados

def _desenhar_receita_mensal(ax, df):
    """Desenha a receita total agrupada por mês."""
    mensal = (
        df.assign(
            mes=df["data_venda"].dt.to_period("M"))
        .groupby("mes")["receita_total"]
        .sum()
    )
    ax.plot(
        mensal.index.astype(str),
        mensal.values,
        color=PALETA["verde"],
        marker="o",
        linewidth=2,
        label="Receita mensal",
    )
    ax.set_title("Receita total por mês")
    ax.set_xlabel("Mês")
    ax.set_ylabel("Receita (R$)")
    ax.tick_params(axis="x", rotation=45)
    ax.legend()

def _desenhar_top_produtos(ax, df):
    """Desenha os cinco produtos com maior receita."""
    top = (
        df.groupby("produto")["receita_total"]
        .sum()
        .nlargest(5)
        .sort_values()
    )
    ax.barh(
        top.index,
        top.values,
        color=PALETA["azul"],
        label="Receita por produto",
    )
    ax.set_title("Top 5 produtos por receita")
    ax.set_xlabel("Receita (R$)")
    ax.set_ylabel("Produto")
    ax.legend()

def _desenhar_dispersao(ax, df):
    """Relaciona quantidade e receita por categoria."""
    categorias = sorted(df["categoria"].dropna().unique())

    for indice, categoria in enumerate(categorias):
        grupo = df[df["categoria"] == categoria]

        ax.scatter(
            grupo["quantidade"],
            grupo["receita_total"],
            color=CORES_CATEGORIAS[
                indice % len(CORES_CATEGORIAS)
            ],
            label=str(categoria),
            alpha=0.75,
            edgecolors="white",
            linewidths=0.4,
        )

    ax.set_title("Quantidade versus receita")
    ax.set_xlabel("Quantidade vendida")
    ax.set_ylabel("Receita (R$)")
    ax.legend(title="Categoria")

def _desenhar_receita_regional(ax, df):
    """Desenha a receita total agrupada por região."""
    regional = (
        df.groupby("regiao")["receita_total"]
        .sum()
        .sort_values()
    )

    ax.barh(
        regional.index.astype(str),
        regional.values,
        color=PALETA["laranja"],
        label="Receita por região",
    )

    ax.set_title("Receita total por região")
    ax.set_xlabel("Receita (R$)")
    ax.set_ylabel("Região")
    ax.legend()

def gerar_graficos(df, pasta_saida="figures"):
    """Gera e exporta as quatro figuras da RF07."""
    dados = _preparar_dados(df)
    pasta = Path(pasta_saida)
    pasta.mkdir(parents=True, exist_ok=True)

    # Figura 1: receita por mês
    plt.figure(figsize=(10, 5))
    fig, ax = plt.subplots(figsize=(10, 5))
    _desenhar_receita_mensal(ax, dados)
    plt.tight_layout()
    plt.savefig(
        pasta / "receita_por_mes.png",
        dpi=150,
        bbox_inches="tight",
    )
    plt.close(fig)

    # Figura 2: top produtos
    fig, ax = plt.subplots(figsize=(10, 6))
    _desenhar_top_produtos(ax, dados)
    plt.tight_layout()
    plt.savefig(
        pasta / "top_produtos.png",
        dpi=150,
        bbox_inches="tight",
    )
    plt.close(fig)

    # Figura 3: dispersão
    fig, ax = plt.subplots(figsize=(9, 6))
    _desenhar_dispersao(ax, dados)
    plt.tight_layout()
    plt.savefig(
        pasta / "quantidade_vs_receita.png",
        dpi=150,
        bbox_inches="tight",
    )
    plt.close(fig)

    # Figura 4: painel 2 x 2
    fig, eixos = plt.subplots(2, 2, figsize=(15, 10))

    _desenhar_receita_mensal(eixos[0, 0], dados)
    _desenhar_top_produtos(eixos[0, 1], dados)
    _desenhar_dispersao(eixos[1, 0], dados)
    _desenhar_receita_regional(eixos[1, 1], dados)

    fig.suptitle("Painel de análise de vendas", fontsize=16)
    plt.tight_layout()
    plt.savefig(
        pasta / "painel_resumo.png",
        dpi=150,
        bbox_inches="tight",
    )
    plt.close(fig)

    print(f"Quatro figuras salvas em: {pasta.resolve()}")
