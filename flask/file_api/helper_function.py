import os

def check_file_exists(file_name: str):
    """
    _summary_

    Args:
        file_name (str): _description_

    Returns:
        bool: True if file exists, False if file doesn't exist.
    """
    if(os.path.exists(file_name)):
        return True
    else:
        return False