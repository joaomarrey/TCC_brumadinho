import pandas as pd
import os
from paths import manipulated_data_path, final_data_path


dados_gerais_df = pd.read_csv(os.path.join(manipulated_data_path, 'dados_gerais_municipios.csv'))

gini_mun_df = pd.read_csv(os.path.join(manipulated_data_path, 'gini_municipios.csv'))
gini_mun_df.loc[gini_mun_df['NOME_MUN'] == "Olhos-d'Água", "NOME_MUN"] = "Olhos-D'Água"
gini_mun_df.loc[gini_mun_df['NOME_MUN'] == "Pingo-d'Água", "NOME_MUN"] = "Pingo-D'Água"
gini_mun_df.loc[gini_mun_df['NOME_MUN'] == "São João del Rei", "NOME_MUN"] = "São João Del Rei"

taxa_alfab_df = pd.read_csv(os.path.join(manipulated_data_path, 'taxa_alfab_municipios.csv'))
taxa_alfab_df.loc[taxa_alfab_df['NOME_MUN'] == 'Barão do Monte Alto', 'NOME_MUN'] = 'Barão de Monte Alto'

faixa_sm_df = pd.read_csv(os.path.join(manipulated_data_path, 'faixa_sm_municipios.csv'))
faixa_sm_df.loc[faixa_sm_df['NOME_MUN'] == 'Barão do Monte Alto', 'NOME_MUN'] = 'Barão de Monte Alto'

outros_dados_df = pd.merge(dados_gerais_df, gini_mun_df, how='left', on=['NOME_MUN', 'ANO'])

outros_dados_df.loc[outros_dados_df['NOME_MUN'] == 'Brasópolis', 'NOME_MUN'] = 'Brazópolis'
outros_dados_df.loc[outros_dados_df['NOME_MUN'] == 'Dona Eusébia', 'NOME_MUN'] = 'Dona Euzébia'
outros_dados_df.loc[outros_dados_df['NOME_MUN'] == "Olhos-D'Água", 'NOME_MUN'] = "Olhos-d'Água"
outros_dados_df.loc[outros_dados_df['NOME_MUN'] == 'Passa-Vinte', 'NOME_MUN'] = 'Passa Vinte'
outros_dados_df.loc[outros_dados_df['NOME_MUN'] == "Pingo-D'Água", 'NOME_MUN'] = "Pingo-d'Água"
outros_dados_df.loc[outros_dados_df['NOME_MUN'] == 'São João Del Rei', 'NOME_MUN'] = 'São João del Rei'
outros_dados_df.loc[outros_dados_df['NOME_MUN'] == 'São Thomé das Letras', 'NOME_MUN'] = 'São Tomé das Letras'

outros_dados_df = outros_dados_df.merge(taxa_alfab_df, how='left', on=['NOME_MUN', 'ANO'])
outros_dados_df = outros_dados_df.merge(faixa_sm_df, how='left', on=['NOME_MUN', 'ANO'])
print(outros_dados_df)

outros_dados_df.to_csv(os.path.join(manipulated_data_path, 'outros_dados_municipios.csv'), index=False)
