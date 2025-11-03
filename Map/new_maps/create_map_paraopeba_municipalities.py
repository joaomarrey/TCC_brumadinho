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


# ax.set_title("Municipalities Affected and Paraopeba River (Minas Gerais State)")
plt.axis('off')
ax.legend(handles=legend_elements, loc='lower left',
          # title='River and Downstream Municipalities'
          )
# plt.show()
plt.tight_layout()
plt.savefig('Mapa_Rio/municipios_afetados_e_rio_map.png', dpi=500, bbox_inches='tight')



##############
# # --- Build a second, zoomed-in map around the dam ---
# zoom_factor = 0.5  # adjust how tight the zoom is (smaller = tighter zoom)
#
# # Get dam coordinates
# dam_x, dam_y = dam_location.x, dam_location.y
#
# # Compute zoom box limits
# x_min, x_max = dam_x - zoom_factor, dam_x + zoom_factor
# y_min, y_max = dam_y - zoom_factor, dam_y + zoom_factor
#
# # Create new figure
# fig2, ax2 = plt.subplots(1, 1, figsize=(6, 6))
#
# # Plot the same base map layers
# merged.plot(
#     color=merged['color'],
#     edgecolor='dimgray',
#     linewidth=0.25,
#     ax=ax2
# )
#
# # Hatched downstream municipalities
# merged[merged['DOWNSTREAM'] == 1].plot(
#     facecolor="none",
#     edgecolor="black",
#     hatch="////",
#     linewidth=0.5,
#     ax=ax2
# )
#
# # Add river
# rio_paraopeba.plot(ax=ax2, color='blue', linewidth=1.2)
#
# # Add dam marker
# dam_gdf.plot(
#     ax=ax2,
#     color='gold',
#     marker='*',
#     markersize=250,
#     edgecolor='black',
#     linewidth=0.8,
#     zorder=5
# )
#
# # Set zoomed-in limits
# ax2.set_xlim(x_min, x_max)
# ax2.set_ylim(y_min, y_max)
#
# # Aesthetics
# plt.axis('off')
# ax2.set_title("Zoom on Córrego do Feijão Dam and Surrounding Area", fontsize=10)
# plt.tight_layout()
#
# # Save
# plt.savefig('Mapa_Rio/dam_zoom_map.png', dpi=500, bbox_inches='tight')



#############
# --- Build a second map focused on the river ---

# Get river bounding box (minx, miny, maxx, maxy)
river_bounds = rio_paraopeba.total_bounds

# Add a small margin (so it's not cut too tight)
margin = 0.1  # adjust as needed (in degrees)
x_min = river_bounds[0] - margin
y_min = river_bounds[1] - margin
x_max = river_bounds[2] + margin
y_max = river_bounds[3] + margin

# Create a new figure for the zoomed map
fig2, ax2 = plt.subplots(1, 1, figsize=(8, 6))

# Base map
merged.plot(
    color=merged['color'],
    edgecolor='dimgray',
    linewidth=0.25,
    ax=ax2
)

# Hatched downstream municipalities
merged[merged['DOWNSTREAM'] == 1].plot(
    facecolor="none",
    edgecolor="black",
    hatch="////",
    linewidth=0.5,
    ax=ax2
)

# Add river and dam
rio_paraopeba.plot(ax=ax2, color='blue', linewidth=1.2, label='Paraopeba River')
dam_gdf.plot(ax=ax2, color='gold', marker='*', markersize=250,
             edgecolor='black', linewidth=0.8, zorder=5)

# Apply zoom to show entire river
ax2.set_xlim(x_min, x_max)
ax2.set_ylim(y_min, y_max)


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

# Aesthetics
plt.axis('off')
# ax2.set_title("Paraopeba River and Downstream Municipalities", fontsize=10)
ax2.legend(handles=legend_elements, loc='lower left')
plt.tight_layout()

# Save
plt.savefig('Mapa_Rio/zoom_river_map.png', dpi=500, bbox_inches='tight')
# plt.show()