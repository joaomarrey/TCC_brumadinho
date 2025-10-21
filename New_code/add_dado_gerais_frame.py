import pandas as pd
import os
from paths import raw_data_path, manipulated_data_path


dados_gerais_df = pd.read_excel(os.path.join(raw_data_path, 'Dados Gerais.xlsx'))
dados_gerais_df.rename({'Territorialidades': 'NOME_MUN'}, axis=1, inplace=True)
dados_gerais_df = dados_gerais_df.iloc[:854]
dados_gerais_df.drop(0, inplace=True)
# print(dados_gerais_df.columns)

exp_vida_mort_inf_idhm_df = dados_gerais_df.loc[:, ['NOME_MUN', 'Esperança de vida ao nascer 2010', 'Mortalidade infantil 2010',
                                        'IDHM 2010', 'IDHM Renda 2010', 'IDHM Longevidade 2010', 'IDHM Educação 2010']
                            ]
exp_vida_mort_inf_idhm_df['ANO'] = 2010
exp_vida_mort_inf_idhm_df.rename({'Esperança de vida ao nascer 2010': 'EXP_VIDA_AO_NASCER',
                               'Mortalidade infantil 2010': 'MORTALIDADE_INFANTIL', 'IDHM 2010': 'IDHM',
                               'IDHM Renda 2010': 'IDHM_RENDA', 'IDHM Longevidade 2010': 'IDHM_LONGEVIDADE',
                               'IDHM Educação 2010': 'IDHM_EDU'}, axis=1, inplace=True)

dfs_renda_media_e_bolsa_familia = []
for i in range(2013, 2018):
    df = dados_gerais_df.loc[:, ['NOME_MUN', f'Rendimento médio no setor formal {i}',
                                 f'Transferência per capita do Bolsa Família {i}']]
    df['ANO'] = i
    df.rename({f'Rendimento médio no setor formal {i}': 'REND_MEDIO_FORMAL',
               f'Transferência per capita do Bolsa Família {i}': 'TRANSF_PER_CAPITA_BOLSA_FAMILIA'},
              axis=1, inplace=True)
    dfs_renda_media_e_bolsa_familia.append(df)

renda_media_formal_e_bolsa_familia_df = pd.concat(dfs_renda_media_e_bolsa_familia, axis='index')

dados_gerais_df = pd.concat([exp_vida_mort_inf_idhm_df, renda_media_formal_e_bolsa_familia_df], axis='index')
print(dados_gerais_df)

dados_gerais_df['NOME_MUN'] = dados_gerais_df['NOME_MUN'].map(lambda x: x.replace(' (MG)', ''))

dados_gerais_df.to_csv(os.path.join(manipulated_data_path, 'dados_gerais_municipios.csv'), index=False)


