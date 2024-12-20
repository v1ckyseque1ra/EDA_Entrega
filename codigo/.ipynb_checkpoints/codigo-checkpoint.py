import pandas as pd
pd.set_option('display.max_columns', None) #Configuro Pandas para ver todas las columnas
df = pd.read_excel("dp2015-13_Dataset.xls")
print(df.head())
print('El dataset tiene {} filas y {} columnas.'.format(df.shape[0],df.shape[1]))

lista_col_con_nulos = []
lista_col_20_nulos= []

for col in df:
    sum_nulls = df[col].isnull().sum() / len(df) * 100
    if sum_nulls != 0:
        lista_col_con_nulos.append(col)
    if sum_nulls > 20:
        lista_col_20_nulos.append(col) 

print(f'Number of columns in the dataframe                             = {df.shape[1]}')
print(f'Number of columns with nulls in the dataframe                  = {len(lista_col_con_nulos)}')
print(f'Number of columns with more than 20% of nulls in the dataframe = {len(lista_col_20_nulos)}')

print("Las siguientes columnas contienen valores nulos y serán eliminadas:")
print(lista_col_20_nulos)

df2 = df.drop(columns=lista_col_20_nulos,axis=1)

print(df2.head(5))
print(df2.shape)

lista_menos_20_nulos = []

lista_menos_20_nulos = list(set(lista_col_con_nulos) - set(lista_col_20_nulos))

lista_menos_20_nulos

#Calculo el numero de entradas nulas que tienen las columnas arriba detalladas
print(f'Nulls in MIR2009: {df2.MIR2009.isnull().sum()}')
print(f'Nulls in MIR2010: {df2.MIR2010.isnull().sum()}')
print(f'Nulls in Inflation2011: {df2.Inflation2011.isnull().sum()}')
print(f'Nulls in Mortgage_PC2010: {df2.Mortgage_PC2010.isnull().sum()}')

print(f'Numero de filas duplicadas en el dataset = {df2.duplicated().sum()}')

df2.drop(['City',
            'City_Short',
            'Latitude_deg',
            'Latitude_min',
            'Latitude_sec',
            'Longitude_deg',
            'Longitude_min',
            'Longitude_sec',
            'Lat',
            'Lon',
            'GDP_PC_PPS',
            'GDP_PC2008',
            'GDP_PC2009',
            'GDP_PC2010',
            'NAds'],axis=1,inplace=True)

print(df2.columns)
df2.rename(columns={'City_Eng':'Ciudad',
                      'Price_Median':'Mediana_Precios',
                      'Price_Mean':'Media_Precios',
                      'Area_Median':'Mediana_Area',
                      'Area_Mean':'Media_Area',
                      'Room_Median':'Mediana_habitaciones',
                      'Room_Mean':'Media_Habitaciones',
                      'Euro_area':'ZonaEuro',
                      'EU':'UnionEuropea',
                      'Population':'Poblacion',
                      'City_Area':'Area_Ciudad',
                      'Density':'Densidad Poblacional', 
                      'GDP_PC':'PIB_PC',
                      'HOR':'Tasa de Propiedad de Vivienda', 
                      'Kearny_GCI2010':'Indice Global de Ciudades de Kearny',
                      'LRIR':'Tasa de interés a largo plazo',
                      'Inflation2010':'Inflacion 2010',
                      'Inflation2011':'Inflacion 2011', 
                      'URate':'Tasa de Desempleo', 
                      'MIR2009':'Tasa de interés hipotecario 2009',
                      'MIR2010':'Tasa de interés hipotecario 2010',
       'Mortgage_PC2010':'Hipotecas per capita'},inplace=True)

print(df2.head())
print('El dataset tiene ahora {} filas y {} columnas.'.format(df2.shape[0],df2.shape[1]))

print(df2.info())

# Convertir las columnas 'Union Europea' y 'ZonaEuro' a tipo booleano
df2['UnionEuropea'] = df2['UnionEuropea'].astype(bool)
df2['ZonaEuro'] = df2['ZonaEuro'].astype(bool)

df2['Ciudad'] = df2['Ciudad'].astype('string')
