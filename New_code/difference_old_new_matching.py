import pandas as pd
import os
from paths import final_data_path, matching_data_path

matching_old = pd.read_excel(os.path.join(matching_data_path, 'matched_group_old.xlsx'))
matching_new = pd.read_csv(os.path.join(matching_data_path, 'matching_k_nearest.csv'))

arenot = matching_new[~matching_new['NOME_MUN'].isin(matching_old["NOME_MUN"])]
print(arenot)
print(len(arenot))
