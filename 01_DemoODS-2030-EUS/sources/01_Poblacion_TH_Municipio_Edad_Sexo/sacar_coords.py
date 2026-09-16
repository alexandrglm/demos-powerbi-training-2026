import pandas as pd
import sys
import re

# ==================== FUNCIÓN PARA NORMALIZAR NOMBRES ====================
def normalizar_nombre(nombre):
    """Normaliza nombres para comparación flexible"""
    if not isinstance(nombre, str):
        return ''
    # Convertir a minúsculas
    nombre = nombre.lower()
    # Eliminar espacios extra
    nombre = ' '.join(nombre.split())
    # Reemplazar caracteres especiales
    reemplazos = {
        '/': ' ',
        '-': ' ',
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'ñ': 'n', 'ü': 'u'
    }
    for old, new in reemplazos.items():
        nombre = nombre.replace(old, new)
    # Eliminar duplicados de espacios
    nombre = ' '.join(nombre.split())
    return nombre

# ==================== DICCIONARIO DE MUNICIPIOS ====================
municipios_buscar = {
    # ARABA/ÁLAVA
    'Agurain/Salvatierra': '010516',
    'Alegría-Dulantzi': '010014',
    'Amurrio': '010023',
    'Añana': '010493',
    'Aramaio': '010035',
    'Armiñón': '010061',
    'Arraia-Maeztu': '010376',
    'Arratzua-Ubarrundia': '010082',
    'Artziniega': '010040',
    'Asparrena': '010098',
    'Ayala/Aiara': '010105',
    'Baños de Ebro/Mañueta': '010110',
    'Barrundia': '010131',
    'Berantevilla': '010147',
    'Bernedo': '010168',
    'Campezo/Kanpezu': '010173',
    'Elburgo/Burgelu': '010217',
    'Elciego': '010222',
    'Elvillar/Bilar': '010238',
    'Erriberagoitia/Ribera Alta': '010467',
    'Harana/Valle de Arana': '010563',
    'Iruña Oka/Iruña de Oca': '019013',
    'Iruraiz-Gauna': '010273',
    'Kripan': '010194',
    'Kuartango': '010201',
    'Labastida/Bastida': '010285',
    'Lagrán': '010308',
    'Laguardia': '010313',
    'Lanciego/Lantziego': '010329',
    'Lantarón': '019025',
    'Lapuebla de Labarca': '010334',
    'Laudio/Llodio': '010360',
    'Legutio': '010584',
    'Leza': '010343',
    'Moreda de Álava/Moreda Araba': '010397',
    'Navaridas': '010413',
    'Okondo': '010425',
    'Oyón-Oion': '010430',
    'Peñacerrada-Urizaharra': '010446',
    'Ribera Baja/Erriberabeitia': '010472',
    'Samaniego': '010521',
    'San Millán/Donemiliaga': '010537',
    'Urkabustaiz': '010542',
    'Urduña/Orduña': '010745',
    'Valdegovía/Gaubea': '010558',
    'Villabuena de Álava/Eskuernaga': '010579',
    'Vitoria-Gasteiz': '010593',
    'Yécora/Iekora': '010607',
    'Zalduondo': '010612',
    'Zambrana': '010628',
    'Zigoitia': '010189',
    'Zuia': '010633',
    
    # BIZKAIA
    'Abadiño': '480018',
    'Abanto y Ciérvana-Abanto Zierbena': '480023',
    'Amorebieta-Etxano': '480039',
    'Amoroto': '480044',
    'Arakaldo': '480053',
    'Arantzazu': '480065',
    'Munitibar-Arbatzegi Gerrikaitz': '480070',
    'Artzentales': '480086',
    'Arrankudiaga-Zollo': '480091',
    'Arrieta': '480109',
    'Arrigorriaga': '480114',
    'Bakio': '480123',
    'Barakaldo': '480135',
    'Barrika': '480140',
    'Basauri': '480156',
    'Berango': '480161',
    'Bermeo': '480177',
    'Berriatua': '480182',
    'Berriz': '480198',
    'Bilbao': '480205',
    'Busturia': '480210',
    'Karrantza Harana/Valle de Carranza': '480226',
    'Artea': '480231',
    'Zeanuri': '480247',
    'Zeberio': '480252',
    'Dima': '480268',
    'Durango': '480273',
    'Ea': '480289',
    'Etxebarri': '480294',
    'Etxebarria': '480301',
    'Elantxobe': '480317',
    'Elorrio': '480322',
    'Ereño': '480338',
    'Ermua': '480343',
    'Fruiz': '480359',
    'Galdakao': '480364',
    'Galdames': '480373',
    'Gamiz-Fika': '480385',
    'Garai': '480390',
    'Gatika': '480408',
    'Gautegiz Arteaga': '480413',
    'Gordexola': '480429',
    'Gorliz': '480434',
    'Getxo': '480443',
    'Güeñes': '480455',
    'Gernika-Lumo': '480460',
    'Gizaburuaga': '480476',
    'Ibarrangelu': '480481',
    'Ispaster': '480497',
    'Izurtza': '480504',
    'Lanestosa': '480513',
    'Larrabetzu': '480525',
    'Laukiz': '480530',
    'Leioa': '480546',
    'Lemoa': '480551',
    'Lemoiz': '480567',
    'Lekeitio': '480572',
    'Mallabia': '480588',
    'Mañaria': '480593',
    'Markina-Xemein': '480600',
    'Maruri-Jatabe': '480616',
    'Mendata': '480621',
    'Mendexa': '480637',
    'Meñaka': '480642',
    'Ugao-Miraballes': '480658',
    'Morga': '480663',
    'Muxika': '480679',
    'Mundaka': '480684',
    'Mungia': '480693',
    'Aulesti': '480707',
    'Muskiz': '480712',
    'Otxandio': '480728',
    'Ondarroa': '480733',
    'Urduña/Orduña': '480749',
    'Orozko': '480754',
    'Sukarrieta': '480763',
    'Plentzia': '480775',
    'Portugalete': '480780',
    'Errigoiti': '480796',
    'Valle de Trápaga-Trapagaran': '480803',
    'Lezama': '480819',
    'Santurtzi': '480824',
    'Ortuella': '480833',
    'Sestao': '480845',
    'Sopela': '480850',
    'Sopuerta': '480866',
    'Trucios-Turtzioz': '480871',
    'Ubide': '480887',
    'Urduliz': '480892',
    'Balmaseda': '480903',
    'Atxondo': '480915',
    'Bedia': '480920',
    'Areatza': '480936',
    'Igorre': '480941',
    'Zaldibar': '480957',
    'Zalla': '480962',
    'Zaratamo': '480978',
    'Derio': '489013',
    'Erandio': '489029',
    'Loiu': '489034',
    'Sondika': '489043',
    'Zamudio': '489055',
    'Forua': '489060',
    'Kortezubi': '489076',
    'Murueta': '489081',
    'Nabarniz': '489097',
    'Iurreta': '489104',
    'Ajangiz': '489113',
    'Alonsotegi': '489125',
    'Zierbena': '489130',
    'Arratzu': '489146',
    'Ziortza-Bolibar': '489151',
    'Usansolo': '489167',
    
    # GIPUZKOA
    'Abaltzisketa': '20001',
    'Aduna': '20002',
    'Aizarnazabal': '20003',
    'Albiztur': '20004',
    'Alegia': '20005',
    'Alkiza': '20006',
    'Altzo': '20007',
    'Amezketa': '20008',
    'Andoain': '20009',
    'Anoeta': '20010',
    'Antzuola': '20011',
    'Arama': '20012',
    'Aretxabaleta': '20013',
    'Asteasu': '20014',
    'Ataun': '20015',
    'Aia': '20016',
    'Azkoitia': '20017',
    'Azpeitia': '20018',
    'Beasain': '20019',
    'Beizama': '20020',
    'Belauntza': '20021',
    'Berastegi': '20022',
    'Berrobi': '20023',
    'Bidania-Goiatz': '20024',
    'Zegama': '20025',
    'Zerain': '20026',
    'Zestoa': '20027',
    'Zizurkil': '20028',
    'Deba': '20029',
    'Eibar': '20030',
    'Elduain': '20031',
    'Elgoibar': '20032',
    'Elgeta': '20033',
    'Eskoriatza': '20034',
    'Ezkio-Itsaso': '20035',
    'Hondarribia': '20036',
    'Gaintza': '20037',
    'Gabiria': '20038',
    'Getaria': '20039',
    'Hernani': '20040',
    'Hernialde': '20041',
    'Ibarra': '20042',
    'Idiazabal': '20043',
    'Ikaztegieta': '20044',
    'Irun': '20045',
    'Irura': '20046',
    'Itsasondo': '20047',
    'Larraul': '20048',
    'Lazkao': '20049',
    'Leaburu': '20050',
    'Legazpi': '20051',
    'Legorreta': '20052',
    'Lezo': '20053',
    'Lizartza': '20054',
    'Arrasate/Mondragón': '20055',
    'Mutriku': '20056',
    'Mutiloa': '20057',
    'Olaberria': '20058',
    'Oñati': '20059',
    'Orexa': '20060',
    'Orio': '20061',
    'Ormaiztegi': '20062',
    'Oiartzun': '20063',
    'Pasaia': '20064',
    'Soraluze-Placencia de las Armas': '20065',
    'Errezil': '20066',
    'Errenteria': '20067',
    'Leintz-Gatzaga': '20068',
    'Donostia / San Sebastián': '20069',
    'Segura': '20070',
    'Tolosa': '20071',
    'Urnieta': '20072',
    'Usurbil': '20073',
    'Bergara': '20074',
    'Villabona': '20075',
    'Ordizia': '20076',
    'Urretxu': '20077',
    'Zaldibia': '20078',
    'Zarautz': '20079',
    'Zumarraga': '20080',
    'Zumaia': '20081',
    'Mendaro': '20901',
    'Lasarte-Oria': '20902',
    'Astigarraga': '20903',
    'Baliarrain': '20904',
    'Orendain': '20905',
    'Altzaga': '20906',
    'Gaztelu': '20907'
}

