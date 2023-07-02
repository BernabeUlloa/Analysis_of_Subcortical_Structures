#Analysis of Subcortical Structures
# https://github.com/BernabeUlloa/Analysis_of_Subcortical_Structures.git

#Analysis of Subcortical Structures Processing of medical images from 
#10 subjects in the public HCP database [1], including their T1 structural 
#images and corresponding subcortical segmentation. Quantitative measures are 
#calculated using masks for scientific analysis, such as the average intensity 
#of a region, arithmetic mean, and coefficient of variation of these averages.

import os
import nibabel as nib
import visualtools  as vt #Visualization library
import numpy as np
import pandas as pd



no_etiqueta = []
etiqueta = []
with open('FreeSurferColorLUT.txt', 'r') as f:
    for line in f:
        fields = line.split()
        no_etiqueta.append(fields[0])
        etiqueta.append(fields[1])
no_etiqueta.pop(0)
etiqueta.pop(0)



ruta_principal = os.path.dirname(os.path.abspath('MP_copia.py'))
carpetas = [nombre for nombre in os.listdir(ruta_principal) if os.path.isdir(os.path.join(ruta_principal, nombre))]




big_image_data = []
big_mask_data = []

for carpeta in carpetas:
    archivo_a = os.path.join(ruta_principal, carpeta, 'orig.nii.gz')
    archivo_b = os.path.join(ruta_principal, carpeta, 'aseg.nii.gz')
    if not (os.path.exists(archivo_a) and os.path.exists(archivo_b)):
        carpetas.remove(carpeta)
    else:
        img = nib.load(archivo_a)
        img_data=img.get_data()
        big_image_data.append(img_data)

        mask = nib.load(archivo_b)
        mask_data=mask.get_data()
        big_mask_data.append(mask_data)             

vt.multi_slice_viewer(big_image_data[0], 'Imagen original')


datos_por_carpeta = {}
for indice, carpeta in enumerate(carpetas):    
    intensidad = []
    for elemento in no_etiqueta:
        parte_deseada = big_image_data[indice-1] * (big_mask_data[indice-1] == int(elemento))
        non_z = np.nonzero(parte_deseada)
        valor_promedio = np.mean(parte_deseada[non_z])
        intensidad.append(valor_promedio)
        if (indice == 0 and int(elemento) == 41):
            vt.multi_slice_viewer(parte_deseada, 'Right-Cerebral-White-Matter')
    datos_por_carpeta[carpeta] = intensidad
    
df_por_carpeta = pd.DataFrame(datos_por_carpeta, index = None)


mean_ = []

for fila in df_por_carpeta.index:
    media_aritmetica = df_por_carpeta.loc[fila].mean()
    mean_.append(media_aritmetica)

    df_mean = pd.DataFrame({'Media aritmetica de promedios de intensidad': mean_}, index = None)




std = df_por_carpeta.std(axis=1)
df_std = pd.DataFrame({'σ Desviación estándar de promedios de intensidad': std}, index = None)




df_concatenado = pd.concat([df_mean, df_std],axis=1)


def coeficiente_de_variacion(row):
    a = row['σ Desviación estándar de promedios de intensidad']
    b = row['Media aritmetica de promedios de intensidad']
    return 100 * (a / b)

df_concatenado['% Coeficiente de Variación'] = df_concatenado.apply(coeficiente_de_variacion, axis=1)



df_etiqueta = pd.DataFrame({'Region': etiqueta}, index = None)

EL_DF = pd.concat([df_etiqueta, df_por_carpeta, df_concatenado],axis=1)
EL_DF = EL_DF.sort_values(by=['% Coeficiente de Variación'], ascending=True)


output_folder = 'resultados'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

output_file = os.path.join(output_folder, 'resultados.xlsx')

EL_DF.to_excel(output_file)

#[1]Human Connectome Project Young Adult Study. “1200 Subjects Data Release”. 
#https://www.humanconnectome.org/study/hcp-young-adult/document/1200-subjects-data-release. 
#(accessed on 17 April 2023).