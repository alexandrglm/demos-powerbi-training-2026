import re
import pandas as pd

# 1. Función para convertir nombres de municipios a Title Case manteniendo guiones y barras
def titutillar_municipio(nombre):
    # Separa por palabras y conectores manteniendo estructura
    palabras = re.split(r'([\s/\-])', nombre)
    excepciones_minusculas = {'y', 'de', 'del', 'las', 'los', 'la', 'el'}
    
    resultado = []
    for i, p in enumerate(palabras):
        p_lower = p.lower()
        if p_lower in excepciones_minusculas and i > 0:
            resultado.append(p_lower)
        else:
            resultado.append(p.capitalize())
    return "".join(resultado)

# 2. Cargar y procesar datos (reemplaza 'datos_rgi.txt' por la ruta de tu archivo)
# El script generará el dataframe unpivoteado plano 'df_final'