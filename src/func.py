import pandas as pd



def fill_years(df_list, years_list):
    """
    Rellena los valores nulos en la columna 'ANO EXERCÍCIO' de una lista de DataFrames 
    con los valores proporcionados en una lista de años.

    Args:
        df_list (list of pd.DataFrame): Lista de DataFrames que contienen la columna 'ANO EXERCÍCIO'.
        years_list (list of int or float): Lista de años que se utilizarán para reemplazar los valores nulos 
                                           en cada DataFrame correspondiente.

    Returns:
        list of pd.DataFrame: Lista de DataFrames con la columna 'ANO EXERCÍCIO' sin valores nulos.
    
    """
    clean_dfs = []
    i = 0
    for df in df_list:
        df["ANO EXERCÍCIO"] = df["ANO EXERCÍCIO"].fillna(years_list[i])
        clean_dfs.append(df)
        i+=1
    return clean_dfs

def decimal_point_conv(data, columns):
    """
    Convierte los valores en columnas específicas de un DataFrame de un formato 
    con punto decimal en coma a un formato con punto decimal y los transforma a valores 
    numéricos de tipo float.

    Args:
        data (pd.DataFrame): DataFrame que contiene las columnas a ser convertidas.
        columns (list of str): Lista de nombres de columnas que se convertirán.

    Returns:
        None: La función modifica el DataFrame `data` en su lugar, 
              convirtiendo los valores de las columnas especificadas.
    """
    for col in columns:
        data[col] = data[col].str.replace(",",".").apply(float).abs().round(2)

def check_date_consistency(dataframe_list):
    """
    Verifica la consistencia de las fechas en una lista de DataFrames comparando el año 
    extraído de la columna 'DATA LANÇAMENTO' con el año en la columna 'ANO EXERCÍCIO'.

    Args:
        dataframe_list (list of pd.DataFrame): Lista de DataFrames que contienen las columnas 
                                                'DATA LANÇAMENTO' y 'ANO EXERCÍCIO'.

    Returns:
        list of int: Lista de diferencias entre la cantidad de inconsistencias 
                      (años no coincidentes) y la cantidad de valores nulos en 
                      'DATA LANÇAMENTO' para cada DataFrame.

    """
    diffs = []
    for df in dataframe_list:
        years_from_date = pd.to_datetime(df["DATA LANÇAMENTO"], format="%d/%m/%Y").dt.year
        years = df["ANO EXERCÍCIO"]
        boolean_series = years != years_from_date
        sum_bool = boolean_series.sum()
        nas = df["DATA LANÇAMENTO"].isna().sum()
        diff = sum_bool-nas
        diffs.append(diff)
    return diffs

def dict_codes_gen(code, name):
    """
    Genera un diccionario a partir de dos listas, asociando códigos con nombres. 
    Si un código o nombre es NaN, o el código ya está en el diccionario, se omite.

    Args:
        code (list): Lista de códigos que se utilizarán como claves en el diccionario.
        name (list): Lista de nombres que se asociarán como valores a los códigos.

    Returns:
        dict: Diccionario que asocia cada código con su nombre correspondiente, 
              omitiendo valores NaN y códigos duplicados.
    """
    dict_codes = dict()
    for i in range(len(code)):
        if pd.isna(code[i]) or pd.isna(name[i]) or code[i] in dict_codes.keys():
            continue
        else:
            dict_codes[code[i]] = name[i]
    return dict_codes



def subcategory(fila):
    """
    Determina la subcategoría económica de una fila en función de la columna 'economy_category'.

    Args:
        fila (dict or pd.Series): Fila que contiene una columna 'economy_category' con información económica.

    Returns:
        str: 
            - 'sem informação' si la categoría económica es 'Sem informação'.
            - 'intra-orçamentárias' si la categoría económica contiene 'intra-orçamentárias'.
            - 'extra-orçamentárias' en cualquier otro caso.
    """
    if fila['economy_category'] == 'Sem informação':
        return 'sem informação'
    elif 'intra-orçamentárias' in fila['economy_category']:
        return 'intra-orçamentárias'
    else:
        return 'extra-orçamentárias'
    

    