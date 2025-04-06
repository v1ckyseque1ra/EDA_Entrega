# EDA_Entrega


## Project Break I

### Introducción
El proyecto analiza un dataset sobre el mercado inmobiliario europeo, las condiciones en las que se desarrolla y algunas variables de relevancia.

---

Project Break I
**Tabla de requerimiento de datos**

| Pregunta/Hipótesis | Columnas Requeridas | Descripción |
|--------------------|---------------------|-------------|
| ¿Existe una relación entre el ingreso per cápita (GDP_PC) y el precio medio de las viviendas en las diferentes ciudades? | City, Price_Mean, GDP_PC | Comparar el ingreso per cápita y el precio medio de viviendas para cada ciudad. |
| ¿Cómo influye la densidad de población (Density) en el área media de las viviendas? | City, Density, Area_Mean | Analizar si las ciudades con mayor densidad tienen viviendas más grandes o pequeñas en promedio. |
| ¿Las tasas de desempleo (URate) están asociadas con las tasas de propiedad de viviendas? | City, URate, Phh-owndwe2007_2009 | Explorar si en ciudades con mayor desempleo hay menos propiedad de viviendas en el período indicado. |

---

### Requisitos del Sistema

Las librerias y módulos utilizados son: geopandas, matplotlib módulo pyplot, numpy, pandas, plotly módulo express, scipy módulo stats y seaborn
---
### Instalación
1. Clona el repositorio:
   ```
   git clone https://github.com/tuusuario/EDA_Entrega.git
   ```
2. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

---

### Estructura del Repositorio
Explicación de la organización de carpetas y archivos.
- `data/`: Contiene los datasets utilizados.
- `notebooks/`: Jupyter Notebooks con el análisis.
- `src/`: Código fuente del proyecto.
- `/utils`: módulo, funciones auxiliares, clases creadas
- `/memoria`: Resumen de los pasos de la analìtica
- Otros archivos relevantes.

---

### Pasos de limpieza de datos realizados
=======
## Pasos de limpieza de datos realizados


1. **Carga y visualización inicial del dataset**:
   - Se carga el archivo `dp2015-13_Dataset.xls` en un DataFrame de Pandas.
   - Se configuran las opciones de Pandas para mostrar todas las columnas.
<<<<<<< HEAD
   - Se imprimen las primeras filas del dataset y se obtiene información sobre el número de filas y columnas.
=======

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
### Memoria del proceso de elaboración del EDA

**Día 1:**
- Definición del caso de uso y recolección de datos.
- Elección de la temática.
- Búsqueda del dataset.
- Definición de hipótesis.
- Documentación del contexto del problema y las hipótesis iniciales en el borrador del README.

**Día 2:**
- Preprocesamiento de datos: descarga y organización de datos.
- Creación de estructura de carpetas en el repositorio de GitHub.
- Limpieza inicial: tratamiento de valores nulos, duplicados y columnas irrelevantes.
- Uniformización de datos.
- Documentación de los pasos de limpieza en el README.

**Día 3:**
- Análisis exploratorio inicial para entender los datos.
- Estadísticas básicas: medias, medianas y desviación estándar.
- Generación de scatterplots, gráficos de caja y gráficos de barra para identificar tendencias y outliers.
- Descripción de relaciones entre variables con correlaciones y visualizaciones.
- Documentación de observaciones preliminares.

**Día 4:**
- Análisis avanzado: generación de nuevas variables y transformación en categorización.
- Análisis multivariante.
- Validación de hipótesis.
- Inclusión de conclusiones preliminares en el README.

**Día 5:**
- Diseño de la presentación:
  - Estructura basada en el contexto (30%), análisis (50%) y conclusiones/oportunidades (20%).
  - Diseño de slides en PowerPoint.
  - Ensayo de la narrativa del discurso.

**Día 6:**
- Grabación y edición del video.
- Ajuste de detalles finales.

**Día 7:**
- Documentación y revisión final:
  - Redacción del README definitivo.
  - Organización del repositorio en GitHub.
  - Pruebas finales del código.

**Día 8:**
- Entrega del proyecto.
- Publicación del enlace de GitHub.

---

### Resultados Principales
1- Existe una relación positiva moderada a fuerte entre el ingreso per capita y el precio emdio de las viviendas de diferentes ciudades.
2- Las diferencias de densidades baja media y alta en relación con la media del area de las viviendas son muy pequeñas.
3- Hay una relación negativa débil entre la tasa de desempleo y la tasa de propiedad de las viviendas.

---

### Próximos Pasos
- Profundizar en factores determinantes del mercado inmobiliario (costo de construcción, políticas fiscales locales, tasas de interés locales).
- Segmentar en subgrupos (ciudades grandes frente a pequeñas o regiones con diferente desarrollo económico).
- Ampliar la muestra y las métricas.
---

### Licencia
Este proyecto fue creado como parte del bootcamp de Data Science de The Bridge. Su uso está restringido a fines educativos y personales. No está permitido su uso comercial ni su redistribución sin autorización previa del autor.

---

### Autores y Reconocimientos

Maria Victoria Sequeira
---

### Contacto

Para más información o comentarios, puedes visitarme en:  
- [Mi perfil de LinkedIn](https://www.linkedin.com/in/maria-victoria-sequeira-77a07528a/)  
- [Mi perfil de GitHub](https://github.com/v1ckyseque1ra)

=======
