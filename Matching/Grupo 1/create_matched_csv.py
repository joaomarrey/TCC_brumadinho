import xlwings as xw
import pandas as pd

# Open workbook and select sheet
wb = xw.Book('Brumadinho Matching.xlsx')   # or xw.Book.caller() if running from Excel
sheet = wb.sheets['Brumadinho']      # change to your actual sheet name

# Read headers from row 3
headers = sheet.range('DN3:DP3').value

# Read data from row 4 downward
data = sheet.range('DN4:DP855').options(ndim=2).value

# Convert to DataFrame
df = pd.DataFrame(data, columns=headers)

df_add = pd.DataFrame({'Nome': 'Brumadinho', 'Codigo': '310900'}, index=[852])

print(df_add)

df = pd.concat([df, df_add], axis=0)

df.loc[df["Grupo 1 controle"] != 1, "Grupo 1 controle"] = 0

df['Grupo 1 tratamento'] = 0

df.loc[df['Nome'] == 'Brumadinho', 'Grupo 1 tratamento'] = 1

print(df)

# # Drop completely empty rows (optional)
# df.dropna(how='all', inplace=True)

print(df.head())

df.to_csv("Matched_Grupo1.csv")