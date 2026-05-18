import pandas as pd
import os

print("="*50)
print("EXECUTANDO: 00_Limpeza e Preparação de Dados")
print("="*50)

# 1. Ler a base bruta
df = pd.read_csv('data/raw/base_original.csv')

# 2. Checagem e remoção de linhas duplicadas
duplicados = df.duplicated().sum()
print(f"-> Linhas duplicadas encontradas: {duplicados}")
if duplicados > 0:
    df = df.drop_duplicates()
    print("   Linhas duplicadas removidas com sucesso!")

# 3. Garantir que a coluna de data seja reconhecida como Data pelo Python
df['order_date'] = pd.to_datetime(df['order_date'])

# 4. Limpeza de textos (remover espaços extras que vêm do teclado nas colunas de texto)
colunas_texto = ['brand', 'model_name', 'category', 'gender', 'color', 'country']
for col in colunas_texto:
    df[col] = df[col].astype(str).str.strip()

# 5. Salvar a base limpa oficial em formato CSV na pasta processed
os.makedirs('data/processed', exist_ok=True)
df.to_csv('data/processed/base_limpa.csv', index=False)

print("\n🎉 Base verificada, padronizada e salva em 'data/processed/base_limpa.csv'!")