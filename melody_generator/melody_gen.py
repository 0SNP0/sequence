import tensorflow as tf
from tensorflow import keras
import numpy as np
#import matplotlib.pyplot as plt

train_in = np.array([[1.0, 6.0, 5.0, 0.5, 1.0, 0.1]])
train_out = np.array([2.0])
test_in, test_out = train_in, train_out

model = keras.Sequential([
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(7, activation=tf.nn.softmax)
])

model.compile(optimizer=tf.train.AdamOptimizer(),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_in, train_out, epochs=5)

test_loss, test_acc = model.evaluate(test_in, test_out)
print('Test accuracy:', test_acc)
predictions = model.predict(test_in)
predictions = model.predict(test_in)
print(predictions)
print(np.argmax(predictions))

model.save_weights('./checkpoints/model')