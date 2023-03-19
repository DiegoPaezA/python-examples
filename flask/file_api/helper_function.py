import os

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