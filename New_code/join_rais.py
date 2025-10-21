import pandas as pd
import os
from paths import manipulated_data_path, manipulated_data_path


rais_vinculos_df = pd.read_csv(os.path.join(manipulated_data_path, 'rais_vinculos_municipios.csv'))

rais_estabelecimentos_df = pd.read_csv(os.path.join(manipulated_data_path, 'rais_estabelecimentos_municipios.csv'))

rais_joined_df = pd.merge(rais_vinculos_df, rais_estabelecimentos_df, how='left', on=['ANO', 'COD_MUN', 'SIGLA_UF'])

rais_joined_df.to_csv(os.path.join(manipulated_data_path, 'rais_integrada_municipios.csv'), index=False)
