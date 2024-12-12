# EDA_Entrega
Project Break I
## Hipotesis

**Tabla de requerimiento de datos**

| Pregunta/Hipótesis | Columnas Requeridas | Descripción |
|--------------------|---------------------|-------------|
| ¿Existe una relación entre el ingreso per cápita (GDP_PC) y el precio medio de las viviendas en las diferentes ciudades? | City, Price_Mean, GDP_PC | Comparar el ingreso per cápita y el precio medio de viviendas para cada ciudad. |
| ¿Cómo influye la densidad de población (Density) en el área media de las viviendas? | City, Density, Area_Mean | Analizar si las ciudades con mayor densidad tienen viviendas más grandes o pequeñas en promedio. |
| ¿Las tasas de desempleo (URate) están asociadas con las tasas de propiedad de viviendas? | City, URate, Phh-owndwe2007_2009 | Explorar si en ciudades con mayor desempleo hay menos propiedad de viviendas en el período indicado. |

---

## Pasos de limpieza de datos realizados

1. **Carga y visualización inicial del dataset**:
   - Se carga el archivo `dp2015-13_Dataset.xls` en un DataFrame de Pandas.
   - Se configuran las opciones de Pandas para mostrar todas las columnas.
   - Se imprime las primeras filas del dataset y se obtiene información sobre el número de filas y columnas.

2. **Identificación de columnas con valores nulos**:
   - Se calcula el porcentaje de valores nulos para cada columna.
   - Se identifican las columnas con algún valor nulo (`lista_col_con_nulos`).
   - Se identifican las columnas con más del 20% de valores nulos (`lista_col_20_nulos`).
   - Se imprime un resumen con la cantidad de columnas con nulos y aquellas que tienen más del 20% de nulos.

3. **Eliminación de columnas con más del 20% de nulos**:
   - Se eliminan las columnas que contienen más del 20% de valores nulos del DataFrame (`df2`).
   - Se imprime el nuevo DataFrame y su tamaño (número de filas y columnas).

4. **Revisión de columnas restantes con valores nulos**:
   - Se calcula y se imprime el número de valores nulos en varias columnas del dataset tras la eliminación.

5. **Eliminación de columnas innecesarias**:
   - Se eliminan otras columnas que no son relevantes para el análisis, como las relacionadas con la ubicación geográfica y el PIB.
   - Se imprime la lista de columnas restantes.

6. **Renombrado de columnas**:
   - Se renombran las columnas para que tengan nombres más descriptivos y en español.
   - Se imprime el nuevo DataFrame con los nombres de las columnas actualizados.

7. **Conversión de tipos de datos**:
   - Se convierten las columnas `UnionEuropea` y `ZonaEuro` a tipo booleano.
   - Se convierte la columna `Ciudad` a tipo string.

8. **Revisión final del DataFrame**:
   - Se imprime un resumen del DataFrame después de la limpieza, mostrando el número de filas, columnas y la información de los tipos de datos.

---

Este proceso de limpieza tiene como objetivo reducir el ruido de datos innecesarios y preparar el conjunto para análisis posteriores.