# Formatear códigos a 6 dígitos
for nombre, codigo in municipios_buscar.items():
    municipios_buscar[nombre] = str(codigo).zfill(6)

# Crear índice normalizado para búsqueda
indice_normalizado = {}
for nombre in municipios_buscar.keys():
    indice_normalizado[normalizar_nombre(nombre)] = nombre

# ==================== LEER ARCHIVO EXCEL ====================
try:
    print('📂 Leyendo archivo MUNICIPIOS.xlsx...')
    df = pd.read_excel('MUNICIPIOS.xlsx', dtype=str)
    print(f'✅ Archivo leído. {len(df)} registros encontrados.')
    print(f'📋 Columnas disponibles: {df.columns.tolist()}')
except FileNotFoundError:
    print('❌ Error: No se encuentra el archivo MUNICIPIOS.xlsx')
    sys.exit(1)
except Exception as e:
    print(f'❌ Error al leer el archivo: {e}')
    sys.exit(1)

# ==================== BUSCAR COLUMNAS ====================
# Identificar columnas
col_codigo = None
col_nombre = None
col_provincia = None

for col in df.columns:
    col_upper = col.upper()
    if 'COD' in col_upper and 'INE' in col_upper:
        col_codigo = col
    if 'NOMBRE' in col_upper or 'ACTUAL' in col_upper:
        col_nombre = col
    if 'PROVINCIA' in col_upper:
        col_provincia = col

