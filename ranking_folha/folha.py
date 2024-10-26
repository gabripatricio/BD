import pandas as pd

def df_universidades():
    df = pd.read_csv("ranking_folha_univ.csv", delimiter=';')
    df = df[["Universidade", "Estado", "Pública ou Privada", "Nota em Ensino", "Nota em Pesquisa", "Nota em Mercado",
             "Nota em Inovação"]]
    #print(df)
    return df
