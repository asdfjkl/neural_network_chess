import numpy as np
import tensorflow as tf
from tensorflow import keras
import random

random.seed(42)
np.random.seed(42)
tf.random.set_seed(42)

x = []
y = []

x = [[0,0],[0,1],[1,0],[1,1]]
y = [ 0, 0, 0, 1]

model = tf.keras.models.Sequential()
model.add(tf.keras.Input(shape=(2,)))
model.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))
print(model.summary())

model.compile(optimizer=keras.optimizers.SGD(learning_rate=0.1),
              loss=keras.losses.MeanSquaredError())

print(np.array(x).shape)

model.fit(np.array(x), np.array(y),
          batch_size=4, epochs=50000)


q = model.predict( np.array( [[0,1],[1,1]] )  )
print(q)