import json
import os

def exportar_resultados(metricas, clientes, estatisticas):
    """
    Exporta métricas e segmentação em CSV e estatísticas em JSON.
    Em seguida, lê o JSON gravado e exibe seu conteúdo.

    Args:
        metricas: Dicionário de DataFrames com as métricas calculadas.
        clientes: DataFrame com a segmentação dos clientes.
        estatisticas: Dicionário com as estatísticas gerais.

    Returns:
        Dicionário com as estatísticas recuperadas do arquivo JSON.
    """
    os.makedirs("outputs", exist_ok=True)

    # Exportação das métricas mensais para CSV
    metricas["por_mes"].to_csv(
        "outputs/metricas_por_mes.csv",
        index=False,
        encoding="utf-8-sig"
    )

    # Exportação da segmentação de clientes para CSV
    clientes.to_csv(
        "outputs/segmentacao_clientes.csv",
        index=False,
        encoding="utf-8-sig"
    )

    # Preparação das estatísticas para serialização em JSON
    serializavel = {
        chave: round(float(valor), 2)
        for chave, valor in estatisticas.items()
    }

    caminho = "outputs/estatisticas_gerais.json"

    # Escrita do arquivo JSON
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(
            serializavel,
            arquivo,
            indent=4,
            ensure_ascii=False
        )

    # Leitura do JSON para conferir a gravação
    with open(caminho, "r", encoding="utf-8") as arquivo:
        conferencia = json.load(arquivo)

    print("\n=== ESTATÍSTICAS RECUPERADAS DO JSON ===")
    print(conferencia)

    return conferencia