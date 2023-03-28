import os
import pandas as pd

def check_file_exists(file_name: str):
    """
    This function helps to check if the file that the user is trying to create
    its already in the folder.

    Args:
        file_name (str): file name

    Returns:
        bool: True if file exists, False if file doesn't exist.
    """
    if(os.path.exists(file_name)):
        return True
    else:
        return False
    
def add_data_to_csv(filename:str, data:dict, mode:str="w"):
    """
    Function to add data to a csv file

    Args:
        filename (str): filename to be created or appended
        data (dict): data to be added to the csv file
        mode (str, optional): Select between "w" to write or "a" to append. Defaults to "w".
    """
    filename_path = "files/" + filename
    data_frame = pd.DataFrame.from_dict(data)
    
    if mode == "w":
        data_frame.to_csv(filename_path, index=False)
    elif mode == "a":
        data_frame.to_csv(filename_path, index=False, header=False, mode="a")
    
    result = data_frame.to_json(orient="split", index=False)

    return result
        
def check_file_type(filename:str):
    """
    Function to check the file type

    Args:
        filename (str): filename to be checked

    Returns:
        str: file type
    """
    filename_path = "files/" + filename
    if filename_path.endswith(".csv"):
        return "csv"
    elif filename_path.endswith(".json"):
        return "json"
    elif filename_path.endswith(".txt"):
        return "txt"
    else:
        return "other"
    
def filter_csv(filename:str, column:str, value:float):
    """
    Function to filter a csv file by a column and a value

    Args:
        filename (str): filename to be filtered
        columns (str): column to be filtered
        value (float): value to be filtered

    Returns:
        result: filtered json
    """
    filename_path = "files/" + filename
    data_frame = pd.read_csv(filename_path)
    data_frame = data_frame[data_frame[column] < value]
    result = data_frame.to_json(orient="split", index=False)

    return result

def filter_range_csv(filename:str, value1:int, value2:int):
    """
    Function to filter a csv file by a column and a range of values

    Args:
        filename (str): filename to be filtered
        columns (str): column to be filtered
        value1 (int): lower value to be filtered
        value2 (int): upper value to be filtered

    Returns:
        result: filtered json
    """
    filename_path = "files/" + filename
    data_frame = pd.read_csv(filename_path)
    data_frame = data_frame.loc[value1:value2]
    result = data_frame.to_json(orient="split", index=False)

    return result