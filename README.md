# 💰 Proyecto de Análisis de Gastos en Python

Este proyecto realiza un proceso completo de limpieza de datos, unión de datasets y análisis básico sobre datos de usuarios, gastos, comercios, categorías y medios de pago.  


---

## 📁 Estructura del proyecto
Momento 2/
│
├── data/
│ ├── raw/ # Datos originales (sucios)
│ ├── processed/ # Datos limpios y transformados
│
├── src/
│ ├── carga.py # Carga de datos
│ ├── limpieza.py # Limpieza de datos
│ ├── merge.py # Unión de datasets
│ ├── analisis.py # Análisis de datos
│
├── main.py # Orquestador del proyecto


---

## ⚙️ Tecnologías usadas

- Python 3
- Pandas
- NumPy

---

## 🚀 Flujo del proyecto

El proceso se ejecuta en 4 etapas:

### 1. Carga de datos
Se leen los archivos CSV desde la carpeta `data/raw`.

### 2. Limpieza de datos
Se realiza:
- Eliminación de espacios
- Conversión a formatos consistentes
- Manejo de valores nulos
- Eliminación de registros incompletos
- Normalización de texto

### 3. Merge de datos
Se unifican los datasets usando:

- `id_usuario`
- `id_comercio`
- `id_categoria`

Resultado:
Gastos_merge.csv

---

### 4. Análisis de datos

Se realizan tres tipos de análisis:

#### 📊 Frecuencia
- Usuario con más registros
- Comercio con más transacciones

#### 📈 Agregación
- Total gastado por usuario
- Total gastado por categoría
- Promedio de gasto

#### 🔍 Filtrado
- Gastos mayores a 50.000
- Usuarios sin correo válido
- Pagos activos
- Gastos sin descripción

---

## ▶️ Cómo ejecutar el proyecto

Ejecuta el archivo principal:

```bash
python main.py

