# Credit Scoring Model

Este proyecto desarrolla un modelo de **riesgo crediticio** capaz de predecir la probabilidad de que un cliente incurra en **mora severa (2 años)** usando el dataset *CreditScoring.csv*.  
Incluye un pipeline completo de limpieza, análisis, modelamiento y exportación del modelo final para uso en aplicaciones web.

---

## Objetivo del Proyecto  
Construir un modelo predictivo que permita identificar clientes con alta probabilidad de caer en default, apoyando la toma de decisiones en procesos de otorgamiento de crédito y mitigación de riesgo financiero.

---

## 🔧 Tecnologías Utilizadas  
- Python 3.10+  
- Pandas / NumPy  
- Matplotlib / Seaborn  
- Scikit-Learn  
- Imbalanced-Learn (SMOTE)  
- YData-Profiling  
- Joblib  
- FastAPI / Uvicorn (para despliegue opcional)

---
Guía de Ejecución del Proyecto

1. Ejecución del Notebook

Pasos para ejecutarlo

Instalar las dependencias

pip install -r requirements.txt

Abre el archivo:

07_EntidadFinanciera.ipynb


Ejecuta las celdas en orden con Run All o usando Shift+Enter.

El notebook guardará automáticamente en la carpeta /Models:

final_model.pkl      → modelo final (Regresión Logística optimizado)
scaler.pkl           → escalador MinMax
columns.pkl          → columnas esperadas por el modelo

🌐 2. Ejecución de la Web-App con Flask

La aplicación web permite ingresar datos manualmente y obtener:

Predicción del modelo

Probabilidad de default

Categoría de riesgo (BAJO / ALTO)

Cómo correr la web-app

Abrir la terminal en la carpeta:

cd web-app


Instala Flask (si no está instalado):

pip install flask


Ejecuta la aplicación:

python app.py


Abre en tu navegador:

👉 http://127.0.0.1:5000/

o
👉 http://localhost:5000/

✔ Predicción

Ingresa los valores solicitados en el formulario y presiona Predecir.
La página mostrará:

El resultado:
BAJO RIESGO (No Default) o ALTO RIESGO (Default)

La probabilidad de default expresada en porcentaje.

Algunos ejemplos son:
- Alto Riesgo:
  
| Variable                             | Valor    |
| ------------------------------------ | -------- |
| RevolvingUtilizationOfUnsecuredLines | **0.90** |
| age                                  | **28**   |
| NumberOfTime30-59DaysPastDueNotWorse | **3**    |
| DebtRatio                            | **1.50** |
| MonthlyIncome                        | **1800** |
| NumberOfOpenCreditLinesAndLoans      | **12**   |
| NumberOfTimes90DaysLate              | **2**    |
| NumberRealEstateLoansOrLines         | **0**    |
| NumberOfTime60-89DaysPastDueNotWorse | **1**    |
| NumberOfDependents                   | **3**    |


- Bajo Riesgo:
  
| Variable                             | Valor    |
| ------------------------------------ | -------- |
| RevolvingUtilizationOfUnsecuredLines | **0.18** |
| age                                  | **45**   |
| NumberOfTime30-59DaysPastDueNotWorse | **0**    |
| DebtRatio                            | **0.30** |
| MonthlyIncome                        | **5500** |
| NumberOfOpenCreditLinesAndLoans      | **8**    |
| NumberOfTimes90DaysLate              | **0**    |
| NumberRealEstateLoansOrLines         | **1**    |
| NumberOfTime60-89DaysPastDueNotWorse | **0**    |
| NumberOfDependents                   | **2**    |
