import pandas as pd
from paths import final_data_path, matching_data_path
import os


downstream_list = [3109006, 3106705
              , 3162922, 3130101, 3140159
              , 3136652, 3126000, 3147105, 3124104, 3163102, 3149606, 3126406, 3139706, 3146909,
              3147402, 3152006, 3120904, 3125705,]

final_df = pd.read_csv(os.path.join(final_data_path, 'dados_finais_municipios.csv'))
final_df = final_df[final_df['ANO'] == 2021]

downstream = final_df.loc[final_df['COD_MUN'].isin(downstream_list), ['NOME_MUN', 'COD_MUN']]

downstream.to_csv(os.path.join(matching_data_path, 'downstream_municipios.csv'), index=False)
