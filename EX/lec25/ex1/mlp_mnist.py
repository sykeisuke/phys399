import numpy as np
import tensorflow as tf
from tensorflow.keras import datasets
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense, Dropout

import matplotlib.pyplot as plt

if __name__ == '__main__':
    np.random.seed(123)

    '''
    1. Dataset
    '''
    mnist = datasets.mnist
    (x_train, t_train), (x_test, t_test) = mnist.load_data()

    # Use 2D input for CNN (batch_size, height, width, channels)
    x_train = (x_train.astype('float32') / 255.0).reshape(-1, 28, 28, 1)
    x_test  = (x_test.astype('float32')  / 255.0).reshape(-1, 28, 28, 1)
    t_train = np.eye(10)[t_train].astype(np.float32)
    t_test = np.eye(10)[t_test].astype(np.float32)

    '''
    2. Model building
    '''
    model = Sequential([
        Input(shape=(28, 28, 1)),
        Conv2D(32, kernel_size=3, activation='relu'),   # 28x28 -> 26x26x32
        MaxPooling2D(pool_size=2),                      # 26x26x32 -> 13x13x32
        Conv2D(64, kernel_size=3, activation='relu'),   # 13x13 -> 11x11x64
        MaxPooling2D(pool_size=2),                      # 11x11x64 -> 5x5x64
        Flatten(),                                      # 5*5*64 = 1600
        Dense(128, activation='relu'),
        Dropout(0.3),
        Dense(10, activation='softmax')
    ])

    '''
    3. Model learning
    '''
    model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(x_train, t_train, epochs=30, batch_size=100, verbose=1)

    '''
    4. Model evaluation
    '''
    loss, acc = model.evaluate(x_test, t_test, verbose=0)
    print('test_loss: {:.3f}, test_acc: {:.3f}'.format(loss, acc))

    '''
    5. Decision boundary plotting
    '''
