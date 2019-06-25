import numpy as np

class Cross_Entropy(object):

    def dz(self, y, y_hat):
        #we avoid using the derivative of softmax to save computing power
        return y_hat - y


    def loss(self, y, y_hat):
        m = y.shape[1]

        loss = (-1/m) * np.sum(np.sum((y * np.log(y_hat))))

        #logs = -np.log(y_hat.T[range(len(y_hat.T)), np.argmax(y.T, axis=-1)])
        #loss = np.mean(logs)
        return loss
