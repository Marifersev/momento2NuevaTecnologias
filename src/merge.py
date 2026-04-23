import pandas as pd

def merge():
    usuarios = pd.read_csv("data/processed/Usuario_limpio.csv")
    gastos = pd.read_csv("data/processed/Gastos_limpio.csv")
    categorias = pd.read_csv("data/processed/Categorias_limpio.csv")
    comercios = pd.read_csv("data/processed/Comercios_limpio.csv")
    gastos_merge = gastos.merge(usuarios, on="id_usuario", how="left") \
                .merge(comercios, on="id_comercio", how="left") \
                .merge(categorias, on="id_categoria", how="left")
    gastos_merge.to_csv('data/processed/Gastos_merge.csv', index=False)
    return gastos_merge

merge()