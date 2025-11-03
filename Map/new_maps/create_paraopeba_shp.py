import geopandas as gpd
import matplotlib.pyplot as plt
# from paths import

river = gpd.read_file('Rio_Paraopeba/bacia_rio_paraopeba.shp')

# See the first few rows
print(river.head())

# Check all available columns
print(river.columns)

# Check coordinate reference system (CRS)
print('#########')
print(river.crs)
print('#########')

# Basic info (geometry type, number of features, etc.)
print(river.info())


pib = gpd.read_file("PIB/pib_municipios_shape.shp")

# See the first few rows
print(pib.head())

# Check all available columns
print(pib.columns)

# Check coordinate reference system (CRS)
print('#########')
print(pib.crs)
print('#########')

# Basic info (geometry type, number of features, etc.)
print(pib.info())


river.plot()
plt.savefig('Mapa_Rio/bacia_paraopeba.png')


# print(list(river['noriocomp']))

rio_paraopeba = river[river['noriocomp'] == 'Rio Paraopeba']
rio_paraopeba.plot()
plt.savefig('Mapa_Rio/paraopeba.png')

rio_paraopeba = rio_paraopeba.to_crs(pib.crs)
rio_paraopeba.plot()
# plt.savefig('paraopeba2.png')

rio_paraopeba.to_file('Rio_Paraopeba/rio_paraopeba.shp')

