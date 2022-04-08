
import numpy  as np
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt


def model(X, theta):
    return X.dot(theta)


def cost (X, y,theta):
    m = len(y)
    Cost = 1/(2*m)*np.sum((model(X, theta)-y)**2)
    return Cost
def grad (X, y,Theta):
    m = len(y)


    Grad = 1/m*X.T.dot(model(X,Theta)-y)
    return Grad
def gradientDescente(X,y, Theta, learningRate, iteration):

            for i in range(0,iteration):
                m = len(y)
                Theta = Theta - learningRate*(1/m)*(X.T).dot(X.dot(Theta)-y)
            return Theta


x,y = make_regression(n_samples= 100, n_features=1, noise = 10)
y  = y.reshape(100,1)                        # target (100,1)
X = np.hstack((x, np.ones(x.shape)))    # les features (100,2)
theta  = np.random.randn(2,1)  # valeur initiale random des parametres a et b

x = X[:,0]
theta = np.array([[2.08573032],
                 [0.06474408]])
plt.scatter(x,y)
plt.plot(X, model(X, theta), c = 'r')
plt.title('cost = ' +str(int(cost (X, y,theta)) ))
print(cost (X, y,theta))
OptimaleTheta = gradientDescente(X,y, theta, 0.0001, 100000)

plt.show()
plt.scatter(x,y)
plt.plot(x, model(X, OptimaleTheta), c = 'g')
plt.title('cost = ' +str(int(cost (X, y,OptimaleTheta)) ))
plt.show()