print(f'🔍 Columnas identificadas:')
print(f'   - Código: {col_codigo}')
print(f'   - Nombre: {col_nombre}')
print(f'   - Provincia: {col_provincia}')

# ==================== FILTRAR POR CÓDIGO INE ====================
# Primero intentar filtrar por código INE
codigos_buscar = set(municipios_buscar.values())
df[col_codigo] = df[col_codigo].astype(str).str.zfill(6)

df_por_codigo = df[df[col_codigo].isin(codigos_buscar)].copy()

if len(df_por_codigo) > 0:
    print(f'\n✅ Encontrados {len(df_por_codigo)} municipios por código INE')
    df_resultado = df_por_codigo
else:
    print('\n⚠️ No se encontraron coincidencias por código INE. Intentando por nombre...')
    
    # ==================== FILTRAR POR NOMBRE ====================
    resultados = []
    no_encontrados = []
    
    # Crear diccionario de nombres del Excel normalizados
    excel_nombres = {}
    for idx, row in df.iterrows():
        nombre_excel = str(row[col_nombre])
        nombre_norm = normalizar_nombre(nombre_excel)
        excel_nombres[nombre_norm] = (idx, row)
    
    # Buscar cada municipio
    for nombre_buscar, codigo in municipios_buscar.items():
        nombre_norm = normalizar_nombre(nombre_buscar)
        
        # Búsqueda exacta normalizada
        if nombre_norm in excel_nombres:
            idx, row = excel_nombres[nombre_norm]
            resultados.append(row)
        else:
            # Búsqueda parcial (para casos como "Donostia / San Sebastián")
            encontrado = False
            for nombre_excel_norm, (idx, row) in excel_nombres.items():
                # Si el nombre buscado está contenido en el nombre del Excel o viceversa
                if (nombre_norm in nombre_excel_norm or nombre_excel_norm in nombre_norm) and len(nombre_norm) > 3:
                    resultados.append(row)
                    encontrado = True
                    print(f'   🔄 Coincidencia parcial: "{nombre_buscar}" → "{row[col_nombre]}"')
                    break
            
            if not encontrado:
                no_encontrados.append((nombre_buscar, codigo))
    
    if resultados:
        df_resultado = pd.DataFrame(resultados)
        print(f'\n✅ Encontrados {len(df_resultado)} municipios por nombre')
    else:
        print('\n❌ No se encontraron coincidencias por nombre.')
        df_resultado = pd.DataFrame()

