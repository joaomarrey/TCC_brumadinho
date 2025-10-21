import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
#
# x = np.array([0,1]).reshape(-1, 1)
# y = np.array([3,2])
#
# model = LinearRegression(fit_intercept=False)
# model.fit(x, y)
#
# print(model.coef_)
#
# x = np.array([[0,1],[1,0]])
#
# model = LinearRegression(fit_intercept=False)
# model.fit(x, y)
#
# print(model.coef_)


# 1. Sample Data (mimicking your situation with missing months)
data = {'municipality': ['A', 'A', 'A', 'B', 'B', 'B'],
        'year':         [2022, 2022, 2023, 2022, 2022, 2022],
        'month':        [1, 3, 2, 10, 11, 12], # A is missing month 2 in 2022
        'wage':         [1000, 1100, 1050, 2000, 2100, 2050]}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# 2. Set the current index to prepare for reindexing
df = df.set_index(['municipality', 'year', 'month'])

# 3. Create the complete MultiIndex
municipalities = df.index.get_level_values('municipality').unique()
years = df.index.get_level_values('year').unique()
months = range(1, 13) # Full range of months

new_index = pd.MultiIndex.from_product(
    [municipalities, years, months],
    names=['municipality', 'year', 'month']
)

# 4. Reindex the DataFrame and get the columns back
df_complete = df.reindex(new_index)
df_complete = df_complete.reset_index()

print("\nComplete DataFrame with missing months added:")
print(df_complete.sort_values(by=['municipality', 'year', 'month']))

# You can then fill the NaN values if needed, for example with forward-fill
df_complete['wage'] = df_complete['wage'].fillna(0)
print(df_complete)
