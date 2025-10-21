import basedosdados as bd
import pandas as pd

# df = bd.read_table(dataset_id='br_me_rais',
# table_id='microdados_vinculos',
# billing_project_id="tcc-fea")

for i in range(1, 13):
    print("run:", i)
    query = f"SELECT * FROM `basedosdados.br_me_rais.microdados_vinculos` WHERE ano=2022 AND mes_admissao = {i}"

    df = bd.read_sql(query=query,
                    billing_project_id="tcc-fea")

    df.to_csv(f"C:/Users/joaom/Downloads/emprego_dados_2022_{i}.csv")

