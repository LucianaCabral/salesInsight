# sales_insight
# :dart: Desafio: Análise e Visualização de Dados de Vendas

## Pergunta-Chave do Negócio
- **Como as vendas se comportam ao longo do tempo?** (por mês e por trimestre)
- **Quais produtos e categorias geram mais receita?**
- **Quais regiões têm melhor desempenho?**
- **Quais clientes são mais valiosos?** (segmentação simples por faixa de gasto)
- **Existe relação entre a quantidade vendida e a receita gerada por transação?**

---

# :rocket:  Mini-Projeto em Python: SalesInsight PY
> **Análise e Visualização de Dados de Vendas**

##  Objetivo
Organizar um fluxo de análise de dados que carregue, transforme, agregue e visualize um dataset de vendas, gerando insights relevantes e exportando os resultados.

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