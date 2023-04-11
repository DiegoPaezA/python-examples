#Importing required libararies
import os
import tensorflow as tf
from tensorflow import keras
#Loading Fashion MNIST dataset
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.fashion_mnist.load_data()
#creating a smaller dataset 
train_labels = train_labels[:1000]
test_labels = test_labels[:1000]
#Normalizing the dataset
train_images = train_images[:1000].astype('float32') / 255
test_images = test_images[:1000].astype('float32') / 255
# Reshaping the data for inputing into the model
train_images = train_images.reshape((train_images.shape[0],  28, 28,1))
test_images = test_images.reshape((test_images.shape[0],  28, 28,1))
#Defining and compiling the keras model
def create_model():
    model = tf.keras.Sequential()
    # Must define the input shape in the first layer of the neural network
    model.add(tf.keras.layers.Conv2D(filters=64, kernel_size=2, padding='same', activation='relu', input_shape=(28,28,1))) 
    model.add(tf.keras.layers.MaxPooling2D(pool_size=2))
    model.add(tf.keras.layers.Dropout(0.3))
    model.add(tf.keras.layers.Conv2D(filters=32, kernel_size=2, padding='same', activation='relu'))
    model.add(tf.keras.layers.MaxPooling2D(pool_size=2))
    model.add(tf.keras.layers.Dropout(0.3))
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(256, activation='relu'))
    model.add(tf.keras.layers.Dropout(0.5))
    model.add(tf.keras.layers.Dense(10, activation='softmax'))
    
    #Compiling the model
    model.compile(loss='sparse_categorical_crossentropy',
             optimizer='adam',
             metrics=['accuracy'])
    
    return model
# Create a basic model instance
model = create_model()
model.summary()

#Fit the train data to the model
model.fit(train_images, 
          train_labels,  
          batch_size=64,
          epochs=100,
          validation_data=(test_images,test_labels))

from keras.models import model_from_json
# serialize model to json
json_model = model.to_json()
#save the model architecture to JSON file
with open('fashionmnist_model.json', 'w') as json_file:
    json_file.write(json_model)
#saving the weights of the model
model.save_weights('FashionMNIST_weights.h5')
#Model loss and accuracy
loss,acc = model.evaluate(test_images,  test_labels, verbose=2)

from keras.initializers import glorot_uniform
#Reading the model from JSON file
with open('fashionmnist_model.json', 'r') as json_file:
    json_savedModel= json_file.read()
#load the model architecture 
model_j = tf.keras.models.model_from_json(json_savedModel)
model_j.summary()