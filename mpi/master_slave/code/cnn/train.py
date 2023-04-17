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

def calculate_fitness(train_data, test_data, num_classes, net, params):
    """
    This function calculates the fitness of a model

    Args:
        train_data (tuple): tuple with the training data
        test_data (tuple): tuple with the test data
        num_classes (int): number of classes
        net (dict): dictionary with the CNN architecture
        params (dict): dictionary with the CNN training parameters

    Returns:
        fitness (float): fitness of the model
    """
    x_train, y_train = train_data
    x_test, y_test = test_data
    # Normalization is donde in create vgg function
    model = create_vgg(x_train.shape[1:], num_classes, net)
    
    model.compile(optimizer=keras.optimizers.Adam(learning_rate=params['lr']),
                  loss=params['loss'],
                  metrics=['accuracy'])
    
    # Train model
    print("Training model...")
    history = model.fit(x_train, y_train, 
              epochs=params['epochs'],
              validation_data=test_data,
              batch_size=params['batch_size'], 
              verbose=1)
    print("Model trained")

    # Evaluate model
    _, fitness = model.evaluate(x_test, y_test, verbose=0)
    return fitness, history;

if __name__ == '__main__':
    # Read parameters
    
    # Load data - CIFAR10
    num_classes = 10
    train_data, test_data = keras.datasets.cifar10.load_data()
    
    # Load nets and params
    net = hf.load_nets("/home/diripar8/python-examples/mpi/master_slave/code/cnn_nets/cnn_nets.yml")
    params = hf.load_params("/home/diripar8/python-examples/mpi/master_slave/code/cnn_nets/cnn_params.yml")  
    fitness_results = []
    history_results = []
    
    # Calculate fitness
    for i in range(len(net)):
        fitness, history = calculate_fitness(train_data,test_data,num_classes,net[1], params[0])
        fitness_results.append(fitness)
        history_results.append(history)
        print(f"Fitness of Net_{i+1}: {fitness}")
        
    print("n/ Results Resume:")    
    for i in range(len(fitness_results)):
        print(f"Fitness of Net_{i+1}: {fitness_results[i]}")