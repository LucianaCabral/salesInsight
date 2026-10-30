from clean_data import remover_espacos_colunas, tratar_datas, ajustar_tipos, gerar_relatorio_tratamento, tratar_dados
from customer_segmentation import segmentar_clientes,exibir_segmentacao
from transform_data import criar_colunas_derivadas
from metrics import calcular_metricas, exibir_metricas
import pandas as pd  
import numpy as np
import random
from visualizations import gerar_graficos
from export_results import exportar_resultados

from datetime import datetime, timedelta
 
def gerar_dataset_vendas(n_registros=200, seed=42):
    """Gera um dataset sintetico de vendas com dados sujos."""
    random.seed(seed)
    np.random.seed(seed)

    produtos = ["Notebook", "Smartphone", "Tablet", "Monitor",
                "Teclado", "Mouse", "Headset"]
    categorias = {"Notebook": "Computadores", "Smartphone": "Celulares",
                  "Tablet": "Celulares", "Monitor": "Computadores",
                  "Teclado": "Perifericos", "Mouse": "Perifericos",
                  "Headset": "Perifericos"}
    precos = {"Notebook": 3500, "Smartphone": 2200, "Tablet": 1800,
              "Monitor": 1200, "Teclado": 250, "Mouse": 120,
              "Headset": 350}
    regioes = ["Sudeste", "Sul", "Nordeste", "Centro-Oeste", "Norte"]

    data_inicio = datetime(2025, 1, 1)
    dados = []

    for i in range(n_registros):
        produto = random.choice(produtos)
        categoria = categorias[produto]
        quantidade = random.randint(1, 10)
        preco = round(precos[produto] * random.uniform(0.85, 1.15), 2)
        data = data_inicio + timedelta(days=random.randint(0, 364))
        data_txt = data.strftime("%Y-%m-%d")
        cliente = f"Cliente_{random.randint(1, 50):03d}"
        # --- sujeira proposital para a etapa de limpeza ---
        if random.random() < 0.03:
            data_txt = "DATA INVALIDA"  # data invalida

        dados.append({
            "id_venda": i + 1,
            "data_venda": data_txt,
            "cliente": cliente,
            "produto": produto,
            "categoria": categoria,
            "regiao": random.choice(regioes),
            "quantidade": quantidade,
            "preco_unitario": preco,
        })

    return pd.DataFrame(dados)


# Gerar e salvar o CSV bruto
df_bruto = gerar_dataset_vendas()
df_bruto.to_csv("vendas.csv", index=False)
print(f"Dataset gerado com {len(df_bruto)} registros.")
print(df_bruto.head())


def inspecionar_dados(df_bruto):
    """"
    Exibe informações estruturais do DataFrame.

    Args:
        df_bruto: DataFrame que será inspecionado.

    Returns:
        O próprio DataFrame recebido.
    """
    print("\n=== INSPECAO INICIAL DO DATASET ===")
    print(f"Shape: {df_bruto.shape}")
    print(f"\nColunas: {list(df_bruto.columns)}")
    print(f"\nTipos de dados:\n{df_bruto.dtypes}")
    print(f"\nValores nulos por coluna:\n{df_bruto.isnull().sum()}")
    print(f"\nPrimeiros registros:\n{df_bruto.head()}")
    return df_bruto

def main():
    """
    Coordena o fluxo completo de análise das vendas.

    Gera os dados, realiza a inspeção, limpeza, transformação,
    cálculo de métricas, segmentação de clientes e visualização.

    Returns:
        Tupla contendo o DataFrame transformado, as métricas
        calculadas e o DataFrame de clientes segmentados.
    """
    # 1. Geração do dataset bruto
    df_bruto = gerar_dataset_vendas()
    df_bruto.to_csv("vendas.csv", index=False)

    print(f"Dataset gerado com {len(df_bruto)} registros.")
    print(df_bruto.head())
    inspecionar_dados(df_bruto)

    # 2. Inspeção inicial
    inspecionar_dados(df_bruto)

    # 3. Limpeza dos dados
    df_limpo, relatorio = tratar_dados(df_bruto)

    print("\n=== DATASET LIMPO ===")
    print(df_limpo.head())
    print(f"\nDimensões finais: {df_limpo.shape}")
    print(f"\nTipos de dados:\n{df_limpo.dtypes}")

    # 4. Criação das colunas derivadas
    df_vendas = criar_colunas_derivadas(df_limpo)

    print("\n=== DATASET COM COLUNAS DERIVADAS ===")
    print(df_vendas.head())

    print(df_vendas[
        [
            "receita_total",
            "mes",
            "mes_nome",
            "trimestre",
            "ano",
            "faixa_receita_item"
        ]
    ].head())

    print(f"\nColunas disponíveis: {list(df_vendas.columns)}")

    # 5. Cálculo e exibição das métricas
    metricas = calcular_metricas(df_vendas)
    exibir_metricas(metricas)

    # 6. Segmentação e exibição dos clientes
    clientes_segmentados = segmentar_clientes(df_vendas)
    exibir_segmentacao(clientes_segmentados)

    # 7. Cálculo das estatísticas gerais
    estatisticas = {
    "receita_total": df_vendas["receita_total"].sum(),
    "quantidade_vendida": df_vendas["quantidade"].sum(),
    "total_vendas": len(df_vendas),
    "ticket_medio": df_vendas["receita_total"].mean()
    }

    # 8. Geração dos gráficos
    gerar_graficos(df_vendas)

    # 9. Exportação dos resultados
    exportar_resultados(
    metricas,
    clientes_segmentados,
    estatisticas
    )
    print("\n[CONCLUÍDO] Fluxo finalizado com sucesso.")
    
    return df_vendas, metricas, clientes_segmentados  

if __name__ == "__main__":
    main()
