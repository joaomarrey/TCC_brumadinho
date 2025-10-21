# import pandas as pd

# cods = pd.read_excel("./codigos_pop_municipios.xlsx")

# cods["pop"] = cods["POPULAÇÃO ESTIMADA"].astype("string").map(lambda x:  x[:x.index("(")].replace(".", "") if "." in x else x).astype("int")

# print(cods.iloc[16,:])

# cods = list(cods.loc[cods["pop"] >= 200000, "CODIGO RAIS"])

# print(cods)
# print(len(cods))

# # a = "548.952"

# # print(a.replace(".", ""))

a = "a"

print(a.replace("b", ""))
