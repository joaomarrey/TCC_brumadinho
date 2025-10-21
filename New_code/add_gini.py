import pandas as pd
import os
from paths import raw_data_path, manipulated_data_path


df_gini = pd.read_csv(os.path.join(raw_data_path, 'gini_mun.csv'), encoding="latin1", skiprows=2)
df_gini[['COD_MUN', 'NOME_MUN']] = df_gini['Município'].str.split(" ", n=1, expand=True)
print(df_gini)

# gini_2000 = gini.loc[:, ['COD_MUN', 'NOME_MUN', '2000']]
# gini_2000['ANO'] = '2000'
# gini_2000.rename({'2000': 'GINI'}, inplace=True, axis=1)

gini_2010 = df_gini.loc[:, ['COD_MUN', 'NOME_MUN', '2010']]
gini_2010['ANO'] = '2010'
gini_2010.rename({'2010': 'GINI'}, inplace=True, axis=1)

# gini = pd.concat([gini_2000, gini_2010])
df_gini = gini_2010

df_gini = df_gini[df_gini['GINI'] != '...']
df_gini['GINI'] = df_gini['GINI'].str.replace(",", ".", regex=False).astype(float)
df_gini.dropna(inplace=True)

# print(df_gini['COD_MUN'])
df_gini = df_gini[df_gini['COD_MUN'].str[0:2] == '31']

df_gini = df_gini[['ANO',
                   #'COD_MUN',
                   'NOME_MUN', 'GINI']]

print(df_gini)

df_gini.to_csv(os.path.join(manipulated_data_path, 'gini_municipios.csv'), index=False)

