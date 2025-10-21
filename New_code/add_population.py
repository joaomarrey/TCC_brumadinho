import pandas as pd
import os
from paths import raw_data_path, manipulated_data_path


pop_df = pd.read_csv(os.path.join(raw_data_path, 'pop_mun_estimada_2002_2021.csv'), skiprows=2)
pop_df.columns = ['NOME_MUN', 'ANO', 'POP']
pop_df = pop_df.iloc[:15354]
pop_df['NOME_MUN'] = pop_df['NOME_MUN'].map(lambda x: x.replace(' (MG)', ''))
print(pop_df)

pop_df.loc[pop_df['NOME_MUN'] == 'Barão do Monte Alto', 'NOME_MUN'] = 'Barão de Monte Alto'

pop_rural_df = pd.read_excel(os.path.join(raw_data_path, 'pop_rural_mun.xls'))
codigo_df = pop_rural_df.loc[:, ['Codigo', 'Município']]

codigo_df.loc[codigo_df["Município"] == 'Brasópolis', "Município"] = 'Brazópolis'
codigo_df.loc[codigo_df["Município"] == 'Dona Eusébia', "Município"] = 'Dona Euzébia'
codigo_df.loc[codigo_df["Município"] == 'Itabirinha de Mantena', "Município"] = 'Itabirinha'
codigo_df.loc[codigo_df["Município"] == 'Passa-Vinte', "Município"] = 'Passa Vinte'
codigo_df.loc[codigo_df["Município"] == 'São Thomé das Letras', "Município"] = 'São Tomé das Letras'

pop_rural_df = pop_rural_df.loc[:, ['Sigla', 'Município', '2010']]
pop_rural_df = pop_rural_df[pop_rural_df['Sigla'] == 'MG']
pop_rural_df.reset_index(drop=True, inplace=True)
pop_rural_df.rename({'Município': 'NOME_MUN', '2010': 'POP_RURAL'}, axis=1, inplace=True)
pop_rural_df['ANO'] = '2010'
pop_rural_df.drop('Sigla', axis=1, inplace=True)
print(pop_rural_df)

# print(pop_df.loc[pop_df['ANO'] == '2009', 'POP'].reset_index(drop=True) + pop_df.loc[pop_df['ANO'] == '2011', 'POP'].reset_index(drop=True))
df_estimate_pop_2010 = (pop_df.loc[pop_df['ANO'] == '2009', 'POP'].reset_index(drop=True) +
                        pop_df.loc[pop_df['ANO'] == '2011', 'POP'].reset_index(drop=True)) / 2
# print(df_estimate_pop_2010)

# print(pop_rural_df['POP_RURAL'].reset_index(drop=True))
# print(df_estimate_pop_2010)
# print(pop_rural_df['POP_RURAL'].reset_index(drop=True).div(df_estimate_pop_2010))
pop_rural_df['PROPORCAO_DA_POP_RURAL'] = pop_rural_df['POP_RURAL'].reset_index(drop=True).div(df_estimate_pop_2010)
# print(pop_rural_df['PROPORCAO_DA_POP_RURAL'])

pop_df = pop_df.merge(pop_rural_df, how='outer', on=['NOME_MUN', 'ANO'])

codigo_df.rename({'Codigo': 'COD_MUN', 'Município': 'NOME_MUN'}, axis=1, inplace=True)
pop_df = pop_df.merge(codigo_df, how='left', on='NOME_MUN')

# pop_df.loc[pop_df['NOME_MUN'] == 'Brasópolis', 'NOME_MUN'] = 'Brazópolis'
# pop_df.loc[pop_df['NOME_MUN'] == 'São Thomé das Letras', 'NOME_MUN'] = 'São Tomé das Letras'
# pop_df.loc[pop_df['NOME_MUN'] == 'Passa-Vinte', 'NOME_MUN'] = 'Passa Vinte'
# pop_df.loc[pop_df['NOME_MUN'] == 'Itabirinha de Mantena', 'NOME_MUN'] = 'Itabirinha'

print(pop_df)
pop_df.to_csv(os.path.join(manipulated_data_path, 'pop_municipios.csv'), index=False)


