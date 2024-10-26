import pandas as pd
import random

def df_universidades():
    df = pd.read_csv("ranking_folha_univ.csv", delimiter=';')
    df = df[["Universidade", "Estado", "Pública ou Privada", "Nota em Ensino", "Nota em Pesquisa", "Nota em Mercado",
             "Nota em Inovação"]]
    ids = random.sample(range(1, 204), len(df))
    df["Código MEC"] = ids

    with open("universidades_sql.txt", "w", encoding="utf-8") as f:
        for _, linha in df.iterrows():
            sql = f"INSERT INTO IES (Código MEC, Nome, Estado, Tipo, Nota Ensino, Nota Pesquisa, Nota Mercado, " \
                  f"Nota Inovação) VALUES ('{linha['Código MEC']},{linha['Universidade']},{linha['Estado']},{linha['Pública ou Privada']},{linha['Nota em Ensino']},{linha['Nota em Pesquisa']},{linha['Nota em Mercado']}',{linha['Nota em Inovação']});\n "
            f.write(sql)
    return df


df_universidades()
