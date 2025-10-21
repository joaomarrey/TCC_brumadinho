import geopandas as gpd
import pandas as pd
import os

# Read shapefile

cwd = os.getcwd()

par_dir_func = lambda x: os.path.abspath(os.path.join(x, os.pardir))

brumadinho_path = par_dir_func(par_dir_func(cwd))
# print(brumadinho_path)

shp_path = os.path.join(brumadinho_path, 'Map', 'MG_Municipios_2023', 'MG_Municipios_2023.shp')
# print(shp_path)

gdf = gpd.read_file(shp_path)
gdf['CD_MUN'] = gdf['CD_MUN'].astype('int')
gdf['CD_MUN'] = gdf['CD_MUN'].map(lambda x: int(x/10))
# print(gdf['CD_MUN'])
# print(len(gdf['CD_MUN'].unique()))
# print(gdf['NM_MUN'])

# Read CSV
df = pd.read_csv('Matched_Grupo1.csv')
df['Codigo'] = df['Codigo'].astype('int')
# print(df['Codigo'])
# print(len(df['Codigo'].unique()))
# print(df['Nome'])

# merged = gdf.merge(df, left_on='NM_MUN', right_on='Nome', how='left')
merged = gdf.merge(df, left_on='CD_MUN', right_on='Codigo', how='left')

merged.rename({'Grupo 1 controle': 'G1_CONT', 'Grupo 1 tratamento': 'G1_TRAT'}, inplace=True, axis=1)

print(merged)

save_path = os.path.join(brumadinho_path, 'Map', 'Grupo 1', 'Municipios_grupo1.shp')

merged.to_file(save_path)


