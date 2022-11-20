import os
from dotenv import load_dotenv
import pandas as pd
import geopandas as gpd

load_dotenv()


def data_from_sheet(key: str, sheet: str, start_column: chr, start_line: int, end_column: chr, end_line: int,
                    names: list = None, converters: dict = None) -> pd.DataFrame:
    df = pd.read_csv("https://docs.google.com/spreadsheets/d/" +
                     key +
                     "/gviz/tq?tqx=out:csv&range=" + start_column + str(start_line) + ":" + end_column + str(end_line) +
                     "&sheet=" +
                     sheet,
                     names=names,
                     converters=converters
                     )
    # df.columns = df.columns.str.replace("\n","")
    df.columns = df.columns.str.strip()

    return df


def add_properties(properties: dict, dataframe: pd.DataFrame, subject: str, sub_subject: str,
                   final_columns: list = None) -> dict:
    """Add data from DataFrame to the argument `properties`, e.g.: properties.subject.subSubject

    A `properties` dictionary like this:
    properties = {
        "id": [],
        "name": [],
        "A_Subject": [],
        "geometry": []
    }

    A DataFrame like this:
    index |   id,   name,   average,   useless_data|
    -----------------------------------------------|
        0 | id_0, name_0, average_0, useless_data_0|
        1 | id_1, name_1, average_1, useless_data_1|
        2 | id_2, name_2, average_2, useless_data_2|
        3 | id_3, name_3, average_3, useless_data_3|

    Call the function like this: add_properties(properties, dataframe, "A_Subject", "A_Subsubject", ["average"] )

    Result:
    properties = {
        "id": [id_0, id_1, id_2, id_3],
        "name": [name_0, name_1, name_2, name_3],
        "A_Subject": [
            {
                "A_Subsubject": {"average": average_0}
            },
            {
                "A_Subsubject": {"average": average_1}
            },
            {
                "A_Subsubject": {"average": average_2}
            },
            {
                "A_Subsubject": {"average": average_3}
            }
        ],
        "geometry": []
    }

    Parameters
        ----------
        properties : dict
            Dictionary used for generate the GeoDataFrame, it contains all data and the `geometry` column
        dataframe : pandas.DataFrame
            Data to add to the `properties` dictionary
        subject : str
            Subject used as name of column (e.g. Befolkning)
        sub_subject : str
            Subsbuject used to categorize subjects within a larger
        final_columns : list
            The final data to keep

    Return
        ---------
        A Dictionary fill with data
    """

    for column_name in dataframe:
        if column_name in properties.keys():
            if len(properties[column_name]) == 0: properties[column_name] = dataframe[column_name].to_list()
        elif len(final_columns) == 0 or column_name in final_columns:
            values = dataframe[column_name].to_list()
            for i in range(len(values)):
                if len(properties[subject]) <= i:
                    properties[subject].append({sub_subject: {column_name: values[i]}})
                elif sub_subject not in properties[subject][i].keys():
                    properties[subject][i][sub_subject] = {column_name: values[i]}
                else:
                    properties[subject][i][sub_subject][column_name] = values[i]
    return properties


def add_geometry_column(properties: dict, geodataframe: gpd.GeoDataFrame, id_property: str = "Levekårsnavn",
                        id_geo: str = "levekårsone") -> dict:
    """Add data to `geometry` column

    Fill the `geometry` column of the `properties` dictionary with the geometry data of `geodataframe`.
    Use the `idProperty` and `idGeo` to match data and geometry

    A `properties` dictionary like this:
    properties = {
        "id": [id_0, id_1, id_2, id_3],
        "geometry": []
    }

    A GeoDataFrame like this:
    index | special_id, ...data...,   geometry|
    ------------------------------------------|
        0 |       id_0, ...data..., geometry_0|
        1 |       id_1, ...data..., geometry_1|
        2 |       id_2, ...data..., geometry_2|
        3 |       id_3, ...data..., geometry_3|

    Call the function like this: add_geometry_column(properties, geodataframe, "id", "special_id" )

    Result:
    properties = {
        "id": [id_0, id_1, id_2, id_3],
        "geometry": [geometry_0, geometry_1, geometry_2, geometry_3]
    }

    Parameters
        ----------
        properties : dict
            Dictionary used for generate the GeoDataFrame, it contains all data and the `geometry` column
        geodataframe : geopandas.GeoDataFrame
            GeoDataFrame with all data for the `geometry` column
        id_property : str, optional
            The id column used in the `properties` dictionary
        id_geo : str, optional
            The id column used in the GeoDataFrame object
    Return
        ---------
        A Dictionary fill with geometry data
    """
    for name in properties[id_property]:
        for j in range(len(geodataframe[id_geo])):
            if name == geodataframe[id_geo][j]:
                properties["geometry"].append(geodataframe["geometry"][j])
    return properties


def create_geodataframe(properties: dict, sheets: dict, geodataframe: gpd.GeoDataFrame, final_columns: list,
                        converters: dict) -> gpd.GeoDataFrame:
    for subject in sheets.keys():
        for subSubject, page in sheets[subject]["values"].items():
            dataframe = data_from_sheet(sheets[subject]["key"], page, "A", 9, "G", 69, converters=converters)
            properties = add_properties(properties, dataframe, subject, subSubject, final_columns)
    properties = add_geometry_column(properties, geodataframe)
    return gpd.GeoDataFrame(properties, crs=os.getenv("CRS"))


def create_interval_dataframe(properties: dict, sheets: dict, final_columns: list, converters: dict) -> pd.DataFrame:
    for subject in sheets.keys():
        for subSubject, page in sheets[subject]["values"].items():
            dataframe = data_from_sheet(sheets[subject]["key"], page, "A", 80, "B", 85, converters=converters)
            properties = add_properties(properties, dataframe, subject, subSubject, final_columns)
    return pd.DataFrame(properties)


def create_trondheim_json(properties: dict, sheets: dict, final_columns: list, converters: dict, renaming: dict) -> dict:
    for subject in sheets.keys():
        for sub_subject, page in sheets[subject]["values"].items():
            dataframe = data_from_sheet(sheets[subject]["key"], page, "G", 9, "H", 10, converters=converters)
            properties = add_properties(properties, dataframe, subject, sub_subject, final_columns)
            for old_name, new_name in renaming.items():
                if old_name in properties[subject][0][sub_subject]:
                    properties[subject][0][sub_subject][new_name] = properties[subject][0][sub_subject].pop(old_name)
        properties[subject] = properties[subject][0]
    return properties
