import pandas as pd
import os
from paths import manipulated_data_path


caged = pd.read_csv(os.path.join(manipulated_data_path, 'caged_municipios.csv'))
print(caged.head())

# Fix months without data
caged = caged.set_index(['ANO', 'MES', 'COD_MUN'])
municipalities = caged.index.get_level_values('COD_MUN').unique()
years = caged.index.get_level_values('ANO').unique()
months = range(1, 13) # Full range of months

new_index = pd.MultiIndex.from_product(
    [years, months, municipalities],
    names=['ANO', 'MES', 'COD_MUN']
)

caged = caged.reindex(new_index)
caged = caged.reset_index()
caged.sort_values(by=['ANO', 'MES', 'COD_MUN'], inplace=True)
print(caged.head())

caged[['ADMITIDOS', 'DESLIGADOS', 'SALDO']] = caged[['ADMITIDOS', 'DESLIGADOS', 'SALDO']].fillna(0)



rais_estabelecimentos = pd.read_csv(os.path.join(manipulated_data_path, 'rais_estabelecimentos_municipios.csv'))


first_year = min(caged['ANO'].astype(int))

print(str(first_year - 1))

first_employment = rais_estabelecimentos.loc[rais_estabelecimentos['ANO'] == (first_year - 1), [
                                                                                                   # 'ANO',
                                                                                                   # 'SIGLA_UF',
                                                                                                   'COD_MUN',
                                                                                                   'VINCULOS_ATIVOS'
                                                                                                   ]]
print(first_employment)

# first_employment['DATA'] = pd.to_datetime(str(first_year - 1) + '-12-01')
first_employment.rename({'VINCULOS_ATIVOS': 'VINCULOS_INICIAIS'}, axis=1, inplace=True)

caged['DATA'] = pd.to_datetime(caged['ANO'].astype(str) + '-' + caged['MES'].astype(str) + '-' + '01')


employment_mes_df = pd.merge(caged, first_employment, how='left', on=['COD_MUN'])

employment_mes_df.sort_values(['COD_MUN', 'DATA'])

print(employment_mes_df)

employment_mes_df['VINCULOS_ATIVOS'] = employment_mes_df.groupby('COD_MUN')['SALDO'].cumsum() + employment_mes_df['VINCULOS_INICIAIS']

employment_mes_df.drop(['VINCULOS_INICIAIS', 'DATA'], axis=1, inplace=True)

print(employment_mes_df)


# employment_df = pd.read_csv(os.path.join(manipulated_data_path, 'empregos_caged_mes_municipios.csv'))
employment_ano_df = employment_mes_df.loc[:, ['ANO', 'COD_MUN', 'VINCULOS_ATIVOS',
                                              #'NUM_FIRMAS'
                                              ]].groupby(['COD_MUN', 'ANO']).mean()
employment_ano_df.rename({'VINCULOS_ATIVOS': 'VINCULOS_MEDIA',
                          #'NUM_FIRMAS': 'NUM_FIRMAS_MEDIA'
                          }, axis=1, inplace=True)

print(employment_ano_df)

employment_mes_df.to_csv(os.path.join(manipulated_data_path, 'empregos_caged_mes_municipios.csv'), index=False)
employment_ano_df.to_csv(os.path.join(manipulated_data_path, 'empregos_caged_ano_municipios.csv'))

