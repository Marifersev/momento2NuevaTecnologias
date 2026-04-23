from src.carga import (
    carga_usuario,
    carga_gasto,
    carga_categoria,
    carga_comercio,
    carga_medio_de_pago
)

from src.limpieza import ejecutar_limpieza
from src.merge import merge
from src.analisis import ejecutar_analisis

print("===== INICIO DEL PROYECTO =====")

# 1. CARGA DE DATOS SUCIOS
print("\n1. Cargando datos...")
usuarios = carga_usuario()
gastos = carga_gasto()
categorias = carga_categoria()
comercios = carga_comercio()
pagos = carga_medio_de_pago()

# 2. LIMPIEZA
print("\n2. Ejecutando limpieza...")
ejecutar_limpieza()

# 3. MERGE
print("\n3. Creando dataset unificado...")
gastos_merge = merge()

# 4. ANÁLISIS
print("\n4. Ejecutando análisis...")
ejecutar_analisis()

print("\n===== PROCESO TERMINADO =====")

