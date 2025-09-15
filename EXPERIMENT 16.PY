# tiny_nn.py
import numpy as np

def sigmoid(x): return 1/(1+np.exp(-x))
def sigmoid_deriv(x): return x*(1-x)  # x = sigmoid(output)

class SimpleNN:
    def __init__(self, n_in, n_hidden, n_out, lr=0.5):
        self.lr = lr
        self.w1 = np.random.randn(n_in, n_hidden) * 0.5
        self.w2 = np.random.randn(n_hidden, n_out) * 0.5
        self.b1 = np.zeros((1,n_hidden))
        self.b2 = np.zeros((1,n_out))

    def forward(self, X):
        self.z1 = sigmoid(np.dot(X, self.w1) + self.b1)
        self.z2 = sigmoid(np.dot(self.z1, self.w2) + self.b2)
        return self.z2

    def train(self, X, y, epochs=1000):
        for e in range(epochs):
            out = self.forward(X)
            loss = np.mean((y-out)**2)
            # backprop
            d2 = (out - y) * sigmoid_deriv(out)
            dW2 = np.dot(self.z1.T, d2)
            db2 = np.sum(d2, axis=0, keepdims=True)

            d1 = np.dot(d2, self.w2.T) * sigmoid_deriv(self.z1)
            dW1 = np.dot(X.T, d1)
            db1 = np.sum(d1, axis=0, keepdims=True)

            # update
            self.w2 -= self.lr * dW2
            self.b2 -= self.lr * db2
            self.w1 -= self.lr * dW1
            self.b1 -= self.lr * db1
            if e % (epochs//5 or 1) == 0:
                print(f"Epoch {e}, loss {loss:.4f}")

if __name__ == "__main__":
    # XOR example
    X = np.array([[0,0],[0,1],[1,0],[1,1]])
    y = np.array([[0],[1],[1],[0]])
    nn = SimpleNN(2, 4, 1, lr=0.5)
    nn.train(X, y, epochs=5000)
    print("Predictions:")
    print(np.round(nn.forward(X), 3))
