#Importing required libararies
import sys
sys.path.insert(1, '/home/diripar8/python-examples/mpi/master_slave/code/')
import helper_functions as hf

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import mixed_precision
from create_model import create_vgg

import matplotlib.pyplot as plt

# Enable mixed precision
mixed_precision.set_global_policy('mixed_float16')

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
    # Load data - CIFAR10
    num_classes = 10
    (x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data()
    # Normalization is donde in create vgg function
    model = create_vgg(x_train.shape[1:], num_classes, net)
    
    model.compile(optimizer=keras.optimizers.Adam(learning_rate=params['lr']),
                  loss=params['loss'],
                  metrics=['accuracy'])
    
    # Train model
    print("Training model...")
    history = model.fit(x_train, y_train, 
              epochs=params['epochs'],
              validation_data=(x_test, y_test),
              batch_size=params['batch_size'], 
              verbose=1)
    print("Model trained")

    # Evaluate model
    _, fitness = model.evaluate(x_test, y_test, verbose=0)
    return fitness, history;

if __name__ == '__main__':
    # Read parameters
    net = hf.load_nets("/home/diripar8/python-examples/mpi/master_slave/code/cnn_nets/cnn_nets.yml")
    params = hf.load_params("/home/diripar8/python-examples/mpi/master_slave/code/cnn_nets/cnn_params.yml")  
    fitness_results = []
    history_results = []
    # Calculate fitness
    for i in range(len(net)):
        fitness, history = calculate_fitness(net[i], params[0])
        fitness_results.append(fitness)
        history_results.append(history)
        print(f"Fitness of Net_{i+1}: {fitness}")
        
    for i in range(len(fitness_results)):
        print(f"Fitness of Net_{i+1}: {fitness_results[i]}")    