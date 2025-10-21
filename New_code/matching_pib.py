import pandas as pd
import os
from paths import final_data_path, matching_data_path
import math
from scipy.stats import zscore
from scipy.spatial import distance
import numpy as np


covariates = [
                "PIB_PER_CAPITA",
                # "POP",
                #"PROPORCAO_DA_POP_RURAL",
                # "VA_AGRO_PER_CAPITA", "VA_IND_PER_CAPITA",
                # "VA_SERV_PER_CAPITA", "VA_ADM_PER_CAPITA",
                #"IMPOSTOS_INDIRETOS_LIQ_SUBSIDIOS_PER_CAPITA",
                "VA_AGRO_SOBRE_VA_TOT",
                "VA_IND_SOBRE_VA_TOT",
                "VA_SERV_SOBRE_VA_TOT",
                "VA_ADM_SOBRE_VA_TOT",
                # "EXP_VIDA_AO_NASCER",
                # "MORTALIDADE_INFANTIL",
                "IDHM_RENDA",
                "IDHM_LONGEVIDADE", "IDHM_EDU",
                # "REMUNERACAO_MEDIA",
                # "REND_MEDIO_FORMAL",
                # "TRANSF_PER_CAPITA_BOLSA_FAMILIA",
                'GINI',
                # 'TAXA_ALFAB',
                # 'PROP_MENOS_DE_1_SM',
                # 'PROP_1_A_2_SM',
                # 'PROP_2_A_5_SM',
                # 'PROP_5_A_10_SM',
                # 'PROP_MAIS_DE_10_SM',
                'VA_AGRO', 'VA_IND', 'VA_SERV', 'VA_ADM',
                'VA_TOT'
                                                                            ]


matching_df = pd.read_csv(os.path.join(final_data_path, 'dados_finais_municipios.csv'))

pre = list(range(2000, 2019))
print(pre)
matching_df = matching_df[matching_df['ANO'].isin(pre)]

matching_pivot = matching_df.pivot(index=['NOME_MUN', 'COD_MUN'], columns='ANO', values=covariates)

matching_pivot.dropna(axis=1, inplace=True, how='all')
matching_pivot.dropna(axis=0, inplace=True, how='any')

print(matching_pivot)


matching_pivot_standard = matching_pivot.apply(zscore, ddof=1)
print(matching_pivot_standard)
print(matching_pivot_standard.mean())
print(matching_pivot_standard.std(ddof=1))

ind = list(matching_pivot_standard.index)
print(ind)
ind.remove(('Brumadinho', 3109006))
distance_dict = {'NOME_MUN': [], 'COD_MUN': [], 'DISTANCIA': []}


## for mahalanobis
# treated unit's data
treated_unit = matching_pivot_standard.loc[('Brumadinho', 3109006), :].values

# control units' data
control_df = matching_pivot_standard.drop(index=('Brumadinho', 3109006))
control_units = control_df.values
control_names = control_df.index

# mahalanobis distance requires the inverse of the covariance matrix of the data that defines the "space" (i.e., the control units)
# use .T to transpose the data so covariance is calculated feature-wise
covariance_matrix = np.cov(control_units.T)
inv_covariance_matrix = np.linalg.inv(covariance_matrix)


for mun in ind:
    # print(mun)
    # print(matching_pivot_standard.columns)
    # print(matching_pivot_standard.loc[mun, :] - matching_pivot_standard.loc[('Brumadinho', 3109006), :])

    ## calculates standard diff
    # diff_vector = np.array([matching_pivot_standard.loc[mun, :] - matching_pivot_standard.loc[('Brumadinho', 3109006), :]])

    ## calculates percent diff
    diff_vector = np.array([(matching_pivot_standard.loc[mun, :] / matching_pivot_standard.loc[('Brumadinho', 3109006), :]) - 1])


    # print(diff_vector)
    # raise Exception

    ## calculates euclidian difference
    # dist = math.sqrt(np.sum(np.square(diff_vector)))
    # dist = np.linalg.norm(diff_vector)
    # print('euclidian', dist)

    ## calculates manhattan difference
    dist = np.sum(np.abs(diff_vector))
    # print('manhattan', dist)

    ## calculates mahalanobis distance
    # control_unit = matching_pivot_standard.loc[mun, :].values
    # dist = distance.mahalanobis(treated_unit, control_unit, inv_covariance_matrix)
    # print('mahalanobis', dist)

    distance_dict['NOME_MUN'].append(mun[0])
    distance_dict['COD_MUN'].append(mun[1])
    distance_dict['DISTANCIA'].append(dist)


# weights_list = []
#
# for i in matching_pivot_standard.columns:
#     # common = set(important_covariates) & set(i)
#
#     weights_list.append(1)
#
# for mun in ind:
#     # print(mun)
#     # print(matching_pivot_standard.columns)
#     # print(matching_pivot_standard.loc[mun, :] - matching_pivot_standard.loc[('Brumadinho', 3109006), :])
#
#     euc_vector = np.array([matching_pivot_standard.loc[mun, :] - matching_pivot_standard.loc[('Brumadinho', 3109006), :]])
#     # print(euc_vector)
#
#     weights_vector = np.array(weights_list)
#     euc_vector = np.dot(euc_vector, weights_vector)
#     # euc_vector = np.sum(euc_vector)
#     # print(euc_vector)
#
#     # euclidian_vect_new = np.array([matching_pivot_standard.loc[mun, :] - matching_pivot_standard.loc[('Brumadinho', 3109006), :]])
#
#
#     euclidian = math.sqrt(np.sum(np.square(euc_vector)))
#
#     distance_dict['NOME_MUN'].append(mun[0])
#     distance_dict['COD_MUN'].append(mun[1])
#     distance_dict['DISTANCIA'].append(euclidian)


matched = pd.DataFrame(distance_dict).sort_values(by='DISTANCIA')
print(matched)

k_nearest = matched.iloc[:30, 0:2]

print(matched)

# doing matching without downstream municipalities
downstream = pd.read_csv(os.path.join(matching_data_path, 'downstream_municipios.csv'))

matched_no_downstream = matched[~matched['COD_MUN'].isin(downstream['COD_MUN'])]

k_nearest_no_downstream = matched_no_downstream.iloc[:30, 0:2]



matching_pivot.to_csv(os.path.join(matching_data_path, 'matching_pivot_pib.csv'))
matching_pivot_standard.to_csv(os.path.join(matching_data_path, 'matching_pivot_standard_pib.csv'))
matched.to_csv(os.path.join(matching_data_path, 'matched_distance_pib.csv'), index=False)
k_nearest.to_csv(os.path.join(matching_data_path, 'matching_k_nearest_pib.csv'), index=False)

matched_no_downstream.to_csv(os.path.join(matching_data_path, 'matched_distance_no_downstream_pib.csv'), index=False)
k_nearest_no_downstream.to_csv(os.path.join(matching_data_path, 'matching_k_nearest_no_downstream_pib.csv'), index=False)
