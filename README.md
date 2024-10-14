# 📊 Análisis de la Ejecución de Ingresos Públicos en Brasil

## 📖 Descripción
Este proyecto realiza un análisis de los datos históricos de la ejecución de ingresos públicos en Brasil entre 2013 y 2021. El objetivo es identificar patrones y áreas problemáticas en la recaudación de ingresos, así como proponer recomendaciones que ayuden a mejorar la precisión de las previsiones y la eficiencia en la recaudación. El análisis se centra en las desviaciones entre lo previsto y lo recaudado, la evolución temporal de los ingresos y el rendimiento de diferentes órganos y unidades gestoras.

## 🗂️ Estructura del Proyecto

```
├── data/ # Datos crudos y procesados ├── notebooks/ # Notebooks de Jupyter con el análisis ├── src/ # Scripts de procesamiento y modelado ├── results/ # Gráficos y archivos de resultados ├── README.md # Descripción del proyecto
```

## 🛠️ Instalación y Requisitos
Este proyecto utiliza Python 3.8 y requiere las siguientes bibliotecas:

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

## 📝 Instrucciones Detalladas

## Lectura y Exploración Inicial

1. **Importación de Bibliotecas**: Se importaron bibliotecas esenciales como `pandas`, `numpy`, `matplotlib` y `seaborn`.

2. **Carga de Datos**: Se leyeron archivos CSV de ingresos públicos en Brasil y se generaron dataframes individuales.

3. **Limpieza de Años**: Se creó una función para rellenar los años faltantes en los dataframes con el valor correspondiente del archivo.

4. **Verificación de Columnas**: Se comprobó que todos los dataframes tenían las mismas columnas y tipos de datos consistentes.

5. **Unión de Dataframes**: Se concatenaron todos los dataframes en uno único (`df_merged`), se renombraron las columnas a inglés y se realizaron verificaciones de datos nulos.

6. **Relación Código-Nombre**: Se generaron diccionarios para mapear códigos de entidades a sus nombres y se rellenaron valores vacíos.

7. **Conversión de Tipos**: Se convirtieron valores monetarios a formato numérico y se aseguraron las fechas con el formato correcto.

8. **Guardado de Datos**: Se guardó el dataframe final en un nuevo archivo CSV (`df_merged.csv`).


## 2. Limpieza

1. **Carga de Datos**: Se cargó el dataframe consolidado (`df_merged.csv`) que contiene los ingresos públicos de Brasil.

2. **Filtrado de Filas con Valores Cero**: Se identificaron filas donde todos los valores monetarios eran cero, representando un pequeño porcentaje del total. Se decidió analizar la distribución de estas filas en relación a los cuerpos superiores.

3. **Análisis de Proporciones**: Se realizaron gráficos de pie para comparar la proporción de filas con valores nulos respecto al total y se observó que no hay una concentración significativa en cuerpos superiores específicos.

4. **Verificación de Años Fiscales**: Se revisó la proporción de datos nulos por año fiscal, encontrando que de 2013 a 2015 había menos datos, lo que podría indicar un fallo en el registro de datos.

5. **Eliminación de Filas**: Se eliminaron las filas con todos los valores monetarios cero del dataframe. La proporción de datos eliminados se reportó.

6. **Consistencia en Categorías Económicas**: Se exploraron las categorías económicas, identificando variaciones en las subcategorías. Se definió una nueva columna para las subcategorías agrupando datos relevantes.

7. **Guardado de Datos Limpiados**: Se guardó el dataframe limpio en un nuevo archivo CSV (`df_clean.csv`) para su análisis posterior.


## Análisis Exploratorio de Datos (EDA)

1. **Distribución de Ingresos por Categoría Económica**: Se agruparon los ingresos por **economy_category** y **economy_subcategory**, sumando los valores realizados y calculando su porcentaje del total. Los ingresos corrientes son ligeramente superiores a los de capital, con predominancia de ingresos no intergubernamentales.

2. **Cálculo de Diferencias**: Se creó una nueva columna para calcular la diferencia promedio entre ingresos estimados y realizados. Se identificaron casos donde el valor estimado era 0, lo que generó diferencias negativas. Aproximadamente el **{df_noest.shape[0]/df.shape[0]*100:.2f}%** de los casos no tenía estimaciones previas, indicando posibles ingresos no planificados o errores en el registro.

3. **Análisis Temporal Anual**: Se sumaron los ingresos realizados por año, observando un crecimiento hasta 2016, seguido de un descenso en 2017, posiblemente debido a corrupción y huelgas en Brasil.

4. **Análisis Temporal Mensual**: Se calcularon sumas, medias y medianas de ingresos mensuales. Se observó un aumento significativo en diciembre, posiblemente relacionado con el cierre del año fiscal. Las medianas mostraron un comportamiento más estable, confirmando el aumento en diciembre.

5. **Identificación de Discrepancias**: Se analizaron las diferencias entre estimaciones y realizaciones por cuerpo superior, utilizando media y mediana para obtener una visión más completa. El Ministerio de Economía mostró consistentemente mayores diferencias, sugiriendo la necesidad de mejorar las predicciones de ingresos.


### Fase 4: Visualización de Datos
1. **Gráficos de Barras y Líneas:**
   - Comparar ingresos previstos, lanzados y realizados para cada categoría.

2. **Diagramas de Caja:**
   - Evaluar la dispersión de las diferencias entre los valores previstos y realizados.

### Fase 5: Conclusiones y Recomendaciones
1. **Resumen de Hallazgos:**
   - Identificar las categorías y períodos con mayor discrepancia.

2. **Propuestas de Mejora:**
   - Sugerir acciones para mejorar la planificación y ejecución de los ingresos.

## 📊 Resultados y Conclusiones
- Se identificaron desviaciones significativas entre los valores previstos y los valores realizados en varias categorías económicas.
- Se observó un aumento estacional en los ingresos realizados, especialmente en diciembre.
- Las unidades gestoras que mostraron consistentemente baja ejecución pueden necesitar un análisis más profundo para identificar ineficiencias.

## 🔄 Próximos Pasos
- Refinar el análisis para incluir factores externos que puedan afectar la recaudación.
- Implementar un modelo predictivo para estimar mejor los ingresos futuros.
- Explorar la relación entre la ejecución de ingresos y variables económicas, como la inflación y el crecimiento del PIB.

## 🤝 Contribuciones
Las contribuciones son bienvenidas. Si deseas mejorar el proyecto, por favor abre un pull request o una issue.
