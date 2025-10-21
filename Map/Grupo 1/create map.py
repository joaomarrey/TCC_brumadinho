import geopandas as gpd
# import pandas as pd
# import os
import matplotlib
matplotlib.use('Agg')  # Non-GUI backend
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


merged = gpd.read_file('Municipios_grupo1.shp')

# Combine into a bivariate code (e.g. '02', '11', etc.)
merged['bivar_code'] = (merged['G1_CONT'].map(lambda x: str(int(x)) + 'cont') + merged['G1_TRAT'].map(lambda x: str(int(x)) + 'trat'))

# print(merged['bivar_code'])

# Define a simple bivariate colormap
bivar_colors = {
    '0cont0trat': '#E8E8E8', '1cont0trat': '#56BCC2', '0cont1trat': '#E87D72',
}

# Define your bivariate legend
legend_elements = [
    # mpatches.Patch(color='#E8E8E8', label='Low Income, Low Education'),
    mpatches.Patch(color='#56BCC2', label='Control Municipalities'),
    mpatches.Patch(color='#E87D72', label='Treated Municipalities'),
]

merged['color'] = merged['bivar_code'].map(bivar_colors)


# Plot
fig, ax = plt.subplots(1, 1, figsize=(8, 8))
merged.plot(
    color=merged['color'],   # your custom fill colors
    edgecolor='dimgray',     # border color (any valid Matplotlib color)
    linewidth=0.25,           # optional: control thickness of borders
    ax=ax
)
ax.set_title("Group 1 Municipalities (Minas Gerais State)")
plt.axis('off')
ax.legend(handles=legend_elements, loc='lower left', title='Control and Treatment Groups')
# plt.show()
plt.tight_layout()
plt.savefig('group1.png', dpi=500, bbox_inches='tight')
plt.savefig("group1_vectorized.pdf")
