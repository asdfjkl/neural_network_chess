from keras.models import Model
from keras.layers import *
import numpy as np
import tensorflow as tf

inp = Input((21,))

l1 = Dense(128, activation='relu')(inp)
l2 = Dense(128, activation='relu')(l1)
l3 = Dense(128, activation='relu')(l2)
l4 = Dense(128, activation='relu')(l3)
l5 = Dense(128, activation='relu')(l4)

policyOut = Dense(28, name='policyHead', activation='softmax')(l5)
valueOut = Dense(1, activation='tanh', name='valueHead')(l5)

bce = tf.keras.losses.CategoricalCrossentropy(from_logits=False)
model = Model(inp, [policyOut,valueOut])
model.compile(optimizer = 'SGD', loss={'valueHead' : 'mean_squared_error', 'policyHead' : bce})

inputData = np.load("positions.npy")
policyOutcomes = np.load("moveprobs.npy")
valueOutcomes = np.load("outcomes.npy")

print(policyOutcomes.shape)
print(inputData.shape)

model.fit(inputData,[policyOutcomes, valueOutcomes], epochs=512, batch_size=16)
model.save('supervised_model.keras')
