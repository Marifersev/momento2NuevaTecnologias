import pandas as pd

usuarios = pd.read_csv("data/processed/Usuario_limpio.csv")
gastos = pd.read_csv("data/processed/Gastos_limpio.csv")
categorias = pd.read_csv("data/processed/Categorias_limpio.csv")
comercios = pd.read_csv("data/processed/Comercios_limpio.csv")
pagos = pd.read_csv("data/processed/Pagos_limpio.csv")

def ejecutar_analisis():
    # =========================
    # 1. ANÁLISIS DE FRECUENCIA
    # =========================
    print("===== ANÁLISIS DE FRECUENCIA =====")

    # Usuario con más registros
    usuario_frecuente = usuarios["nombre"].value_counts().head(1)
    print("Usuario con más registros:")
    print(usuario_frecuente)

    # Comercio con más gastos
    comercio_frecuente = gastos["id_comercio"].value_counts().head(1)
    print("Comercio con más transacciones (ID):")
    print(comercio_frecuente)


    # =========================
    # 2. ANÁLISIS DE AGREGACIÓN
    # =========================
    print("===== ANÁLISIS DE AGREGACIÓN =====")

    # Total gastado por usuario
    gasto_por_usuario = gastos.groupby("id_usuario")["valor"].sum()
    print("Total gastado por usuario:")
    print(gasto_por_usuario)

    # Total gastado por categoría
    gasto_por_categoria = gastos.groupby("id_categoria")["valor"].sum()
    print("Total gastado por categoría:")
    print(gasto_por_categoria)

    # Promedio de gasto
    promedio_gasto = gastos["valor"].mean()
    print("Promedio de gasto:")
    print(promedio_gasto)


    # =========================
    # 3. ANÁLISIS CON FILTRO Y CONTEO
    # =========================
    print("===== ANÁLISIS FILTRADO =====")

    # Gastos mayores a 50.000
    gastos_altos = gastos[gastos["valor"] > 50000]
    print("Cantidad de gastos mayores a 50.000:")
    print(len(gastos_altos))

    # Usuarios sin correo válido
    usuarios_sin_correo = usuarios[usuarios["correo"].isna()]
    print("Usuarios sin correo:")
    print(len(usuarios_sin_correo))

    # Pagos activos
    pagos_activos = pagos[pagos["estado"] == "activo"]
    print("Cantidad de pagos activos:")
    print(len(pagos_activos))

    # Gastos sin descripción (si aún existe alguno)
    gastos_sin_desc = gastos[gastos["descripcion"].isna()]
    print("Gastos sin descripción:")
    print(len(gastos_sin_desc))


    # =========================
    # RESULTADOS EXTRA 
    # =========================
    print("===== TOP RESÚMENES =====")

    print("Top 3 usuarios con más gastos:")
    print(gastos.groupby("id_usuario")["valor"].sum().sort_values(ascending=False).head(3))

    print("Top 3 categorías con más gasto:")
    print(gastos.groupby("id_categoria")["valor"].sum().sort_values(ascending=False).head(3))
    return ejecutar_analisis