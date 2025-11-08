import numpy as np
from mlp import MLP, Layer
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt

# ---- 1. data (1D regression)
np.random.seed(123)
n = 200
x = np.linspace(-3, 3, n).reshape(-1, 1)
t = np.sin(x) + 0.3*np.random.randn(n, 1)

x_train, x_test, t_train, t_test = train_test_split(
    x, t, test_size=0.2, random_state=42
)

# ---- 2. Model (output layer: identity)
model = MLP(1, 20, 1)  

# ---- 3. Learning parameters
lr = 0.01
epochs = 2000
batch_size = 20
n_batches = x_train.shape[0] // batch_size

# ---- 4. Learning Loops
def compute_loss(t, y):
    return 0.5 * np.mean((y - t)**2)

def train_step(xb, tb, lr):
    yb = model(xb)
    m  = xb.shape[0]

    # Output layer (linear + MSE)
    delta_out = (yb - tb) / m                      # (batch, 1)
    W2_pre = model.l2.W.copy()                

    # Gradients (output layer)
    dW2 = model.l2._input.T @ delta_out            # (hidden, 1)
    db2 = delta_out.sum(axis=0, keepdims=True)     
    model.l2.W -= lr * dW2
    model.l2.b -= lr * db2

    # Hidden layer δ = (δ_out @ W2_pre^T) * f'(z1)
    delta_h = (delta_out @ W2_pre.T) * model.l1.derivative(model.l1._pre_activation)

    # Gradients (hidden layer)
    dW1 = model.l1._input.T @ delta_h              # (in, hidden)
    db1 = delta_h.sum(axis=0, keepdims=True)    
    model.l1.W -= lr * dW1
    model.l1.b -= lr * db1

    return compute_loss (tb, yb)

for ep in range(epochs):
    train_loss = 0.0
    xs, ts = shuffle(x_train, t_train, random_state=ep)
    for b in range(n_batches):
        s = b*batch_size
        e = s + batch_size
        train_loss += train_step(xs[s:e], ts[s:e], lr)

    if ep % 50 == 0 or ep == epochs-1:
        print(f"epoch: {ep+1}, MSE: {train_loss/n_batches:.4f}")

# ---- 5. Plots
x_min, x_max = x.min(), x.max() 
x_plot = np.linspace(x_min, x_max, 400).reshape(-1, 1)

y_plot = model(x_plot).ravel()        # (400,1) -> (400,)

plt.figure(figsize=(7,5))
plt.scatter(xs.ravel(), ts.ravel(), s=24, alpha=0.6,
            edgecolors='k', linewidths=0.4, label='train')

plt.plot(x_plot.ravel(), y_plot, linewidth=3, zorder=10, label='MLP prediction')

plt.title('MLP Regression (MSE, linear output)')
plt.xlabel('x'); plt.ylabel('y')
plt.legend()
plt.tight_layout()
plt.show()

# ---- 6. Evaluation
y_pred = model(x_test)
rmse = np.sqrt(mean_squared_error(t_test, y_pred))
mae = mean_absolute_error(t_test, y_pred)
print(f"RMSE: {rmse:.4f}, MAE: {mae:.4f}")

