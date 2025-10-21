import pandas as pd
import os
from paths import manipulated_data_path, final_data_path


balance_df = pd.read_csv(os.path.join(final_data_path, 'test_balance.csv'))
index = balance_df.columns[0]
balance_df.set_index(index, inplace=True)
# print(balance_df)

balance_df = balance_df.loc[2010, :]
mask = balance_df != 1
output = balance_df[mask]
print(output)
