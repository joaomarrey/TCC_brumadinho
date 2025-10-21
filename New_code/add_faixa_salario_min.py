import pandas as pd
import os
from paths import raw_data_path, manipulated_data_path


df_faixa_sm = pd.read_excel(os.path.join(raw_data_path, 'faixas_salario_min_mun.xlsx'), skiprows=3)
df_faixa_sm = df_faixa_sm.iloc[4:, :]
df_faixa_sm.rename({'Unnamed: 0': 'NOME_MUN'}, inplace=True, axis=1)
df_faixa_sm = df_faixa_sm.replace("-", 0)
df_faixa_sm.dropna(inplace=True)

df_faixa_sm['Menos de 1 SM'] = df_faixa_sm['Até 1/4 de salário mínimo'] + df_faixa_sm['Mais de 1/4 a 1/2 salário mínimo'] + df_faixa_sm['Mais de 1/2 a 1 salário mínimo']
df_faixa_sm['1 a 2 SM'] = df_faixa_sm['Mais de 1 a 2 salários mínimos']
df_faixa_sm['2 a 5 SM'] = df_faixa_sm['Mais de 2 a 3 salários mínimos'] + df_faixa_sm['Mais de 3 a 5 salários mínimos']
df_faixa_sm['5 a 10 SM'] = df_faixa_sm['Mais de 5 a 10 salários mínimos']
df_faixa_sm['Mais de 10 SM'] = df_faixa_sm['Mais de 10 a 15 salários mínimos'] + df_faixa_sm['Mais de 15 a 20 salários mínimos'] + df_faixa_sm['Mais de 20 a 30 salários mínimos'] + df_faixa_sm['Mais de 30 salários mínimos']

df_faixa_sm['PROP_MENOS_DE_1_SM'] = df_faixa_sm['Menos de 1 SM'] / df_faixa_sm['Total']
df_faixa_sm['PROP_1_A_2_SM'] = df_faixa_sm['1 a 2 SM'] / df_faixa_sm['Total']
df_faixa_sm['PROP_2_A_5_SM'] = df_faixa_sm['2 a 5 SM'] / df_faixa_sm['Total']
df_faixa_sm['PROP_5_A_10_SM'] = df_faixa_sm['5 a 10 SM'] / df_faixa_sm['Total']
df_faixa_sm['PROP_MAIS_DE_10_SM'] = df_faixa_sm['Mais de 10 SM'] / df_faixa_sm['Total']

df_faixa_sm = df_faixa_sm[['NOME_MUN', 'PROP_MENOS_DE_1_SM', 'PROP_1_A_2_SM', 'PROP_2_A_5_SM', 'PROP_5_A_10_SM', 'PROP_MAIS_DE_10_SM']]

df_faixa_sm['NOME_MUN'] = df_faixa_sm['NOME_MUN'].str.replace(' (MG)', '', regex=False)
df_faixa_sm['ANO'] = '2010'

print(df_faixa_sm)

df_faixa_sm.to_csv(os.path.join(manipulated_data_path, 'faixa_sm_municipios.csv'), index=False)

