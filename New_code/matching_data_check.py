import pandas as pd
import os
from paths import final_data_path, matching_data_path


final_df = pd.read_csv(os.path.join(final_data_path, 'dados_finais_municipios.csv'))

k_nearest_df = pd.read_csv(os.path.join(matching_data_path, 'matching_k_nearest_remuneracao.csv'))

match_check_df = pd.merge(k_nearest_df, final_df, how='left', on=['NOME_MUN', 'COD_MUN'])

print(match_check_df)

match_check_df.to_csv(os.path.join(matching_data_path, 'matching_check.csv'))
