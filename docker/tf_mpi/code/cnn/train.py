#Importing required libararies
from cnn.utils import disable_tf_logging

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import mixed_precision
from cnn.create_model import create_vgg
import time

# Enable mixed precision
mixed_precision.set_global_policy('mixed_float16')

# Enable memory growth for GPU 
# https://www.tensorflow.org/guide/gpu
gpu_names = []
gpus = tf.config.list_physical_devices('GPU')
if gpus:
  try:
    # Currently, memory growth needs to be the same across GPUs
    for gpu in gpus:
      tf.config.experimental.set_memory_growth(gpu, True)
    logical_gpus = tf.config.list_logical_devices('GPU')
    #print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
  except RuntimeError as e:
    # Memory growth must be set before GPUs have been initialized
    print(e)
  gpu_names = [gpu.name for gpu in logical_gpus]

# Disable tensorflow logging
disable_tf_logging()

def calculate_fitness(train_data, test_data, num_classes, net, params, worker):
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
    gpu_name = gpu_names[worker % len(gpu_names)]
    print(f"Worker {worker} is training with GPU {gpu_name}")
  

    x_train, y_train = train_data
    x_test, y_test = test_data
        # Normalization is donde in create vgg function
    try:
      with tf.device(gpu_name):
        model = create_vgg(x_train.shape[1:], num_classes, net)
        model.compile(optimizer=keras.optimizers.Adam(learning_rate=params['lr']),
                      loss=params['loss'],
                      metrics=['accuracy'])
        # Train model
        train_start = time.perf_counter()        
        history = model.fit(x_train, y_train, 
                  epochs=params['epochs'],
                  validation_data=test_data,
                  batch_size=params['batch_size'],
                  verbose=0)
        
        total_time =  round((time.perf_counter() - train_start) / 60.0,2)
        print(f"Training time Worker {worker}: {total_time} minutes")
        # Evaluate model
        _, fitness = model.evaluate(x_test, y_test, verbose=0)
    except RuntimeError as e:
      print(e)
      fitness = 0
    return fitness