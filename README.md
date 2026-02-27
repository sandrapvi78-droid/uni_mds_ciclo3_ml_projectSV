# Proyecto: Predicción de Calidad de Vinos 

## 1. Descripción
Este proyecto busca predecir si un vino es de **alta o baja calidad** usando sus propiedades fisicoquímicas.

## 2. Contexto del problema
La industria vitivinícola enfrenta el desafío de mantener estándares de calidad consistentes. Evaluar la calidad del vino es un proceso fundamental para determinar su precio, posicionamiento en el mercado y aceptación del consumidor. 

Actualmente, la calidad depende de catadores expertos lo que implica procesos que consumen tiempo, recursos y evaluación sensorial que puede ser subjetiva.

## 3. Limitaciones
- La calidad está basada en evaluaciones sensoriales humanas.
- El dataset puede estar desbalanceado
- No se incluyen variables externas como marca, tipo de uva o región.

## 4. Objetivos

### 4.1 Objetivo general
Predecir la calidad de los vinos utilizando modelos de clasificación basados en sus características.

### 4.2 Objetivos específicos
- Analizar la distribución de la variable `quality`.
- Identificar variables más influyentes en la calidad del vino.
- Construir un modelo de clasificación.
- Evaluar el desempeño del modelo con métricas de precisión, recall y F1-score.

## 5. Beneficios 

- Control de calidad sin depender de catadores.
- Identificación temprana de lotes de baja calidad.
- Mayor consistencia en la calidad del producto.

## 6. Dataset: Wine Quality
### 6.1 Fuente de datos

 - **Origen**: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/wine+quality)
 - **Tipo**: Vino tinto (Vinho Verde, Portugal)
- **Muestras**: 1,143 instancias
- **Variables**: 12 variables

### 6.2 Descripción de Variables

| Variable | Tipo | Descripción | Rango Típico |
|----------|------|-------------|--------------|
| **fixed acidity** | numérica | Acidez fija (tartárica) | 4.6 - 15.9 g/dm³ |
| **volatile acidity** | numérica | Acidez volátil (acética) | 0.12 - 1.58 g/dm³ |
| **citric acid** | numérica | Ácido cítrico | 0.0 - 1.0 g/dm³ |
| **residual sugar** | numérica | Azúcar residual | 0.9 - 15.5 g/dm³ |
| **chlorides** | numérica | Cloruro de sodio | 0.012 - 0.611 g/dm³ |
| **free sulfur dioxide** | numérica | SO2 libre | 1 - 72 mg/dm³ |
| **total sulfur dioxide** | numérica | SO2 total | 6 - 289 mg/dm³ |
| **density** | numérica | Densidad | 0.990 - 1.004 g/cm³ |
| **pH** | numérica | pH | 2.74 - 4.01 |
| **sulphates** | numérica | Sulfato de potasio | 0.33 - 2.0 g/dm³ |
| **alcohol** | numérica | % de alcohol | 8.4 - 14.9% |
| **quality** | ordinal | Calidad (0-10) | 3 - 8 |

## 7. Resultados esperados
- Un modelo capaz de clasificar vinos en categorías de calidad.
- Visualizaciones que expliquen el comportamiento de los datos