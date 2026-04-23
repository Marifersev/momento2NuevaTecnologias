import pandas as pd

def carga_usuario():
    df = pd.read_csv('data/raw/Usuario.csv')
    return df

def carga_gasto():
    df = pd.read_csv('data/raw/Gasto.csv')
    return df

def carga_categoria():
    df = pd.read_csv('data/raw/Categoria.csv')
    return df

def carga_comercio():
    df = pd.read_csv('data/raw/Comercio.csv')
    return df

def carga_medio_de_pago():
    df = pd.read_csv('data/raw/MedioPago.csv')
    return df