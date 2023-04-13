#Importing required libararies
import sys
sys.path.insert(1, '/home/diripar8/python-examples/mpi/master_slave/code/')
import helper_functions as hf

import tensorflow as tf
from tensorflow import keras
from create_model import create_vgg


# Disable tensorflow logging
hf.disable_tf_logging()

def calculate_fitness(net, params):
    """
    This function calculates the fitness of a model

    Args:
        net (dict): dictionary with the CNN architecture
        params (dict): dictionary with the CNN training parameters

    Returns:
        fitness (float): fitness of the model
    """
    # Compile model
    x_train, y_train, x_test, y_test = keras.datasets.cifar10.load_data()
    
    model = create_vgg(x_train.shape[1:], y_train.shape[1], net)
    
    model.compile(optimizer=keras.optimizers.Adam(lr=params['lr']),
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    # Train model
    model.fit(x_train, y_train, epochs=params['epochs'], batch_size=params['batch_size'], verbose=0)

    # Evaluate model
    _, fitness = model.evaluate(x_test, y_test, verbose=0)
    return fitness