import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers
from tensorflow.keras.initializers import RandomNormal

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error

import matplotlib.pyplot as plt

if __name__ == '__main__':
    np.random.seed(123)

    '''
    1. Dataset
    '''
    n = 200
    x = np.linspace(-3, 3, n).reshape(-1, 1)
    t = np.sin(x) + 0.3*np.random.randn(n, 1)

    x_train, x_test, t_train, t_test = train_test_split(
        x, t, test_size=0.2, random_state=42
    )

    '''
    2. Model building
    '''
    model = Sequential([
        keras.Input(shape=(1,)),
        Dense(20, activation='tanh'),
        Dense(1, activation='linear')
    ])

    '''
    3. Model learning
    '''
    optimizer = optimizers.SGD(learning_rate=0.01)
    model.compile(optimizer=optimizer, 
 		  loss='mse', 
                  metrics=[keras.metrics.RootMeanSquaredError(name='rmse'),
			   keras.metrics.MeanAbsoluteError(name='mae')]
    )
    model.fit(x_train, t_train, epochs=1000, batch_size=20, verbose=1)

    '''
    4. Model evaluation
    '''
    eval_res = model.evaluate(x_test, t_test, verbose=0)
    print(f"Test  -> loss(MSE): {eval_res[0]:.4f}, RMSE: {eval_res[1]:.4f}, MAE: {eval_res[2]:.4f}")

    '''
    5. Plotting
    '''
    x_plot = np.linspace(x.min(), x.max(), 400).reshape(-1, 1).astype("float32")
    y_plot = model.predict(x_plot, verbose=0).ravel()

    plt.figure(figsize=(7,5))
    plt.scatter(x_train.ravel(), t_train.ravel(), s=24, alpha=0.6,
            edgecolors='k', linewidths=0.4, label='train')
    plt.plot(x_plot.ravel(), y_plot, linewidth=3, label='MLP prediction')
    plt.title('MLP Regression (MSE, linear output)')
    plt.xlabel('x'); plt.ylabel('y')
    plt.legend()
    plt.tight_layout()
    plt.show()

