# 📊 Análisis de la Ejecución de Ingresos Públicos en Brasil

## 📖 Descripción
Este proyecto realiza un análisis de los datos históricos de la ejecución de ingresos públicos en Brasil entre 2013 y 2021. El objetivo es identificar patrones y áreas problemáticas en la recaudación de ingresos, así como proponer recomendaciones que ayuden a mejorar la precisión de las previsiones y la eficiencia en la recaudación. El análisis se centra en las desviaciones entre lo previsto y lo recaudado, la evolución temporal de los ingresos y el rendimiento de diferentes órganos y unidades gestoras.

## 🗂️ Estructura del Proyecto

```
├── README.md                   # Descripción del proyecto
├── .gitignore                  # gitignore
├── data/                       # Datos crudos y procesados
├── notebook/                   # Notebooks de Jupyter con el análisis
│   ├── merger.ipynb             
│   ├── cleanse.ipynb          
│   ├── eda.ipynb 
│   ├── visuals.ipynb     
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

7. **Guardado de Datos Limpios**: Se guardó el dataframe limpio en un nuevo archivo CSV (`df_clean.csv`) para su análisis posterior.


## Análisis Exploratorio de Datos (EDA)

1. **Distribución de Ingresos por Categoría Económica**: Se agruparon los ingresos por **economy_category** y **economy_subcategory**, sumando los valores realizados y calculando su porcentaje del total. Los ingresos corrientes son ligeramente superiores a los de capital, con predominancia de ingresos no intergubernamentales.

2. **Cálculo de Diferencias**: Se creó una nueva columna para calcular la diferencia promedio entre ingresos estimados y realizados. Se identificaron casos donde el valor estimado era 0, lo que generó diferencias negativas. Aproximadamente el **{df_noest.shape[0]/df.shape[0]*100:.2f}%** de los casos no tenía estimaciones previas, indicando posibles ingresos no planificados o errores en el registro.

3. **Análisis Temporal Anual**: Se sumaron los ingresos realizados por año, observando un crecimiento hasta 2016, seguido de un descenso en 2017, posiblemente debido a corrupción y huelgas en Brasil.

4. **Análisis Temporal Mensual**: Se calcularon sumas, medias y medianas de ingresos mensuales. Se observó un aumento significativo en diciembre, posiblemente relacionado con el cierre del año fiscal. Las medianas mostraron un comportamiento más estable, confirmando el aumento en diciembre.

5. **Identificación de Discrepancias**: Se analizaron las diferencias entre estimaciones y realizaciones por cuerpo superior, utilizando media y mediana para obtener una visión más completa. El Ministerio de Economía mostró consistentemente mayores diferencias, sugiriendo la necesidad de mejorar las predicciones de ingresos.


## Visualización

1. **Gráficas por Categoría y Subcategoría**: Se generaron gráficos de barras para visualizar los valores estimados, lanzados y realizados, agrupados por **economy_category** y **economy_subcategory**. Esto permite identificar qué categorías tienen las mejores estimaciones, destacando que las **Receitas Correntes** muestran mayor consistencia entre lo estimado y lo realizado.

2. **Evolución Temporal**: Se elaboraron gráficos de líneas para observar la evolución de los ingresos a lo largo de los años fiscales, comparando los valores estimados y realizados. Se notó que el valor estimado suele ser superior al realizado, a excepción de ciertos años como 2016, coincidiendo con eventos económicos significativos en Brasil.

3. **Diagramas de Cajas**: Se utilizaron diagramas de cajas para evaluar la dispersión de las diferencias porcentuales entre los valores estimados y realizados por categoría. Los ingresos de capital presentaron menor dispersión, mientras que dentro de las **Receitas Correntes**, las intergubernamentales mostraron la menor variación.


## Conclusiones

### Resumen de Hallazgos

1. **Discrepancias en Ingresos**: Se identificó que las **Receitas de Capital** presentan las mayores discrepancias entre los ingresos estimados y realizados. En particular, algunos años, como 2016, mostraron diferencias significativas que requieren atención.

2. **Tendencias de Ejecución**: A lo largo del período analizado, se observó un crecimiento en los ingresos hasta 2016, seguido de una caída en 2017. Este descenso puede estar asociado a factores como la recesión económica y eventos políticos, afectando la recaudación.

3. **Aumento de ingresos fin de año**: Durante los años se ha observado una tendencia de aumento en los ingresos de todas las categorías económicas en el mes de diciembre, posiblemente debido a un cierre del año fiscal.

### Propuestas de Mejora

1. **Fortalecer el Proceso de Estimación**: Implementar metodologías más robustas y basadas en datos históricos para mejorar la precisión en la estimación de ingresos, especialmente para las **Receitas de Capital**.

2. **Análisis de Datos Atípicos**: Realizar una limpieza exhaustiva de datos y un análisis de valores atípicos para asegurar que las proyecciones se basen en información precisa y representativa. Crear una diferenciación entre datos nulos y 0 en los valores, ya que podrían significar diferentes cosas dependiendo del contexto en el que se encuentren registrados.

3. **Mejoras en el Registro de Datos**: Implantar un sistema de registros donde los datos se completen de forma correcta, de tal modo que las discrepancias y los valores atípicos se puedan reducir en gran medida, lo cual mejoraría y ampliaría las posibilidades a la hora de realizar un análisis económico del país.


## 🔄 Próximos Pasos
- Iincluir un análisis de los valores atípicos encontrados en todas las categorías, de tal manera que las inferencias puedan ser más precisas, sin la dependencia de estas sobre el significado de valores inciertos.
- Exploración histórica para comprender las tendencias anuales (y/o mensuales) y las fluctuaciones en los ingresos.


## 🤝 Contribuciones
Las contribuciones son bienvenidas. Si deseas mejorar el proyecto, por favor abre un pull request o una issue.
