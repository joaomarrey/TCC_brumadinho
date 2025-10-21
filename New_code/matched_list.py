import pandas as pd
import os
from paths import final_data_path, raw_data_path


df_matched = pd.read_excel(os.path.join(final_data_path, 'matched_group.xlsx'))
df_codigo = pd.read_excel(os.path.join(raw_data_path, 'pop_rural_mun.xls'))
df_codigo.rename({'Município': 'NOME_MUN'}, axis=1, inplace=True)
df_codigo = df_codigo[df_codigo['Sigla'] == 'MG']
print(df_codigo)
df_matched = df_matched.merge(df_codigo, how='left', on='NOME_MUN')
print(df_matched)

lista_matched = list(df_matched['Codigo'])
# print(lista_matched)
string = ''
for i in lista_matched:
    string += "'"
    string += str(i)
    string += "'"
    string += ', '

print(string)
