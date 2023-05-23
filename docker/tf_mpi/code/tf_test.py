import tensorflow as tf
from tensorflow.python.client import device_lib

print("**"*20)
print("*** TF Test ***")
print("TF Version: ", tf.__version__)
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
device_lib.list_local_devices()
print("**"*20)