import geopandas as gpd
import os
import matplotlib
import pandas as pd
from shapely.geometry import Point

matplotlib.use('Agg')  # Non-GUI backend
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from paths import matching_data_path, maps_data


# with downstream
# matched = pd.read_csv(os.path.join(matching_data_path, 'matching_k_nearest.csv'))
merged = gpd.read_file(os.path.join(maps_data, 'MG_Municipios_2023.shp'))

downstream = pd.read_csv(os.path.join(matching_data_path, 'downstream_municipios.csv'))

rio_paraopeba = gpd.read_file('Rio_Paraopeba/rio_paraopeba.shp')

print(merged['CD_MUN'])
# print(matched['COD_MUN'])


merged.loc[merged['CD_MUN'].isin(downstream['COD_MUN'].astype(str)), 'DOWNSTREAM'] = 1
merged.loc[~merged['CD_MUN'].isin(downstream['COD_MUN'].astype(str)), 'DOWNSTREAM'] = 0


# # Define a simple bivariate colormap
# bivar_colors = {
#     '0cont0trat': '#E8E8E8', '1cont0trat': '#56BCC2', '0cont1trat': '#E87D72',
# }


merged['color'] = '#E8E8E8'

# dam
dam_location = Point(-44.1176231054265, -20.118366261569832)
dam_gdf = gpd.GeoDataFrame({'name': ['Main Dam']}, geometry=[dam_location], crs=merged.crs)

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

rio_paraopeba.plot(ax=ax, color='blue', linewidth=1.2, label='Paraopeba River')

dam_gdf.plot(ax=ax, color='gold', marker='*', markersize=250, label='Córrego do Feijão Dam', zorder=5,
             edgecolor='black',  # solid black border
             linewidth=0.8,
             )

# Legend
legend_elements = [
    mpatches.Patch(facecolor='white', edgecolor='black', hatch='///', label='Downstream Municipalities'),
    mpatches.Patch(color='blue', label='Paraopeba River'),
    plt.Line2D([0], [0], marker='*',
                color='black',             # border color
                markerfacecolor='gold',    # fill color
                markeredgewidth=0.8,       # border thickness
                label='Córrego do Feijão Dam',
                markersize=15,
                linestyle='None')
]


ax.set_title("Municipalities Affected and Paraopeba River (Minas Gerais State)")
plt.axis('off')
ax.legend(handles=legend_elements, loc='lower left',
          # title='River and Downstream Municipalities'
          )
# plt.show()
plt.tight_layout()
plt.savefig('municipios_afetados_e_rio_map.png', dpi=500, bbox_inches='tight')
