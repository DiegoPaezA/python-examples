#Importing required libararies
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense, Input, Conv2D, MaxPool2D, GlobalAveragePooling2D
from tensorflow.keras.models import Model

print(f"Tensorflow version: {tf.__version__}")

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

(X_train, y_train), (X_test, y_test) = keras.datasets.cifar10.load_data()

input_layer = Input(shape=(32,32,3))
x = vgg_block(input_layer, 64, 2)
x = vgg_block(x, 128, 2)
x = vgg_block(x, 256, 3)
x = GlobalAveragePooling2D()(x)
output_layer = Dense(10, activation='softmax')(x)

model = Model(input_layer, output_layer)
print(model.summary())

'''
model.compile(loss="SparseCategoricalCrossentropy",
              optimizer= keras.optimizers.Adam(), 
              metrics=["accuracy"])

history = model.fit(x=X_train, y=y_train, 
                    batch_size=256, 
                    epochs=10, 
                    validation_data=(X_test, y_test), 
                    verbose=1)
                    '''
