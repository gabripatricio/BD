import pandas as pd
import random

def df_universidades():
    df = pd.read_csv("ranking_folha_univ.csv", delimiter=';')
    df = df[["Universidade", "Estado", "Pública ou Privada", "Nota em Ensino", "Nota em Internacionalização", "Nota em Mercado",
             "Nota em Inovação"]]
    ids = random.sample(range(1, 204), len(df))
    df["Código MEC"] = ids

    with open("inserts_universidades.txt", "w", encoding="utf-8") as f:
        for _, linha in df.iterrows():
            sql = f"INSERT INTO ies (codigoemecies, nome, tipo, notaensinoruf,notrufinovacao, notarufmercado, " \
                  f"notarufinternacionalizacao)" f"VALUES ('{linha['Código MEC']},{linha['Universidade']},{linha['Pública ou Privada']},{linha['Nota em Ensino']},{linha['Nota em Inovação']},{linha['Nota em Mercado']}',{linha['Nota em Internacionalização']});\n "
            f.write(sql)
    return df


df_universidades()
