import numpy as np
import pandas as pd

# 1. Configurar semilla y parámetros para todo el trimestre Q1 (Enero - Marzo 2025)
np.random.seed(42)
n_total = 500  # Total de registros robustos para el portafolio

# Generar fechas distribuidas a lo largo de todo el trimestre
fechas = pd.date_range(start='2025-01-01', end='2025-03-31', periods=n_total)
clientes = [
    'Carlos Pérez',
    'Carmen Ortiz',
    'Ana Gómez',
    'Pedro Rodríguez',
    'Luis Soto',
    'Jorge Mendoza',
    'Sofía Castro',
    'María Silva',
]
tipos_poliza = ['Vida', 'Automóvil', 'Hogar', 'Salud', None]

# 2. Construir el DataFrame base
data = {
    'ID_Cliente': [
        f'CLI-{np.random.randint(1000, 9999)}' for _ in range(n_total)
    ],
    'Nombre_Cliente': np.random.choice(clientes, n_total),
    'Tipo_Poliza': np.random.choice(
        tipos_poliza, n_total, p=[0.25, 0.25, 0.22, 0.22, 0.06]
    ),
    'Fecha_Registro': fechas,
    'Prima_Pagada': np.random.uniform(80000, 350000, n_total).round(2),
}

df_final = pd.DataFrame(data)

# 3. Calcular costos de siniestros y ratios financieros
df_final['Costo_Siniestro'] = (
    df_final['Prima_Pagada'] * np.random.uniform(0.3, 0.95, n_total)
).round(2)
df_final['Ratio_Siniestralidad'] = (
    df_final['Costo_Siniestro'] / df_final['Prima_Pagada']
).round(4)


def clasificar_riesgo(ratio):
  if pd.isna(ratio) or ratio == 0:
    return 'Sin Siniestro'
  elif ratio > 0.8:
    return 'Alto Riesgo (Déficit)'
  elif ratio >= 0.5:
    return 'Riesgo Moderado'
  else:
    return 'Bajo Riesgo (Rentable)'


df_final['Categoria_Riesgo'] = df_final['Ratio_Siniestralidad'].apply(
    clasificar_riesgo
)

# 4. Saneamiento final: rellenar valores nulos de póliza como 'No Definida'
df_final['Tipo_Poliza'] = df_final['Tipo_Poliza'].fillna('No Definida')

# 5. Guardar el nuevo archivo maestro limpio para Power BI
archivo_salida = 'datos_limpios_seguros_q1.csv'
df_final.to_csv(archivo_salida, index=False, encoding='utf-8-sig')

print(
    f'¡Archivo maestro generado con éxito: {archivo_salida}! Total de'
    f' registros: {len(df_final)}'
)