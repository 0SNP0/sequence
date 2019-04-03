import tensorflow as tf
from tensorflow import keras
import numpy as np

class My_model:
    model = keras.Sequential([
        keras.layers.Dense(128, activation=tf.nn.relu),
        keras.layers.Dense(7, activation=tf.nn.softmax)
    ])

    def  __init__(self):
        model.compile(optimizer=tf.train.AdamOptimizer(), 
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy'])
        
    def train(train_in, train_out, epochs=5):
        self.model.fit(train_in, train_out, epochs=self.epochs)
    
    def eval(test_in, test_out):
        test_loss, test_acc = self.model.evaluate(test_in, test_out)
        print('Test accuracy:', test_acc)

    def save(cp_path='./checkpoints/model'):
        self.model.save_weights(cp_path)
    def load(cp_path='./checkpoints/model'):
        pass
