import os 
import numpy as np
from six.moves import cPickle as pickle
import tensorflow as tf

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

def load_CIFAR_batch(filename):
    """ load single batch of cifar """
    with open(filename, 'rb') as f:
        datadict = pickle.load(f, encoding="latin1")
        X = datadict['data']
        Y = datadict['labels']
        X = X.reshape(10000,32,32,3, order="F")
        X = X.transpose((0, 2, 1, 3))
        Y = np.array(Y)
        return X, Y
        
def load_CIFAR10(dirname="cifar-10-batches-py"):
    """ load all of cifar """
    path = dirname
    
    num_train_samples = 50000

    x_train = np.empty((num_train_samples,32, 32, 3), dtype="uint8")
    y_train = np.empty((num_train_samples,), dtype="uint8")

    for i in range(1, 6):
        fpath = os.path.join(path, "data_batch_" + str(i))
        (
            x_train[(i - 1) * 10000 : i * 10000, :, :, :],
            y_train[(i - 1) * 10000 : i * 10000],
        ) = load_CIFAR_batch(fpath)

    fpath = os.path.join(path, "test_batch")
    x_test, y_test = load_CIFAR_batch(fpath)

    y_train = np.reshape(y_train, (len(y_train), 1))
    y_test = np.reshape(y_test, (len(y_test), 1))

    x_train = x_train.transpose(0, 2, 3, 1)
    x_test = x_test.transpose(0, 2, 3, 1)

    x_test = x_test.astype(x_train.dtype)
    y_test = y_test.astype(y_train.dtype)

    return (x_train, y_train), (x_test, y_test)