import pandas as pd
import os
from paths import raw_data_path, manipulated_data_path


df_taxa_alfabetizacao = pd.read_excel(os.path.join(raw_data_path, 'taxa_alfabetizacao_mun.xlsx'), skiprows=4)
df_taxa_alfabetizacao.rename({'Unnamed: 0': 'NOME_MUN', 'Total': 'TAXA_ALFAB'}, inplace=True, axis=1)
df_taxa_alfabetizacao['ANO'] = '2010'
df_taxa_alfabetizacao['NOME_MUN'] = df_taxa_alfabetizacao['NOME_MUN'].str.replace(' (MG)', '', regex=False)
df_taxa_alfabetizacao.dropna(inplace=True)
df_taxa_alfabetizacao = df_taxa_alfabetizacao.iloc[1:, :]

print(df_taxa_alfabetizacao)

df_taxa_alfabetizacao.to_csv(os.path.join(manipulated_data_path, "taxa_alfab_municipios.csv"), index=False)


