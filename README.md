# sales_insight
# :dart: Desafio: Análise e Visualização de Dados de Vendas

# :rocket:  Mini-Projeto em Python: SalesInsight PY
> **Análise e Visualização de Dados de Vendas**

## Sobre o projeto
Analise e visualizacao de dados de vendas desenvolvida em Python. O
projeto carrega, limpa, transforma, agrega e visualiza um dataset de
vendas, gerando metricas por periodo, produto, categoria e regiao,
alem de uma segmentacao simples de clientes por faixa de gasto.
 
## O que o projeto analisa
- Receita total e volume de vendas por mes e por trimestre
- Top produtos e categorias por receita
- Desempenho por regiao
- Segmentacao de clientes por nivel de gasto (Bronze, Prata, Ouro)
- Relacao entre quantidade vendida e receita por transacao
- Exportacao de relatorios em CSV e JSON e de graficos em PNG

## Conceitos aplicados (Modulo 01 - Semanas 01 a 08)
- Logica de programacao: variaveis, tipos, operadores, condicionais
- Estruturas de dados: listas, tuplas, dicionarios e compostas
- Funcoes: parametros, retorno, lambda, ordem superior
- Leitura e escrita de arquivos CSV e JSON
- Modulo datetime e conversão de tipos (cast)
- Pandas:DataFrames, filtros, groupby, transformacoes
- Matplotlib e Seaborn: linha, barra, dispersao, subplots, export
- Git e GitHub: branches, commits e GitFlow simplificado

---

## :memo: Requisitos Funcionais 

1. **Carga e Inspeção de Dados**
   - Carregar e inspecionar os dados brutos a partir de um arquivo CSV.

2. **Engenharia de Recursos (Colunas Derivadas)**
   - Criar colunas derivadas:
     - Receita por linha (`quantidade * preco_unitario`)
     - Mês
     - Trimestre
     - Ano
     - Faixa de valor (ex: Baixo, Médio, Alto)

3. **Agregações e Métricas**
   - Calcular métricas agregadas por:
     - Mês
     - Produto
     - Categoria
     - Região

4. **Segmentação de Clientes**
   - Segmentar clientes por nível de gasto acumulado (ex: *Bronze*, *Prata*, *Ouro*).

5. **Visualização de Dados**
   - Gerar visualizações claras e informativas.
   - Criar uma figura contendo múltiplos *subplots* para resumir as análises.

6. **Exportação de Resultados**
   - Exportar um relatório resumido em formato **CSV**.
   - Exportar estatísticas gerais em formato **JSON**.
   - Exportar os gráficos gerados em formato **PNG**.

7. **Arquitetura e Organização do Código**
   - Organizar todo o fluxo em **funções reutilizáveis**.
   - Implementar ao menos **uma classe** para encapsular o pipeline de análise.

## Como executar
### Localmente com VS Code
1. Instale o Python 3.10+ e o VS Code.
2. Instale as dependencias:
   pip install pandas numpy matplotlib seaborn
3. Execute no terminal: python salesinsight.py

## Decisões técnicas

### Organização e responsabilidade dos arquivos

O projeto foi organizado em módulos separados, cada um com uma responsabilidade específica:

| Arquivo | Responsabilidade |
|---|---|
| `clean_data.py` | Limpar os dados, padronizar textos, tratar datas e ajustar tipos. |
| `transform_data.py` | Criar colunas derivadas e aplicar transformações aos dados. |
| `metrics.py` | Calcular métricas e indicadores de vendas. |
| `customer_segmentation.py` | Segmentar clientes conforme os critérios definidos no projeto. |
| `visualizations.py` | Gerar e salvar os quatro gráficos em PNG. |
| `export_results.py` | Exportar métricas, segmentação e estatísticas em arquivos CSV e JSON. |
| `salesInsight.py` | Coordenar a execução das etapas, chamando as funções dos módulos. |

### Justificativa para a separação dos arquivos

A separação foi adotada para organizar o código conforme a responsabilidade de cada etapa do processamento. Essa estrutura facilita a manutenção,as alterações,  a correção, identificação de erros e a reutilização das funções, além de evitar que todas as operações fiquem concentradas em um único arquivo.

Essa organização também permite modificar ou ampliar uma etapa do projeto sem precisar alterar diretamente as demais, favorecendo a legibilidade e a evolução do código.

### Fluxo de processamento

O processamento foi organizado respeitando a dependência entre as etapas:

1. **Geração dos dados:** criação do dataset sintético de vendas.
2. **Inspeção inicial:** verificação da estrutura, dos tipos de dados e dos valores nulos.
3. **Limpeza:** padronização dos textos, conversão das datas, remoção dos registros com datas inválidas e ajuste dos tipos.
4. **Transformação:** criação das colunas derivadas, como receita total, mês, trimestre, ano e faixa de receita por item.
5. **Métricas:** cálculo dos indicadores de vendas por mês, produto, categoria e região.
6. **Segmentação:** agrupamento e classificação dos clientes conforme o total gasto.
7. **Visualização:** geração dos gráficos a partir dos dados tratados e transformados.
8. **Exportação:** gravação dos resultados em arquivos CSV e JSON.

A limpeza é realizada antes das transformações, agregações e visualizações, garantindo que as análises sejam feitas sobre dados tratados.

## Trello: [SalesInsight PY](https://trello.com/b/YYWZeipR/salesinsight-py-analise-e-visualizacao-de-dados-de-vendas)