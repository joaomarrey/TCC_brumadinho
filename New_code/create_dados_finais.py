import pandas as pd
import os
from paths import manipulated_data_path, final_data_path
from scipy.stats import zscore
import numpy as np


outros_dados_df = pd.read_csv(os.path.join(manipulated_data_path, 'outros_dados_municipios.csv'))
# outros_dados_df.loc[outros_dados_df['NOME_MUN'] == 'Brasópolis', 'NOME_MUN'] = 'Brazópolis'
# outros_dados_df.loc[outros_dados_df['NOME_MUN'] == 'Dona Eusébia', 'NOME_MUN'] = 'Dona Euzébia'
# outros_dados_df.loc[outros_dados_df['NOME_MUN'] == "Olhos-D'Água", 'NOME_MUN'] = "Olhos-d'Água"
# outros_dados_df.loc[outros_dados_df['NOME_MUN'] == 'Passa-Vinte', 'NOME_MUN'] = 'Passa Vinte'
# outros_dados_df.loc[outros_dados_df['NOME_MUN'] == "Pingo-D'Água", 'NOME_MUN'] = "Pingo-d'Água"
# outros_dados_df.loc[outros_dados_df['NOME_MUN'] == 'São João Del Rei', 'NOME_MUN'] = 'São João del Rei'
# outros_dados_df.loc[outros_dados_df['NOME_MUN'] == 'São Thomé das Letras', 'NOME_MUN'] = 'São Tomé das Letras'

pib_pop_df = pd.read_csv(os.path.join(manipulated_data_path, 'pib_pop_municipios.csv'))

rais_joined_df = pd.read_csv(os.path.join(manipulated_data_path, 'rais_integrada_municipios.csv'))

final_df = pd.merge(pib_pop_df, outros_dados_df, how='left', on=['NOME_MUN', 'ANO'])

id_columns = ['ANO', 'COD_UF', 'NOME_UF', 'COD_MUN', 'NOME_MUN']
all_columns = final_df.columns
for ano in range(2022, 2025):
    aux_df = final_df[final_df["ANO"] == 2021].copy()
    for col in all_columns:
        if col not in id_columns:
            aux_df[col] = None
    aux_df['ANO'] = ano

    final_df = pd.concat([final_df, aux_df])


final_df = pd.merge(final_df, rais_joined_df, how='left', on=['ANO', 'COD_MUN'])

caged_df = pd.read_csv(os.path.join(manipulated_data_path, 'empregos_caged_ano_municipios.csv'))
final_df = pd.merge(final_df, caged_df, how='left', on=['COD_MUN', 'ANO'])

final_df["PROP_POP_EMPREGADA"] = final_df["VINCULOS_ATIVOS"] / final_df["POP"]
final_df["PROP_POP_EMPREGADA_CLT"] = final_df["VINCULOS_CLT"] / final_df["POP"]
final_df["PROP_POP_EMPREGADA_ESTATUTARIOS"] = final_df["VINCULOS_ESTATUTARIOS"] / final_df["POP"]

final_df["FIRMAS_PER_CAPITA"] = final_df["NUM_FIRMAS"] / final_df["POP"]

final_df["PROP_EMPREGADOS_CLT"] = final_df["VINCULOS_CLT"] / final_df["VINCULOS_ATIVOS"]
final_df["PROP_EMPREGADOS__ESTATUTARIOS"] = final_df["VINCULOS_ESTATUTARIOS"] / final_df["VINCULOS_ATIVOS"]

# print(final_df[final_df['ANO'] == 2023].loc[:, 'VA_TOT'])
print(final_df)

# % employed
final_df["PROP_MEDIA_POP_EMPREGADA"] = final_df["VINCULOS_MEDIA"] / final_df["POP"]


# testing using ln() of salary
final_df["LN_REMUNERACAO_MEDIA"] = np.log(final_df["REMUNERACAO_MEDIA"])

final_df.to_csv(os.path.join(final_data_path, 'dados_finais_municipios.csv'), index=False)

# final_df_strings = final_df[["ANO", "COD_UF", "NOME_UF", "COD_MUN", "NOME_MUN"]]
# final_df_values = final_df.drop(["ANO", "COD_UF", "NOME_UF", "COD_MUN", "NOME_MUN"], axis=1)
#
# # final_df_standard_values = final_df_values.apply(zscore, ddof=1)
# final_df_standard_values = final_df_values.apply(
#     lambda col: zscore(col, ddof=1, nan_policy="omit"),
#     axis=0
# )
# print(final_df_standard_values)
# print(final_df_standard_values.mean())
# print(final_df_standard_values.std(ddof=1))
#
# final_df_standard = pd.concat([final_df_strings, final_df_standard_values], axis=1)
#
#
# print(final_df_standard)
#
# final_df_standard.to_csv(os.path.join(final_data_path, "dados_finais_municipios_padronizado.csv"), index=False)