import pandas as pd
import os

print("="*50)
print("EXECUTANDO: 03_Análise de Comportamento do Consumidor")
print("="*50)

# 1. Carregar a base limpa oficial
df = pd.read_csv('data/processed/base_limpa.csv')

# ========================================================
# PERGUNTA 4: Renda vs. Preço Final Pago (Ticket por Renda)
# ========================================================
# Agrupamos por nível de renda e calculamos a média do preço final
renda_preco = df.groupby('customer_income_level')['final_price_usd'].mean().reset_index()
# Ordenamos para ver qual classe gasta mais em média
renda_preco = renda_preco.sort_values(by='final_price_usd', ascending=False)


# ========================================================
# PERGUNTA 5: Análise Geográfica (Ticket Médio por País)
# ========================================================
# Qual país tem o maior gasto médio por produto?
ticket_medio_pais = df.groupby('country')['final_price_usd'].mean().reset_index()
ticket_medio_pais = ticket_medio_pais.sort_values(by='final_price_usd', ascending=False)


# ========================================================
# PERGUNTA 6: Impacto de Descontos no Volume de Vendas
# ========================================================
# Agrupamos pelo percentual de desconto para ver o total de unidades vendidas
impacto_desconto = df.groupby('discount_percent')['units_sold'].sum().reset_index()


# ========================================================
# SALVANDO OS RESULTADOS EM EXCEL
# ========================================================
os.makedirs('data/processed', exist_ok=True)

renda_preco.to_excel('data/processed/analise_renda_preco.xlsx', index=False)
ticket_medio_pais.to_excel('data/processed/ticket_medio_por_pais.xlsx', index=False)
impacto_desconto.to_excel('data/processed/impacto_descontos.xlsx', index=False)

print("\n🎉 Sucesso! As análises de comportamento foram salvas em 'data/processed/'")
print("- analise_renda_preco.xlsx")
print("- ticket_medio_por_pais.xlsx")
print("- impacto_descontos.xlsx")