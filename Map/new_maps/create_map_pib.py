import geopandas as gpd
import os
import matplotlib
import pandas as pd

matplotlib.use('Agg')  # Non-GUI backend
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from paths import matching_data_path, maps_data

rio_paraopeba = gpd.read_file('Rio_Paraopeba/rio_paraopeba.shp')

# with downstream
matched = pd.read_csv(os.path.join(matching_data_path, 'matching_k_nearest_pib.csv'))
merged = gpd.read_file(os.path.join(maps_data, 'MG_Municipios_2023.shp'))

downstream = pd.read_csv(os.path.join(matching_data_path, 'downstream_municipios.csv'))

print(merged['CD_MUN'])
print(matched['COD_MUN'])

merged.loc[merged['CD_MUN'] == '3109006', 'TRATADOS'] = 1
merged.loc[merged['CD_MUN'] != '3109006', 'TRATADOS'] = 0
merged.loc[merged['CD_MUN'].isin(matched['COD_MUN'].astype(str)), 'CONTROLES'] = 1
merged.loc[~merged['CD_MUN'].isin(matched['COD_MUN'].astype(str)), 'CONTROLES'] = 0
merged.loc[merged['CD_MUN'].isin(downstream['COD_MUN'].astype(str)), 'DOWNSTREAM'] = 1
merged.loc[~merged['CD_MUN'].isin(downstream['COD_MUN'].astype(str)), 'DOWNSTREAM'] = 0

# Combine into a bivariate code (e.g. '02', '11', etc.)
merged['bivar_code'] = (merged['TRATADOS'].map(lambda x: str(int(x)) + 'cont') + merged['CONTROLES'].map(lambda x: str(int(x)) + 'trat'))

# print(merged['bivar_code'])

# Define a simple bivariate colormap
bivar_colors = {
    '0cont0trat': '#E8E8E8', '1cont0trat': '#56BCC2', '0cont1trat': '#E87D72',
}


merged['color'] = merged['bivar_code'].map(bivar_colors)


# Plot
fig, ax = plt.subplots(1, 1, figsize=(8, 8))

# Base map (all municipalities)
merged.plot(
    color=merged['color'],   # your custom fill colors
    edgecolor='dimgray',     # border color (any valid Matplotlib color)
    linewidth=0.25,           # optional: control thickness of borders
    ax=ax
)

# Add hatched layer for downstream municipalities
merged[merged['DOWNSTREAM'] == 1].plot(
    facecolor="none",           # keep base color visible underneath
    edgecolor="black",          # optional outline
    hatch="////",               # hatch pattern (e.g. /, \, x, o, etc.)
    linewidth=0.5,
    ax=ax
)

rio_paraopeba.plot(ax=ax, color='blue', linewidth=1.2, label='Rio São Francisco')

# Legend
legend_elements = [
    mpatches.Patch(color='#56BCC2', label='Treated Municipalities'),
    mpatches.Patch(color='#E87D72', label='Control Municipalities'),
    mpatches.Patch(facecolor='white', edgecolor='black', hatch='///', label='Downstream Municipalities'),
    mpatches.Patch(color='blue', label='Paraopeba River')
]

# ax.set_title("GDP Synthetic Control Municipalities With Downstream (Minas Gerais State)")
plt.axis('off')
ax.legend(handles=legend_elements, loc='lower left',
          # title='Treatment and Downstream Municipalities',
          #title='Legend'
          )
# plt.show()
plt.tight_layout()
plt.savefig('Mapas_matching/pib_municipios_map.png', dpi=500, bbox_inches='tight')
# plt.savefig("pib_vectorized.pdf")

#merged.to_file('SHPS_matching/pib_municipios_shape.shp')


# no downstream
matched = pd.read_csv(os.path.join(matching_data_path, 'matching_k_nearest_no_downstream_pib.csv'))
merged = gpd.read_file(os.path.join(maps_data, 'MG_Municipios_2023.shp'))

downstream = pd.read_csv(os.path.join(matching_data_path, 'downstream_municipios.csv'))

print(merged['CD_MUN'])
print(matched['COD_MUN'])

merged.loc[merged['CD_MUN'] == '3109006', 'TRATADOS'] = 1
merged.loc[merged['CD_MUN'] != '3109006', 'TRATADOS'] = 0
merged.loc[merged['CD_MUN'].isin(matched['COD_MUN'].astype(str)), 'CONTROLES'] = 1
merged.loc[~merged['CD_MUN'].isin(matched['COD_MUN'].astype(str)), 'CONTROLES'] = 0
merged.loc[merged['CD_MUN'].isin(downstream['COD_MUN'].astype(str)), 'DOWNSTREAM'] = 1
merged.loc[~merged['CD_MUN'].isin(downstream['COD_MUN'].astype(str)), 'DOWNSTREAM'] = 0

# Combine into a bivariate code (e.g. '02', '11', etc.)
merged['bivar_code'] = (merged['TRATADOS'].map(lambda x: str(int(x)) + 'cont') + merged['CONTROLES'].map(lambda x: str(int(x)) + 'trat'))

# print(merged['bivar_code'])

# Define a simple bivariate colormap
bivar_colors = {
    '0cont0trat': '#E8E8E8', '1cont0trat': '#56BCC2', '0cont1trat': '#E87D72',
}


merged['color'] = merged['bivar_code'].map(bivar_colors)


# Plot
fig, ax = plt.subplots(1, 1, figsize=(8, 8))

# Base map (all municipalities)
merged.plot(
    color=merged['color'],   # your custom fill colors
    edgecolor='dimgray',     # border color (any valid Matplotlib color)
    linewidth=0.25,           # optional: control thickness of borders
    ax=ax
)

# Add hatched layer for downstream municipalities
merged[merged['DOWNSTREAM'] == 1].plot(
    facecolor="none",           # keep base color visible underneath
    edgecolor="black",          # optional outline
    hatch="////",               # hatch pattern (e.g. /, \, x, o, etc.)
    linewidth=0.5,
    ax=ax
)

rio_paraopeba.plot(ax=ax, color='blue', linewidth=1.2, label='Rio São Francisco')

# Legend
legend_elements = [
    mpatches.Patch(color='#56BCC2', label='Treated Municipalities'),
    mpatches.Patch(color='#E87D72', label='Control Municipalities'),
    mpatches.Patch(facecolor='white', edgecolor='black', hatch='///', label='Downstream Municipalities'),
    mpatches.Patch(color='blue', label='Paraopeba River')
]

# ax.set_title("GDP Synthetic Control Municipalities Without Downstream (Minas Gerais State)")
plt.axis('off')
ax.legend(handles=legend_elements, loc='lower left',
          # title='Treatment and Downstream Municipalities',
          #title='Legend'
          )
# plt.show()
plt.tight_layout()
plt.savefig('Mapas_matching/pib_municipios_map_no_dowsntream.png', dpi=500, bbox_inches='tight')
# plt.savefig("pib_vectorized.pdf")

#merged.to_file('SHPS_matching/pib_municipios_shapeno_dowsntream.shp')
