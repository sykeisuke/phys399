import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt

if __name__ == '__main__':

    '''
    1. Dataset
    '''
    sample_0 = np.load('training.npy')
    sample_1 = np.load('test.npy')

    # Data shape: [dim1, dim2, dim3, label]
    x_train = sample_0[:, :3] 
    t_train = sample_0[:, 3]
    x_test = sample_1[:, :3]
    t_test = sample_1[:, 3]

    # signal (label==1) / background (label==0) 
    sig_dim1 = sample_0[:,0][sample_0[:,3] > 0]
    bkg_dim1 = sample_0[:,0][sample_0[:,3] < 1]
    sig_dim2 = sample_0[:,1][sample_0[:,3] > 0]
    bkg_dim2 = sample_0[:,1][sample_0[:,3] < 1]
    sig_dim3 = sample_0[:,2][sample_0[:,3] > 0]
    bkg_dim3 = sample_0[:,2][sample_0[:,3] < 1]

    # --- Plot dim1 ---
    plt.figure(figsize=(4,4))
    plt.hist(bkg_dim1, bins=50, log=True, label='label == 0', alpha=0.5, color='blue')
    plt.hist(sig_dim1, bins=50, log=True, label='label == 1', alpha=0.5, color='red')
    plt.legend().get_frame().set_alpha(0)
    plt.xlabel('dim1')
    plt.ylabel('Entries')
    plt.title('Feature distribution: dim1')
    plt.show()

    # --- Plot dim2 ---
    plt.figure(figsize=(4,4))
    plt.hist(bkg_dim2, bins=50, log=True, label='label == 0', alpha=0.5, color='blue')
    plt.hist(sig_dim2, bins=50, log=True, label='label == 1', alpha=0.5, color='red')
    plt.legend().get_frame().set_alpha(0)
    plt.xlabel('dim2')
    plt.ylabel('Entries')
    plt.title('Feature distribution: dim2')
    plt.show()

    # --- Plot dim3 ---
    plt.figure(figsize=(4,4))
    plt.hist(bkg_dim3, bins=50, log=True, label='label == 0', alpha=0.5, color='blue')
    plt.hist(sig_dim3, bins=50, log=True, label='label == 1', alpha=0.5, color='red')
    plt.legend().get_frame().set_alpha(0)
    plt.xlabel('dim3')
    plt.ylabel('Entries')
    plt.title('Feature distribution: dim3')
    plt.show()

    '''
    2. Model building
    '''
    model = Sequential([
        Input(shape=(3,)),
        Dense(32, activation='relu'),
        Dense(32, activation='relu'),
        Dense(1, activation='sigmoid')
    ])

    '''
    3. Model learning
    '''
    model.compile(optimizer=Adam(learning_rate=0.001),
                  loss='binary_crossentropy',
                  metrics=['accuracy']
    )

    history = model.fit(x_train, t_train, epochs=10, batch_size=128, verbose=1)

    '''
    4. Model evaluation
    '''
    loss, acc = model.evaluate(x_test, t_test, verbose=0)
    print(f"Test Loss: {loss:.3f}, Test Accuracy: {acc:.3f}")

    '''
    5. Plotting
    '''
    plt.figure(figsize=(8,4))
    plt.plot(history.history['loss'], label='train loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()

    plt.figure(figsize=(8,4))
    plt.plot(history.history['accuracy'], label='train acc')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.show()

    # Score Distribution
    y_score = model.predict(x_test, verbose=0).ravel()
    sig_scores = y_score[t_test == 1]
    bkg_scores = y_score[t_test == 0]

    plt.figure(figsize=(8,4))
    plt.hist(bkg_scores, bins=50, log=True, label='label == 0', alpha=0.5, color='blue')
    plt.hist(sig_scores, bins=50, log=True, label='label == 1', alpha=0.5, color='red')
    plt.xlabel('Model output (probability)')
    plt.ylabel('Counts'); plt.title('Test scores')
    plt.legend(); plt.tight_layout(); plt.show()

