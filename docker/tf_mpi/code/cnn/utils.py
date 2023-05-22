import os 

def disable_tf_logging(level:int=1):
    """
    Disable tensorflow logging
    Args:
    Level (int): level of logging
    
        0 = all messages are logged.
        1= INFO logs are removed.
        2 = INFO with WARNINGS is removed.
        3= ALL messages are removed.
    """
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = str(level) 