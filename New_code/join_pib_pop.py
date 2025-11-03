import pandas as pd
import os
from paths import manipulated_data_path, manipulated_data_path


gdp_df = pd.read_csv(os.path.join(manipulated_data_path, 'pib_municipios.csv'))
print(gdp_df)

pop_df = pd.read_csv(os.path.join(manipulated_data_path, 'pop_municipios.csv'))
print(pop_df)

# gdp_pop_df = pd.merge(gdp_df, pop_df, how='left', on=['NOME_MUN', 'ANO'])
pop_df.drop('NOME_MUN', axis=1, inplace=True)
gdp_pop_df = pd.merge(gdp_df, pop_df, how='left', on=['COD_MUN', 'ANO'])

gdp_pop_df.loc[gdp_pop_df["ANO"] == 2010, 'POP'] = round((gdp_pop_df.loc[gdp_pop_df["ANO"] == 2010, 'PIB'] / gdp_pop_df.loc[gdp_pop_df["ANO"] == 2010, 'PIB_PER_CAPITA']) * 1000)
print(gdp_pop_df.loc[gdp_pop_df["ANO"] == 2010, 'POP'])

gdp_pop_df.loc[gdp_pop_df["ANO"] == 2007, 'POP'] = round((gdp_pop_df.loc[gdp_pop_df["ANO"] == 2007, 'PIB'] / gdp_pop_df.loc[gdp_pop_df["ANO"] == 2007, 'PIB_PER_CAPITA']) * 1000)
print(gdp_pop_df.loc[gdp_pop_df["ANO"] == 2007, 'POP'])

print(gdp_pop_df)
# print(gdp_pop_df['NOME_MUN'])

gdp_pop_df[['VA_AGRO_PER_CAPITA', 'VA_IND_PER_CAPITA', 'VA_SERV_PER_CAPITA', 'VA_ADM_PER_CAPITA', 'VA_TOT_PER_CAPITA',
            'IMPOSTOS_INDIRETOS_LIQ_SUBSIDIOS_PER_CAPITA']] = (
    gdp_pop_df[['VA_AGRO', 'VA_IND', 'VA_SERV', 'VA_ADM', 'VA_TOT', 'IMPOSTOS_INDIRETOS_LIQ_SUBSIDIOS']].div(
    gdp_pop_df['POP'], axis=0
    )) * 1000

gdp_pop_df[['VA_AGRO_SOBRE_VA_TOT', 'VA_IND_SOBRE_VA_TOT', 'VA_SERV_SOBRE_VA_TOT', 'VA_ADM_SOBRE_VA_TOT']] = (
    gdp_pop_df[['VA_AGRO', 'VA_IND', 'VA_SERV', 'VA_ADM']].div(
    gdp_pop_df['VA_TOT'], axis=0
    ))

# print(gdp_pop_df['VA_AGRO'] / gdp_pop_df['POP'].iloc[4260:])

gdp_pop_df.to_csv(os.path.join(manipulated_data_path, 'pib_pop_municipios.csv'), index=False)

