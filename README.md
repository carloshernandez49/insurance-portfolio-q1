# insurance-portfolio-q1
Executive Business Intelligence dashboard designed to monitor loss ratio control, claims volatility, and underwriting profitability for Q1 2025.
## Data Engineering & Transformation Logic

We used Python to clean raw records, handle missing values, and split timestamps correctly before feeding the data into the business intelligence layer:

```python
import pandas as pd

# Load raw insurance dataset
df = pd.read_csv("datos_seguros_raw.csv")

# Clean and split timestamp columns to ensure proper date recognition
df['Fecha_Registro'] = pd.to_datetime(df['Timestamp_Col']).dt.date
df['Hora_Registro'] = pd.to_datetime(df['Timestamp_Col']).dt.time

# Handle nulls in critical operational fields
df['Tipo_Poliza'] = df['Tipo_Poliza'].fillna('No Definida')

# Export clean dataset for Power BI ingestion
df.to_excel("datos_limpios_seguros.xlsx", index=False)

# 2. Summary & Total Calculations (DAX / Excel Integration)
# To optimize performance and bypass conversion friction for monthly trends (January – March 2025), aggregated summary tables were established:

Resumen_Mensual_Tendencia = 
SUMMARIZE(
    datos_limpios_seguros,
    datos_limpios_seguros[Fecha_Registro],
    "Total_Primas", SUM(datos_limpios_seguros[Prima_Pagada]),
    "Total_Siniestros", SUM(datos_limpios_seguros[Costo_Siniestro]),
    "Ratio_Siniestralidad", DIVIDE(SUM(datos_limpios_seguros[Costo_Siniestro]), SUM(datos_limpios_seguros[Prima_Pagada]), 0)
)
