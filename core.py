import tensorflow as tf
from tensorflow import keras
import numpy as np

class NN_model:
    model = keras.Sequential([
        keras.layers.Dense(512, activation=tf.nn.relu),
        keras.layers.Dense(7, activation=tf.nn.softmax)
    ])

    def  __init__(self):
        self.model.compile(optimizer=tf.train.AdamOptimizer(), 
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy'])
        
    def train(self, train_in, train_out):
        self.model.fit(train_in, train_out, epochs=500)
    
    def eval(self, test_in, test_out):
        test_acc = self.model.evaluate(test_in, test_out)[1]
        print('Test accuracy:', test_acc)

    def predict(self, test_in):
        prediction = self.model.predict(test_in)
        return np.argmax(prediction)+1

    def apredict(self, note1, note2, note3, rhytm, strong, pos):
        test_in = np.array([[note1, note2, note3, rhytm, strong, pos]])
        return self.predict(test_in)

    def save(self, cp_path='./checkpoints/model'):
        self.model.save_weights(cp_path)
        
    def load(self, cp_path='./checkpoints/model'):
        self.model.load_weights(cp_path)

if __name__ == "__main__":
    train_in = np.array([[1.0, 6.0, 5.0, 0.5, 1.0, 0.1]])
    train_out = np.array([2.0])
    test_in, test_out = train_in, train_out

    model = NN_model()
    model.train(train_in, train_out)
    model.eval(test_in, test_out)
    print(model.predict(test_in))
    print(model.apredict(1.0, 6.0, 5.0, 0.5, 1.0, 0.1))
    model.save()
