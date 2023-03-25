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
    
def add_data_to_csv(data:dict, filename:str, mode:str="w"):
    """_summary_

    Args:
        data (dict): data to be added to the csv file
        filename (str): filename to be created or appended
        mode (str, optional): Select between "w" to write or "a" to append. Defaults to "w".
    """
    filename_path = "files/" + filename
    data_frame = pd.DataFrame.from_dict(data)
    
    if mode == "w":
        data_frame.to_csv(filename_path, index=False)
    elif mode == "a":
        data_frame.to_csv(filename_path, index=False, header=False, mode="a")
        
def check_file_type(filename:str):
    """_summary_

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