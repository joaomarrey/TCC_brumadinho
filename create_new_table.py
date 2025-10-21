import pandas as pd
import numpy as np
import os

cods = pd.read_excel("./codigos_pop_municipios.xlsx")

cods["pop"] = cods["POPULAÇÃO ESTIMADA"].astype("string").map(lambda x:  x[:x.index("(")].replace(".", "") if "." in x else x).astype("int")

cods.rename({"CODIGO RAIS": "id_municipio"}, axis=1, inplace=True)

# print(cods)

# cods_list = list(cods.loc[cods["pop"] >= 100000, "CODIGO RAIS"])

new_df = None


for i in range(1, 13):
    print(f"start {i}")
    old_df = pd.read_csv(f"C:/Users/joaom/Downloads/emprego_dados_2022_{i}.csv")

    old_df = old_df[["id_municipio", "valor_remuneracao_media", "grau_instrucao_apos_2005"]]

    df = old_df.copy()
    # print(df["grau_instrucao_apos_2005"].dtype)
    df.loc[old_df["grau_instrucao_apos_2005"]==1, "grau_instrucao_apos_2005"] = 0
    df.loc[old_df["grau_instrucao_apos_2005"]==2, "grau_instrucao_apos_2005"] = 1
    df.loc[old_df["grau_instrucao_apos_2005"]==3, "grau_instrucao_apos_2005"] = 5
    df.loc[old_df["grau_instrucao_apos_2005"]==4, "grau_instrucao_apos_2005"] = 6
    df.loc[old_df["grau_instrucao_apos_2005"]==5, "grau_instrucao_apos_2005"] = 9
    df.loc[old_df["grau_instrucao_apos_2005"]==6, "grau_instrucao_apos_2005"] = 10
    df.loc[old_df["grau_instrucao_apos_2005"]==7, "grau_instrucao_apos_2005"] = 12
    df.loc[old_df["grau_instrucao_apos_2005"]==8, "grau_instrucao_apos_2005"] = 13
    df.loc[old_df["grau_instrucao_apos_2005"]==9, "grau_instrucao_apos_2005"] = 17
    df.loc[old_df["grau_instrucao_apos_2005"]==10, "grau_instrucao_apos_2005"] = 19
    df.loc[old_df["grau_instrucao_apos_2005"]==11, "grau_instrucao_apos_2005"] = 21
    df.loc[old_df["grau_instrucao_apos_2005"]==-1, "grau_instrucao_apos_2005"] = np.nan

    df.dropna()

    # df = df[df["id_municipio"].isin(cods_list)]

    if new_df is not None:
        new_df = pd.concat([new_df, df])
    else:
        new_df = df

    print(f"end {i}")

# new_df = new_df.groupby(by=["id_municipio"])[["valor_remuneracao_media", "grau_instrucao_apos_2005"]].std().dropna()

# os.path.join(os.curdir)
# new_df.to_csv("./test_rais_sd_fixed_all_months.csv")

new_df = pd.merge(new_df, cods, how="left", on="id_municipio")

new_df.to_csv("agraggate_data_all_months.csv")
