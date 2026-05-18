import streamlit as st
import pandas as pd

# ==========================================
# CONFIGURAÇÃO DA PÁGINA (DESIGN DO DASHBOARD)
# ==========================================
st.set_page_config(page_title="Dashboard de Vendas - Grupo 49", layout="wide")

st.title("📊 Dashboard de Performance de Vendas e Consumo")
st.markdown("---")

import os

# ==========================================
# CARREGAMENTO DOS DADOS TRATADOS
# ==========================================
# Descobre a pasta exata onde o main.py está rodando (app/)
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Junta o caminho da pasta atual com o arquivo base_limpa.csv que está nela
caminho_base = os.path.join(diretorio_atual, 'base_limpa.csv')

# Lê a base de dados de forma definitiva
df = pd.read_csv(caminho_base)

# ==========================================
# BARRA LATERAL - FILTROS DINÂMICOS
# ==========================================
st.sidebar.header("Filtros do Dashboard")

# Filtro de País
lista_paises = ["Todos"] + list(df['country'].unique())
pais_selecionado = st.sidebar.selectbox("Selecione o País:", lista_paises)

# Filtro de Marca
lista_marcas = ["Todas"] + list(df['brand'].unique())
marca_selecionada = st.sidebar.selectbox("Selecione a Marca:", lista_marcas)

# Aplicando os filtros na base de dados de forma dinâmica
df_filtrado = df.copy()
if pais_selecionado != "Todos":
    df_filtrado = df_filtrado[df_filtrado['country'] == pais_selecionado]
if marca_selecionada != "Todas":
    df_filtrado = df_filtrado[df_filtrado['brand'] == marca_selecionada]

# ==========================================
# 1. VALORES TOTAIS (CARDS DE MÉTRICAS)
# ==========================================
# Mostra resumos rápidos no topo do site
col1, col2, col3 = st.columns(3)

with col1:
    faturamento_total = df_filtrado['revenue_usd'].sum()
    st.metric(label="💰 Faturamento Total (USD)", value=f"${faturamento_total:,.2f}")

with col2:
    total_vendido = df_filtrado['units_sold'].sum()
    st.metric(label="👟 Total de Unidades Vendidas", value=f"{total_vendido:,}")

with col3:
    ticket_medio = df_filtrado['final_price_usd'].mean()
    st.metric(label="🎯 Ticket Médio por Item", value=f"${ticket_medio:,.2f}")

st.markdown("---")

# ==========================================
# 2. GRÁFICOS INTERATIVOS
# ==========================================
col_esq, col_dir = st.columns(2)

with col_esq:
    st.subheader("🏆 Melhores Categorias (Volume de Vendas)")
    # Agrupa e soma com base no que foi filtrado pelo usuário
    vendas_cat = df_filtrado.groupby('category')['units_sold'].sum().sort_values(ascending=True)
    st.bar_chart(vendas_cat)

with col_dir:
    st.subheader("📈 Faturamento por Marca")
    faturamento_marca = df_filtrado.groupby('brand')['revenue_usd'].sum().sort_values(ascending=True)
    st.bar_chart(faturamento_marca)

st.markdown("---")

# ==========================================
# 3. TABELA DE DADOS (INSIGHTS DE RENDA)
# ==========================================
st.subheader("💎 Comportamento de Compra por Nível de Renda")
renda_preco = df_filtrado.groupby('customer_income_level')['final_price_usd'].mean().reset_index()
renda_preco.columns = ['Nível de Renda', 'Preço Médio Pago ($)']
st.dataframe(renda_preco, use_container_width=True)