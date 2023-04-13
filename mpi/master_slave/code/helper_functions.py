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
#     nets = load_nets('cnn_nets/cnn_nets.yml')
    
    
#     print(nets[2])