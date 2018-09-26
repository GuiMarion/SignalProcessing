import random
import matplotlib.pyplot as plt
import time

class functionX:

    def __init__(self, N):
        self.N = N
        self.X = []
        for i in range(N):
            self.X.append(i+1)

    def plot(self):
        plt.plot(self.X)
        plt.show()


    def getElem(self,i):
        if i < self.N and i >= 0:
            return self.X[i]

        else :
            return 0

    def getAllValues(self):
        return self.X

    def getSize(self):
        return self.N

class functionH:

    def __init__(self, N):
        self.N = N
        self.X = []
        for i in range(N):
            self.X.append(1)

    def plot(self):
        plt.plot(self.X)
        plt.show()


    def getElem(self,i):
        if i < self.N and i >= 0:
            return self.X[i]
        else :
            return 0

    def getAllValues(self):
        return self.X

    def getSize(self):
        return self.N


class functionHN:

    def __init__(self, N):
        self.N = N
        self.X = []
        for i in range(N):
            self.X.append(1/N)

    def plot(self):
        plt.plot(self.X)
        plt.show()


    def getElem(self,i):
        if i < self.N and i >= 0:
            return self.X[i]

        else :
            return 0

    def getAllValues(self):
        return self.X

    def getSize(self):
        return self.N


# TODO : allow noise to have negative values
class functionXNoisy:

    # B niveau de bruit
    def __init__(self, N, B):
        self.N = N
        self.X = []
        for i in range(N):
            self.X.append(i+1 + random.random()*B)

    def plot(self):
        plt.plot(self.X)
        plt.show()


    def getElem(self,i):
        if i < self.N and i >= 0:
            return self.X[i]

        else :
            return 0

    def getAllValues(self):
        return self.X

    def getSize(self):
        return self.N


def conv(x, h):

    time_start = time.clock()
    Max = max(x.getSize(), h.getSize())

    Y = []

    for n in range(Max):

        ret = 0
        for i in range(2*Max):
            ret += h.getElem(i)*x.getElem(n-i)

        Y.append(ret)

    time_elapsed = (time.clock() - time_start)
    print()
    print("Computation time:",time_elapsed)
    print()

    return Y

def main():

    # Simple
    x = functionX(10)
    h = functionH(30)

    Y = conv(x,h)

    plt.plot(Y, 'k')
    plt.plot([x.getElem(i) for i in range(30)])
    plt.show()

    # Noisy 
    x = functionXNoisy(10, 1)
    h = functionH(30)

    Y = conv(x,h)

    plt.plot(Y, 'k')
    plt.plot([x.getElem(i) for i in range(30)])
    plt.show()

    # Noisy + h normalized
    x = functionXNoisy(10, 1)
    h = functionHN(30)

    Y = conv(x,h)

    plt.plot(Y, 'k')
    plt.plot([x.getElem(i) for i in range(30)])
    plt.show()



main()








