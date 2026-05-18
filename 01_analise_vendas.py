# ==========================================
# 1. IMPORTAÇÃO DAS BIBLIOTECAS
# ==========================================
import pandas as pd
# ==========================================
# 2. CARREGAMENTO DOS DADOS
# ==========================================
# Indicamos o caminho relativo de onde o arquivo CSV está guardado
caminho_do_arquivo = 'data/processed/base_limpa.csv'
# Lemos o arquivo CSV e salvamos dentro de uma variável chamada 'df' (DataFrame)
df = pd.read_csv(caminho_do_arquivo)

# ==========================================
# 3. PRIMEIRA INSPEÇÃO VISUAL
# ==========================================
print("--- Primeiras 5 linhas do DataFrame ---")
# O método .head() exibe, por padrão, as 5 primeiras linhas da tabela
print(df.head())

print("\n--- Informações Estruturais dos Dados ---")
# O método .info() exibe o nome das colunas, tipos de dados e se há valores nulos
df.info()

# ==========================================
# 4. ANÁLISE 1: VOLUME DE VENDAS POR CATEGORIA E PAÍS
# ==========================================
print("\n--- Volume de Vendas por Categoria e País ---")

# Agrupamos por País e Categoria, e depois somamos as Unidades Vendidas
vendas_por_pais_categoria = df.groupby(['country', 'category'])['units_sold'].sum().reset_index()

# Ordenamos o resultado para ver os maiores volumes primeiro
vendas_por_pais_categoria = vendas_por_pais_categoria.sort_values(by=['country', 'units_sold'], ascending=[True, False])

# Exibe o resultado na tela
print(vendas_por_pais_categoria)

