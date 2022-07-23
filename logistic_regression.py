import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-1))

class LogisticRegression:
    def __init__(self, learning_rate=0.001, n_iters=1000):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples = n_features = X.shape

        # initial parameters
        self.weights = np.zeros(n_features)
        self.bias = 0

        # gradient descent
        for _ in range(self.n_iters):
            y_predicted = np.dot(X, self.weights) + self.bias
            # apply sigmoid function
            y_predicted = self._sigmoid(y_predicted)

            # compute gradients
            dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1 / n_samples) * np.sum(y_predicted - y)

            # updated parameters
            self.weights -= self.lr * dw
            self.bias -= self.lr * db

        def predict(self, X):
            y_predicted = np.dot(X, self.weights) + self.bias
            y_predicted = sigmoid(y_predicted)

            #clip to 1 or 0
            y_predicted = [1 if i > 0.5 else 0 for i in y_predicted]
            return np.array(y_predicted)