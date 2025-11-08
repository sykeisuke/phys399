import numpy as np
from sklearn.utils import shuffle

class MLP(object):
    '''
    Multi-Layer Perceptron
    '''
    def __init__(self, input_dim, hidden_dim, output_dim):
	# input layer - hidden layer
        self.l1 = Layer(input_dim = input_dim,
			output_dim = hidden_dim,
			activation = tanh,
			derivative = dtanh) 

	# hidden layer - output layer
        self.l2 = Layer(input_dim = hidden_dim,
			output_dim = output_dim,
			activation = identity,
			derivative = didentity) 

        self.layers = [self.l1, self.l2]

    def __call__(self, x):
      return self.forward(x)

    def forward(self, x):
      h = self.l1(x)
      y = self.l2(h)
      return y

class Layer(object):
    '''
    Layer Coupling
    '''
    def __init__(self, input_dim, output_dim,activation, derivative):
      scale = np.sqrt(2.0 / (input_dim + output_dim))
      self.W = np.random.normal(size=(input_dim, output_dim)) * scale
      self.b = np.zeros((1,output_dim))

      self.activation = activation # activation function
      self.derivative = derivative # derivative of activation function

    def __call__(self, x):
      return self.forward(x)

    def forward(self, x):
      self._input = x
      self._pre_activation = np.matmul(x, self.W) + self.b
      return self.activation(self._pre_activation)

    def backward(self, delta, W_next):
        if W_next is not None: 
            delta = (delta @ W_next.T) * self.derivative(self._pre_activation)
        dW = self._input.T @ delta
        db = np.sum(delta, axis=0, keepdims=True)
        layer.b -= lr *db
        return delta, dW, db

    #def backward(self, delta, W):
    #  delta = self.derivative(self._pre_activation)*np.matmul(delta, W.T)
    #  return delta

    def compute_gradients(self, delta):
      dW = np.matmul(self._input.T, delta)
      db = np.matmul(np.ones(self._input.shape[0]), delta)
      return dW, db

def sigmoid(x):
  return 1 / (1 + np.exp(-x))

def dsigmoid(x):
  return sigmoid(x) * (1 - sigmoid(x))

def identity(x): 
    return x

def didentity(x):
    return np.ones_like(x)

def tanh(x): return np.tanh(x)

def dtanh(x):
    t = np.tanh(x)
    return 1.0 - t*t
