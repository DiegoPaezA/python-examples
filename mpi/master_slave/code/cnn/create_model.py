#Importing required libararies
import sys
sys.path.insert(1, '/home/diripar8/python-examples/mpi/master_slave/code/')
import helper_functions as hf

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense, Input, Conv2D, MaxPool2D, GlobalAveragePooling2D
from tensorflow.keras.models import Model


# Disable tensorflow logging
hf.disable_tf_logging()

def vgg_block(layer_in, n_filters, n_conv):
    """
    This function creates a VGG block

    Args:
        layer_in (keras.layers or input shape): input layer
        n_filters (int): number of filters
        n_conv (int): number of convolutional layers

    Returns:
        _type_: _description_
    """
    # add convolutional layers
    for _ in range(n_conv):
        layer_in = Conv2D(n_filters, (3,3), padding='same', activation='relu')(layer_in)
    # add max pooling layer
    layer_in = MaxPool2D((2,2), strides=(2,2))(layer_in)
    return layer_in

def add_vgg_block(layer_in, net):
    """
    This function adds a VGG blocks to the model

    Args:
        layer_in (keras.layers or input shape): input layer
        net (dict): dictionary with the CNN architecture

    Returns:
        x : output of the last vgg block
    """
    n_vgg_blocks = net['vgg_blocks'] # number of vgg blocks
    n_conv = net['conv_layers'] # number of convolutional layers
    n_filters = net['num_filters'] # number of filters
    
    for i in range(n_vgg_blocks):
        if n_vgg_blocks == 1:
            x = vgg_block(layer_in, n_filters[i], n_conv[i])
        else:
            x = vgg_block(layer_in, n_filters[i], n_conv[i])
            layer_in = x
    return x

def create_vgg(input_shape, num_classes, net):
    """
    This function creates a tiny vgg model

    Args:
        input_shape (tuple): input shape of the model (height, width, channels)
        num_classes (int): number of classes
        net (dict): dictionary with the CNN architecture

    Returns:
        model (keras.models.Model): model
    """
    # define model input
    input_layer = Input(input_shape)
    # add vgg blocks
    x= add_vgg_block(input_layer, net)
    # add global average pooling layer
    x = GlobalAveragePooling2D()(x)
    # add classifier
    output_layer = Dense(num_classes, activation='softmax')(x)
    # define model
    model = Model(input_layer, output_layer)
    return model


# if __name__ == '__main__':
    
#     net_1 = {'vgg_blocks': 1, 'conv_layers': [2], 'num_filters': [64]}
#     net_2 = {'vgg_blocks': 2, 'conv_layers': [2, 2], 'num_filters': [64, 128]}
#     net_3 = {'vgg_blocks': 3, 'conv_layers': [2, 2, 3], 'num_filters': [64, 128, 256]}
    
#     input_shape = (224,224,3)
#     num_classes = 10
#     test_model = create_vgg(input_shape,num_classes,net_3)




