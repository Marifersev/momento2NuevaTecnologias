import pandas as pd

def carga_usuario():
    df_usuario = pd.read_csv('data/raw/Usuario.csv')
    df_usuario.info()
    print(df_usuario.head())
    return df_usuario

def carga_gasto():
    df_gasto = pd.read_csv('data/raw/Gasto.csv')
    df_gasto.info()
    print(df_gasto.head())
    return df_gasto

def carga_categoria():
    df_categoria = pd.read_csv('data/raw/Categoria.csv')
    df_categoria.info()
    print(df_categoria .head())
    return df_categoria

def carga_comercio():
    df_comercio = pd.read_csv('data/raw/Comercio.csv')
    df_comercio.info()
    print(df_comercio.head())
    return df_comercio

def carga_medio_de_pago():
    df_medio_de_pago = pd.read_csv('data/raw/MedioPago.csv')
    df_medio_de_pago.info()
    print(df_medio_de_pago.head())
    return df_medio_de_pago

if __name__ == "__main__":
    carga_usuario()
    carga_gasto()
    carga_categoria()
    carga_comercio()
    carga_medio_de_pago()