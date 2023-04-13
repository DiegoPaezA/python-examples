import yaml
import os

def load_nets(net_file):
    """
    Load the CNN nets from a YAML file and return a list of dict with each net.
    
    Args:
        net_file (str): path to the YAML file
    Returns: 
        nets (list): list of dict with CNN nets
    """
    with open(net_file, 'r') as f:
        net = yaml.safe_load(f)
    net_keys = list(net.keys())
    nets = []    
    for key in net_keys:
        nets.append(net[key])
        
    return nets

def load_params(param_file):
    """
    Load the parameters from a YAML file and return a dict with the parameters.
    
    Args:
        param_file (str): path to the YAML file
    Returns: 
        params (dict): dictionary with the parameters
    """
    with open(param_file, 'r') as f:
        params = yaml.safe_load(f)
    return params

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

# if __name__ == '__main__':
#     nets = load_params('cnn_nets/cnn_params.yml')
#     print(list(nets.keys()))