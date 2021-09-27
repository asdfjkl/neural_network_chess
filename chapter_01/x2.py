import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import random

random.seed(42)
np.random.seed(42)
tf.random.set_seed(42)

x = []
y = []
for i in range(0,10000):
    xi = random.randint(0,5000)
    xi = xi/100
    if(xi==2.0 or xi==4.0):
        continue
    yi = xi**2
    x.append([xi])
    y.append(yi)

print(np.array(x)[0:20])

model = tf.keras.models.Sequential()
model.add(tf.keras.Input(shape=(1,)))
model.add(tf.keras.layers.Dense(units=8, activation="relu"))
model.add(tf.keras.layers.Dense(units=8, activation="relu"))
model.add(tf.keras.layers.Dense(units=1, activation="linear"))
print(model.summary())

model.compile(optimizer=keras.optimizers.Adam(),
              loss=keras.losses.MeanSquaredError())


print(np.array(x).shape)

model.fit(np.array(x), np.array(y),
          batch_size=256, epochs=5000)


q = model.predict( np.array( [[2],[4]] )  )
print(q)

original = [ x**2 for x in range(0,50)]

plt.figure()
plt.plot(original)
plt.show()

predicted = model.predict(np.array([ x for x in range(0,50) ]))

plt.figure()
plt.plot(predicted)
plt.show()

