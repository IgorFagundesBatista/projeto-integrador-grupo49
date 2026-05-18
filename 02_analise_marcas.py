import pandas as pd
import os

# 1. Carregar os dados
caminho_do_arquivo = 'data/processed/base_limpa.csv'
df = pd.read_csv(caminho_do_arquivo)

print("="*50)
print("EXECUTANDO: Análise de Performance de Marcas")
print("="*50)

# 2. Conta: Qual marca gera mais receita total (Faturamento Geral)?
faturamento_marca = df.groupby('brand')['revenue_usd'].sum().reset_index()
faturamento_marca = faturamento_marca.sort_values(by='revenue_usd', ascending=False)

# 3. Conta: Qual marca vende mais unidades em cada país?
marca_pais = df.groupby(['country', 'brand'])['units_sold'].sum().reset_index()
marca_pais = marca_pais.sort_values(by=['country', 'units_sold'], ascending=[True, False])

# ========================================================
# SALVANDO OS RESULTADOS EM EXCEL (Como você gosta!)
# ========================================================
# Primeiro, garantimos que a pasta para salvar os resultados existe
os.makedirs('data/processed', exist_ok=True)

# Salvamos o faturamento por marca em uma planilha
faturamento_marca.to_excel('data/processed/faturamento_por_marca.xlsx', index=False)

# Salvamos as marcas mais vendidas por país em outra planilha
marca_pais.to_excel('data/processed/marcas_por_pais.xlsx', index=False)

print("\n🎉 Sucesso! As análises foram calculadas e salvas na pasta 'data/processed/'")
print("- faturamento_por_marca.xlsx")
print("- marcas_por_pais.xlsx")