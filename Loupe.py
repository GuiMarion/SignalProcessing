import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack
from scipy import signal
import cmath


class Hanning:

    def __init__(self, N):
        self.N = N
        self.X = np.hanning(N)
        self.name = "Hanning"

    def __str__(self):
        return str(self.X)

    def getName(self):
        return self.name

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

    def getElems(self, imin, imax):

        if imax < self.N:
            return self.X[imin:imax]
        else:
            return self.X[imin : self.N] + [0]*(imax-self.N)
        
    def getSize(self):
        return self.N

    def printSignal(self, imin, imax):
        print(self.getElems(imin,imax))

    def plotFFT(self):


        t = np.arange(self.N)
        sp = np.fft.fft(self.X)
        freq = np.fft.fftfreq(t.shape[-1])

        Y = []

        for i in range(len(sp.real)):
            Y.append(20*math.log10(math.sqrt(sp.real[i]**2 + sp.imag[i]**2)))

        plt.plot(freq, Y)
        
        plt.show()


class BoxCar:

    def __init__(self, N):
        self.N = N
        self.X = signal.boxcar(N)
        self.name = "BoxCar"

    def __str__(self):
        return str(self.X)

    def getName(self):
        return self.name

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

    def getElems(self, imin, imax):

        if imax < self.N:
            return self.X[imin:imax]
        else:
            return self.X[imin : self.N] + [0]*(imax-self.N)
        
    def getSize(self):
        return self.N

    def printSignal(self, imin, imax):
        print(self.getElems(imin,imax))

    def plotFFT(self):


        t = np.arange(self.N)
        sp = np.fft.fft(self.X)
        freq = np.fft.fftfreq(t.shape[-1])

        Y = []

        for i in range(len(sp.real)):
            Y.append(20*math.log10(math.sqrt(sp.real[i]**2 + sp.imag[i]**2)))

        plt.plot(freq, Y)
        
        plt.show()


def conv(x, h):

    Max = max(x.getSize(), h.getSize())

    Y = []

    for n in range(Max):

        ret = 0
        for i in range(2*Max-1):
            ret += h.getElem(i)*x.getElem(n-i)

        Y.append(ret)

    return Y    

class Cosinus:

    def __init__(self, N, nu0, B, num):

        self.N = N
        self.nu0 = nu0
        self.COS = []
        for i in range(self.N):
            self.COS.append(math.cos(2*math.pi*self.nu0*i + B*math.sin(2*math.pi*num*i)))

    def plot(self):
        plt.plot(self.COS)
        plt.show()


    def getValues(self,nMin, nMax):

        return self.COS[nMin : nMax]

    def getAllValues(self):

        return self.COS

    def getElem(self,i):
        if i < self.N and i >= 0:
            return self.COS[i]
        else :
            return 0

    def getSize(self):
        return self.N

    def plotFFT(self):


        t = np.arange(self.N)
        sp = np.fft.fft(self.COS)
        freq = np.fft.fftfreq(t.shape[-1])

        Y = []

        for i in range(len(sp.real)):
            Y.append(20*math.log10(math.sqrt(sp.real[i]**2 + sp.imag[i]**2)))

        plt.plot(freq, Y)
        
        plt.show()


    def obspec(self, H, Nfft, nu0):

        Y = conv(self, H)

        t = np.arange(Nfft)
        sp = np.fft.fft(Y, n = Nfft)
        freq = np.fft.fftfreq(Nfft)

        Y = []

        for i in range(len(sp.real)):
            Y.append(20*math.log10(math.sqrt(sp.real[i]**2 + sp.imag[i]**2)))

        plt.plot(freq, Y)    

        plt.savefig("/Users/gui/Documents/IRCAM/SignalProcessing/Figs/TFD/TFD_"+ str(Nfft)+"_"+str(nu0)+ "_" +H.getName() +".png")

        plt.show() 

class W1:

    def __init__(self, N, nu0):
        self.N = N
        self.X = []

        for i in range(N):
            self.X.append(cmath.exp(2j * math.pi * nu0*i))


        self.name = "W1"

    def __str__(self):
        return str(self.X)

    def getName(self):
        return self.name

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

    def getElems(self, imin, imax):

        if imax < self.N:
            return self.X[imin:imax]
        else:
            return self.X[imin : self.N] + [0]*(imax-self.N)
        
    def getSize(self):
        return self.N

    def printSignal(self, imin, imax):
        print(self.getElems(imin,imax))

    def plotFFT(self):


        t = np.arange(self.N)
        sp = np.fft.fft(self.X)
        freq = np.fft.fftfreq(t.shape[-1])

        Y = []

        for i in range(len(sp.real)):
            Y.append(20*math.log10(math.sqrt(sp.real[i]**2 + sp.imag[i]**2)))

        plt.plot(freq, Y)
        
        plt.show()

class Func:

    def __init__(self, X):
        self.N = len(X)
        self.X = X
        self.name = "X"       


    def __str__(self):
        return str(self.X)

    def getName(self):
        return self.name

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

    def getElems(self, imin, imax):

        if imax < self.N:
            return self.X[imin:imax]
        else:
            return self.X[imin : self.N] + [0]*(imax-self.N)
        
    def getSize(self):
        return self.N

    def printSignal(self, imin, imax):
        print(self.getElems(imin,imax))

    def plotFFT(self):


        t = np.arange(self.N)
        sp = np.fft.fft(self.X)
        freq = np.fft.fftfreq(t.shape[-1])

        Y = []

        for i in range(len(sp.real)):
            Y.append(20*math.log10(math.sqrt(sp.real[i]**2 + sp.imag[i]**2)))

        plt.plot(freq, Y)
        
        plt.show()


def plotFFT(X):

    t = np.arange(len(X))
    sp = np.fft.fft(X)
    freq = np.fft.fftfreq(t.shape[-1])

    Y = []

    for i in range(len(sp.real)):
        Y.append(20*math.log10(math.sqrt(sp.real[i]**2 + sp.imag[i]**2)))

    plt.plot(freq, Y)
    
    plt.show()


def Multiply(X, W):

    Y = []

    for i in range(X.getSize()):

        Y.append(X.getElem(i)*W.getElem(i))

    return Y

def Decimate(X, M):

    Y = []

    mX = X.getAllValues()

    for i in range(X.getSize()//M):
        Y.append(mX[i*M])

    return Y


def main():
    N = 256
    nu0 = 0.3
    num = 5*10**(-4)
    B = 10

    X = Cosinus(N, nu0, B, num)

    #5.1

    # Centering cos with W
    w1 = W1(N, nu0)
    X1 = Func(Multiply(X, w1))
    #X1.plotFFT()

    # Filtering X1 with H
    H = BoxCar(N//2)
    X2 = Func(conv(X1, H))
    #X2.plotFFT()

    # Decimating signal with M
    X3 = Func(Decimate(X2,10))
    #X3.plotFFT()

    # Centering at 0.5 with W2
    w2 = W1(N, -0.5)
    Y1 = Func(Multiply(X3, w2))
    #Y1.plotFFT()


    # 5.2

    M = 32

    X4 = Cosinus(N*M, nu0, B, num)
    X4.plotFFT()

    X5 = Func(Multiply(X, w1))
    X5.plotFFT()

    d1 = 0.1
    d2 = 1/100

    # Compute the order of the filter
    Nua = 0.3
    Nuc = 0.06
    O = int(2/(3*(Nua - Nuc)) * math.log10(1/(10*d1*d2)))

    h = Func(signal.remez(O, [0, Nuc, Nua, 0.5], [d2, d1]))

    X6 = Func(conv(X5, h))

    X6.plotFFT()


    

main()









