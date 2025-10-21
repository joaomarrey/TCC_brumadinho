import pandas as pd
import os
from paths import raw_data_path, manipulated_data_path

df_gdp_02_09 = pd.read_excel(os.path.join(raw_data_path, 'PIB_municipios_2002_2009.xls'))
df_gdp_02_09 = df_gdp_02_09[df_gdp_02_09['Nome da Unidade da Federação'] == 'Minas Gerais']
df_gdp_02_09.columns = df_gdp_02_09.columns.str.replace('\n', ' ')
df_gdp_02_09 = df_gdp_02_09[['Ano', 'Código da Unidade da Federação', 'Nome da Unidade da Federação',
                             'Código do Município', 'Nome do Município',
                             'Valor adicionado bruto da Agropecuária,  a preços correntes (R$ 1.000)',
                             'Valor adicionado bruto da Indústria, a preços correntes (R$ 1.000)',
                             'Valor adicionado bruto dos Serviços, a preços correntes  - exceto Administração, defesa, educação e saúde públicas e seguridade social (R$ 1.000)',
                             'Valor adicionado bruto da Administração, defesa, educação e saúde públicas e seguridade social,  a preços correntes (R$ 1.000)',
                             'Valor adicionado bruto total,  a preços correntes (R$ 1.000)',
                             'Impostos, líquidos de subsídios, sobre produtos,  a preços correntes (R$ 1.000)',
                             'Produto Interno Bruto,  a preços correntes (R$ 1.000)',
                             'Produto Interno Bruto per capita,  a preços correntes (R$ 1,00)'
                             ]]
df_gdp_02_09.rename({
                    'Ano': 'ANO',
                    'Código da Unidade da Federação': 'COD_UF',
                    'Nome da Unidade da Federação': 'NOME_UF',
                    'Código do Município': 'COD_MUN',
                    'Nome do Município': 'NOME_MUN',
                    'Valor adicionado bruto da Agropecuária,  a preços correntes (R$ 1.000)': 'VA_AGRO',
                    'Valor adicionado bruto da Indústria, a preços correntes (R$ 1.000)': 'VA_IND',
                    'Valor adicionado bruto dos Serviços, a preços correntes  - exceto Administração, defesa, educação e saúde públicas e seguridade social (R$ 1.000)': 'VA_SERV',
                    'Valor adicionado bruto da Administração, defesa, educação e saúde públicas e seguridade social,  a preços correntes (R$ 1.000)': 'VA_ADM',
                    'Valor adicionado bruto total,  a preços correntes (R$ 1.000)': 'VA_TOT',
                    'Impostos, líquidos de subsídios, sobre produtos,  a preços correntes (R$ 1.000)': 'IMPOSTOS_INDIRETOS_LIQ_SUBSIDIOS',
                    'Produto Interno Bruto,  a preços correntes (R$ 1.000)': 'PIB',
                    'Produto Interno Bruto per capita,  a preços correntes (R$ 1,00)': 'PIB_PER_CAPITA'
                    },
                    inplace=True,
                    axis=1)

print(df_gdp_02_09)
# print(df_gdp_02_09["Nome do Município"])
# print(df_gdp_02_09.columns)


df_gdp_10_21 = pd.read_excel(os.path.join(raw_data_path, 'PIB_municipios_2010_2021.xlsx'))
df_gdp_10_21 = df_gdp_10_21[df_gdp_10_21['Nome da Unidade da Federação'] == 'Minas Gerais']
df_gdp_10_21.columns = df_gdp_10_21.columns.str.replace('\n', ' ')
# print(df_gdp_10_21.columns)
df_gdp_10_21 = df_gdp_10_21[['Ano', 'Código da Unidade da Federação', 'Nome da Unidade da Federação',
                             'Código do Município', 'Nome do Município',
                             'Valor adicionado bruto da Agropecuária, a preços correntes (R$ 1.000)',
                             'Valor adicionado bruto da Indústria, a preços correntes (R$ 1.000)',
                             'Valor adicionado bruto dos Serviços, a preços correntes - exceto Administração, defesa, educação e saúde públicas e seguridade social (R$ 1.000)',
                             'Valor adicionado bruto da Administração, defesa, educação e saúde públicas e seguridade social, a preços correntes (R$ 1.000)',
                             'Valor adicionado bruto total, a preços correntes (R$ 1.000)',
                             'Impostos, líquidos de subsídios, sobre produtos, a preços correntes (R$ 1.000)',
                             'Produto Interno Bruto, a preços correntes (R$ 1.000)',
                             'Produto Interno Bruto per capita, a preços correntes (R$ 1,00)'
                             ]]
df_gdp_10_21.rename({
                    'Ano': 'ANO',
                    'Código da Unidade da Federação': 'COD_UF',
                    'Nome da Unidade da Federação': 'NOME_UF',
                    'Código do Município': 'COD_MUN',
                    'Nome do Município': 'NOME_MUN',
                    'Valor adicionado bruto da Agropecuária, a preços correntes (R$ 1.000)': 'VA_AGRO',
                    'Valor adicionado bruto da Indústria, a preços correntes (R$ 1.000)': 'VA_IND',
                    'Valor adicionado bruto dos Serviços, a preços correntes - exceto Administração, defesa, educação e saúde públicas e seguridade social (R$ 1.000)': 'VA_SERV',
                    'Valor adicionado bruto da Administração, defesa, educação e saúde públicas e seguridade social, a preços correntes (R$ 1.000)': 'VA_ADM',
                    'Valor adicionado bruto total, a preços correntes (R$ 1.000)': 'VA_TOT',
                    'Impostos, líquidos de subsídios, sobre produtos, a preços correntes (R$ 1.000)': 'IMPOSTOS_INDIRETOS_LIQ_SUBSIDIOS',
                    'Produto Interno Bruto, a preços correntes (R$ 1.000)': 'PIB',
                    'Produto Interno Bruto per capita, a preços correntes (R$ 1,00)': 'PIB_PER_CAPITA'
                    },
                    inplace=True,
                    axis=1)

print(df_gdp_10_21)
# print(df_gdp_10_21.columns)

df_gdp_02_21 = pd.concat([df_gdp_02_09, df_gdp_10_21], axis='index')
df_gdp_02_21.reset_index(drop=True, inplace=True)
print(df_gdp_02_21)
print(df_gdp_02_21.head)

df_gdp_02_21.to_csv(os.path.join(manipulated_data_path, 'pib_municipios.csv'), index=False)
