import pandas as pd

df = pd.read_excel("PIB dos Municípios - base de dados 2010-2021.xlsx")

print(df)
print(df.columns)

df_filtered = df[["Ano", "Código do Município", "Nome do Município", "Nome da Unidade da Federação",
                  "Valor adicionado bruto da Agropecuária, a preços correntes (R$ 1.000)",
                  "Valor adicionado bruto da Indústria, a preços correntes (R$ 1.000)",
                  "Valor adicionado bruto dos Serviços, a preços correntes - exceto Administração, defesa, educação e saúde públicas e seguridade social (R$ 1.000)",
                  "Valor adicionado bruto da Administração, defesa, educação e saúde públicas e seguridade social, a preços correntes (R$ 1.000)",
                  "Valor adicionado bruto total, a preços correntes (R$ 1.000)",
                  "Impostos, líquidos de subsídios, sobre produtos, a preços correntes (R$ 1.000)",
                  "Produto Interno Bruto, a preços correntes (R$ 1.000)",
                  "Produto Interno Bruto per capita, a preços correntes (R$ 1,00)"
                  ]]

df_filtered = df_filtered[(df_filtered["Nome da Unidade da Federação"] == "Minas Gerais") & (df_filtered["Ano"] >= 2015)]

df_filtered.rename({"Código do Município": "Codigo do Municipio", "Nome do Município": "Nome do Municipio",
                  "Nome da Unidade da Federação": "Nome da Unidade da Federacao",
                  "Valor adicionado bruto da Agropecuária, a preços correntes (R$ 1.000)": "Valor adicionado bruto da Agropecuaria (1000)",
                  "Valor adicionado bruto da Indústria, a preços correntes (R$ 1.000)": "Valor adicionado bruto da Industria (1000)",
                  "Valor adicionado bruto dos Serviços, a preços correntes - exceto Administração, defesa, educação e saúde públicas e seguridade social (R$ 1.000)": "Valor adicionado bruto dos Serviços (1000)",
                  "Valor adicionado bruto da Administração, defesa, educação e saúde públicas e seguridade social, a preços correntes (R$ 1.000)": "Valor adicionado bruto da Adm (1000)",
                  "Valor adicionado bruto total, a preços correntes (R$ 1.000)": "Valor adicionado bruto total (1000)",
                  "Impostos, líquidos de subsídios, sobre produtos, a preços correntes (R$ 1.000)": "Impostos, liq de Subsidios, sobre produtos (1000)",
                  "Produto Interno Bruto, a preços correntes (R$ 1.000)": "PIB (1000)",
                  "Produto Interno Bruto per capita, a preços correntes (R$ 1,00)": "PIB per Capita (1)"},
                   axis="columns",
                   inplace=True)

print(df_filtered)

df_filtered.to_csv("pib_per_capita_mun.csv", index=False)