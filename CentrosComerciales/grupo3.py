"""Módulo del grupo 3 para realización de las consultas"""

import pandas as pd

def filtro_columnas_temporalidad(year, quarter, month):
    """Función para filtrar columnas de temporalidad"""

    columnas_groupby_temporalidad = []
    if year:
        columnas_groupby_temporalidad.append('A¤o')

    if quarter:
        columnas_groupby_temporalidad.append('Trimestre')

    if month:
        columnas_groupby_temporalidad.append('Mes ')
    
    return columnas_groupby_temporalidad

def filtro_columnas_ids(provincia, centro, division, departamento):
    """Función para filtrar columnas de ids"""
    columnas_groupby_ids = []
    if provincia:
        columnas_groupby_ids.append('ProvinciaId')

    if centro:
        columnas_groupby_ids.append('CentroId')

    if division:
        columnas_groupby_ids.append('DivisionId')

    if departamento:
        columnas_groupby_ids.append('DepartamentoId')

    return columnas_groupby_ids


class Grupo3:
    """Módulo de la consulta 13"""

    def __init__(self, df_input: pd.DataFrame) -> None:
        self.df_input = df_input
        self.dataframe = None
        self.add_quarter()

    def add_quarter(self):
        """Método para agregar columna trimestre en base al mes"""
        self.df_input["Trimestre"] = self.df_input["Mes "].apply(lambda x: 1 if int(x) <= 3 else (2 if int(x) <= 6 else (3 if int(x) <= 9 else 4)))


    @staticmethod
    def filtro_temporalidad(df, year, quarter, month):
        """Filtrar por año, trimestre y mes si es necesario
        (Se ha hecho con staticmethod para poder meter el dataframe que se quiera filtrar)
        """
        df_result = df.copy()
        if year is not None:
            df_result = df_result[df_result['A¤o'] == year]

        if quarter is not None:
            df_result = df_result[df_result['Trimestre'] == quarter]

        if month is not None:
            df_result = df_result[df_result['Mes '] == month]
        
        return df_result

    @staticmethod
    def filtro_ids(df, provincia, centro, division, departamento):
        """Filtrar por ids si es necesario
        (Se ha hecho con staticmethod para poder meter el dataframe que se quiera filtrar)
        """
        df_result = df.copy()
        if provincia is not None:
            df_result = df_result[df_result['ProvinciaId'] == provincia]

        if centro is not None:
            df_result = df_result[df_result['CentroId'] == centro]

        if division is not None:
            df_result = df_result[df_result['DivisionId'] == division]

        if departamento is not None:
            df_result = df_result[df_result['DepartamentoId'] == departamento]

        return df_result


    def filtrar_ventas(self, provincia=None, centro=None, division=None, departamento=None, year=None, quarter=None, month=None):
        """Filtrar tabla de ventas por ids y temporalidad"""
        self.dataframe = self.filtro_ids(self.df_input, provincia, centro, division, departamento)
        self.dataframe = self.filtro_temporalidad(self.dataframe, year, quarter, month)
        column_order = ['ProvinciaId', 'CentroId', 'DivisionId', 'DepartamentoId', 'A¤o', 'Trimestre', 'Mes ', 'Visitas']
        self.dataframe = self.dataframe[column_order]



    def groupby(self, provincia=None, centro=None, division=None, departamento=None, year=None, quarter=None, month=None):
        """Agrupar por ids y temporalidad"""
        columnas_groupby_ids = filtro_columnas_ids(provincia, centro, division, departamento)
        # columnas_groupby_ids = ['ProvinciaId', 'CentroId', 'DivisionId', 'DepartamentoId']
        columnas_groupby_temporalidad = filtro_columnas_temporalidad(year, quarter, month)

        self.filtrar_ventas(provincia, centro, division, departamento, year, quarter, month)

        result = self.dataframe.groupby(columnas_groupby_ids + columnas_groupby_temporalidad)['Visitas'].sum().reset_index()
        return result
