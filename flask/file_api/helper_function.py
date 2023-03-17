import os

def check_file_exists(file_name: str):
    """
    _summary_

    Args:
        dataframe (pandas Dataframe): _description_
        file_name (str): _description_

    Returns:
        bool: True if file exists, False if file doesn't exist.
    """
    if(os.path.exists(file_name)):
        print('File already exists.')
        return True
    else:
        print(f"File doesn't exist.")
        return False