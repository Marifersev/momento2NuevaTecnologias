import pandas as pd
import numpy as np

from src.carga import (
    carga_usuario,
    carga_gasto,
    carga_categoria,
    carga_comercio,
    carga_medio_de_pago
)

def ejecutar_limpieza():
    # =========================
    # CARGA DE DATOS
    # =========================
    usuarios = carga_usuario()
    gastos = carga_gasto()
    categorias = carga_categoria()
    comercios = carga_comercio()
    pagos = carga_medio_de_pago()

    # =========================
    # FUNCIONES GENERALES
    # =========================
    def limpiar_texto(df):
        for col in df.select_dtypes(include="object").columns:
            df[col] = df[col].astype(str).str.strip().str.lower()
        return df


    def reemplazar_vacios(df):
        return df.replace(["", " ", "nan", "None", "null"], np.nan)

    # =========================
    # LIMPIEZA USUARIOS
    # =========================
    print("===== LIMPIEZA USUARIOS =====")

    usuarios = limpiar_texto(usuarios)
    usuarios = reemplazar_vacios(usuarios)

    print("Limpieza de espacios y formato")

    usuarios["nombre"] = usuarios["nombre"].str.strip().str.title()
    usuarios["correo"] = usuarios["correo"].str.strip()
    usuarios["telefono"] = usuarios["telefono"].str.strip()

    print("Eliminar duplicados")
    usuarios = usuarios.drop_duplicates()

    print("Tratamiento de correos inválidos")
    usuarios.loc[~usuarios["correo"].str.contains("@", na=False), "correo"] = np.nan

    print("Limpieza de teléfonos")
    usuarios["telefono"] = usuarios["telefono"].fillna(0)
    usuarios["telefono"] = usuarios["telefono"].astype(str).str.strip()
    print("Resultado final usuarios")

    print("Eliminar usuarios incompletos")

    usuarios = usuarios.dropna(subset=[
        "nombre",
        "telefono",
        "correo",
        "documento"
    ])

    usuarios.info()

    # =========================
    # LIMPIEZA PAGOS
    # =========================
    print("===== LIMPIEZA PAGOS =====")

    pagos = limpiar_texto(pagos)
    pagos = reemplazar_vacios(pagos)

    print("Normalizando franquicia")
    pagos["franquicia"] = pagos["franquicia"].str.strip().str.lower()

    print("Normalizando estado")
    pagos["estado"] = pagos["estado"].str.strip().str.lower()

    print("Eliminar estados inválidos")
    pagos.loc[~pagos["estado"].isin(["activo", "inactivo"]), "estado"] = np.nan

    print("Eliminar pagos incompletos")

    pagos = pagos.dropna(subset=[
        "nombre",
        "franquicia",
        "estado"
    ])

    pagos.info()

    # =========================
    # LIMPIEZA GASTOS
    # =========================
    print("===== LIMPIEZA GASTOS =====")

    gastos = limpiar_texto(gastos)
    gastos = reemplazar_vacios(gastos)

    print("Limpieza de fechas")
    gastos["fecha"] = pd.to_datetime(gastos["fecha"], errors="coerce")

    print("Limpieza de valores monetarios")
    gastos["valor"] = gastos["valor"].astype(str).str.replace(r"[$,]", "", regex=True)
    gastos["valor"] = pd.to_numeric(gastos["valor"], errors="coerce")

    print("Limpieza de descripción")
    gastos["descripcion"] = gastos["descripcion"].str.strip()

    print("Eliminar registros sin valor")
    gastos = gastos.dropna(subset=["valor"])

    print("Eliminar gastos incompletos")

    gastos = gastos.dropna(subset=[
        "id_usuario",
        "id_pago",
        "id_comercio",
        "id_categoria",
        "fecha",
        "valor",
        "descripcion"
    ])

    gastos.info()

    # =========================
    # LIMPIEZA COMERCIOS
    # =========================
    print("===== LIMPIEZA COMERCIOS =====")

    comercios = limpiar_texto(comercios)
    comercios = reemplazar_vacios(comercios)

    print("Formato título en nombres")
    comercios["nombre"] = comercios["nombre"].str.strip().str.title()

    print("Eliminar duplicados")
    comercios = comercios.drop_duplicates()

    print("Eliminar comercios incompletos")

    comercios = comercios.dropna(subset=[
        "nit",
        "nombre",
        "tipo_comercio"
    ])

    comercios.info()

    # =========================
    # LIMPIEZA CATEGORÍAS
    # =========================
    print("===== LIMPIEZA CATEGORÍAS =====")

    categorias = limpiar_texto(categorias)
    categorias = reemplazar_vacios(categorias)

    print("Normalizando nombres")
    categorias["nombre"] = categorias["nombre"].str.strip().str.lower()

    print("Tratamiento de fechas")
    categorias["fecha_creacion"] = pd.to_datetime(categorias["fecha_creacion"], errors="coerce")

    print("Normalizando responsable")
    categorias["responsable"] = categorias["responsable"].str.strip().str.upper()

    print("Eliminar categorías incompletas")

    categorias = categorias.dropna(subset=[
        "nombre",
        "fecha_creacion",
        "responsable",
        "justificacion"
    ])

    categorias.info()

    # =========================
    # VALIDACIONES ÚTILES
    # =========================

    # usuarios sin correo
    usuarios_sin_correo = usuarios[usuarios["correo"].isna()]

    # gastos sin valor
    gastos_sin_valor = gastos[gastos["valor"].isna()]

    # claves foráneas inválidas
    gastos_invalidos = gastos[
        ~gastos["id_usuario"].isin(usuarios["id_usuario"])
    ]

    # =========================
    # EXPORTAR LIMPIO
    # =========================
    usuarios.to_csv("data/processed/Usuario_limpio.csv", index=False)
    pagos.to_csv("data/processed/Pagos_limpio.csv", index=False)
    gastos.to_csv("data/processed/Gastos_limpio.csv", index=False)
    comercios.to_csv("data/processed/Comercios_limpio.csv", index=False)
    categorias.to_csv("data/processed/Categorias_limpio.csv", index=False)
    return ejecutar_limpieza