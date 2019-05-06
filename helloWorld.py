import tensorflow as tf
# helps us to represent our data as lists easily and quickly
import numpy as np
#  framework for defining a neural network as a set of Sequential layers
from tensorflow import keras

# The LOSS function measures the guessed answers against the known correct answers and measures how well or how badly it did
# then uses the OPTIMIZER function to make another guess. Based on how the loss function went, it will try to minimize the loss.
model = tf.keras.Sequential([keras.layers.Dence(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')
# providing data
xs = np.array([-1.0,0.0,1.0,2.0,3.0,4.0],dtype=float)
ys = np.array([-3.0,-1.0,1.0,3.0,5.0,7.0],dtype=float)