# ==================== VERIFICAR NO ENCONTRADOS ====================
encontrados_codigos = set(df_resultado[col_codigo].astype(str).str.zfill(6).tolist()) if not df_resultado.empty else set()
buscados_codigos = set(municipios_buscar.values())
no_encontrados_codigos = buscados_codigos - encontrados_codigos

if no_encontrados_codigos:
    print('\n⚠️ MUNICIPIOS NO ENCONTRADOS:')
    for nombre, codigo in municipios_buscar.items():
        if codigo in no_encontrados_codigos:
            print(f'   - {nombre} (código: {codigo})')
else:
    print('\n✅ Todos los municipios fueron encontrados.')

# ==================== SELECCIONAR COLUMNAS ====================
if not df_resultado.empty:
    # Seleccionar columnas de interés
    columnas_interes = [col_codigo, col_nombre]
    if col_provincia:
        columnas_interes.append(col_provincia)
    
    # Buscar columnas adicionales
    for col in df_resultado.columns:
        col_upper = col.upper()
        if 'SUPERFICIE' in col_upper and col not in columnas_interes:
            columnas_interes.append(col)
        if 'PERIMETRO' in col_upper and col not in columnas_interes:
            columnas_interes.append(col)
        if 'LONGITUD' in col_upper and col not in columnas_interes:
            columnas_interes.append(col)
        if 'LATITUD' in col_upper and col not in columnas_interes:
            columnas_interes.append(col)
        if 'ALTITUD' in col_upper and col not in columnas_interes:
            columnas_interes.append(col)
    
    df_final = df_resultado[columnas_interes].copy()
    
    # Renombrar columnas para claridad
    renombres = {
        col_codigo: 'COD_INE',
        col_nombre: 'NOMBRE'
    }
    if col_provincia:
        renombres[col_provincia] = 'PROVINCIA'
    
    df_final = df_final.rename(columns=renombres)
    
    # Limpiar formato numérico (convertir comas a puntos)
    for col in df_final.columns:
        if col not in ['COD_INE', 'NOMBRE', 'PROVINCIA']:
            df_final[col] = df_final[col].astype(str).str.replace(',', '.').str.replace(' ', '')
    
    # Ordenar por código INE
    df_final = df_final.sort_values('COD_INE')
    
    # ==================== GUARDAR RESULTADOS ====================
    df_final.to_csv('municipios_datos.csv', index=False, encoding='utf-8-sig', sep=';')
    print(f'\n📁 Datos guardados en: municipios_datos.csv')
    print(f'📊 Total de municipios encontrados: {len(df_final)}')
    print(f'📊 Total de municipios buscados: {len(municipios_buscar)}')
    
    # Mostrar resumen
    print('\n📋 RESUMEN DE DATOS (primeros 10):')
    print(df_final.head(10).to_string(index=False))
    
    # ==================== GENERAR ARCHIVOS SEPARADOS ====================
    # Latitudes
    if 'LATITUD' in df_final.columns:
        df_lat = df_final[['COD_INE', 'NOMBRE', 'LATITUD']].copy()
        df_lat.to_csv('latitudes.csv', index=False, encoding='utf-8-sig', sep=';')
        print(f'📁 Latitudes guardadas en: latitudes.csv')
    
    if 'LONGITUD' in df_final.columns:
        df_lon = df_final[['COD_INE', 'NOMBRE', 'LONGITUD']].copy()
        df_lon.to_csv('longitudes.csv', index=False, encoding='utf-8-sig', sep=';')
        print(f'📁 Longitudes guardadas en: longitudes.csv')
else:
    print('\n❌ No se encontraron datos para ningún municipio.')
    print('Verifica que el archivo MUNICIPIOS.xlsx contiene los municipios buscados.')
