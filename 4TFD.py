import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack
from scipy import signal


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

    M = x.getSize() + h.getSize()

    Y = []

    for n in range(M -1):

        ret = 0
        for i in range(M-2):
            ret += h.getElem(i)*x.getElem(n-i)

        Y.append(ret)

    return Y    

class Cosinus:

    def __init__(self, N, nu0):

        self.N = N
        self.nu0 = nu0
        self.COS = []
        for i in range(self.N):
            self.COS.append(math.cos(2*math.pi*self.nu0*i))

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


def main():
    N = 64
    nu0 = 0.1
    NfftL = [32, 64, 128, 1024]


    for Nfft in NfftL:

        S = Cosinus(N, nu0)

        S.plot()

        H = BoxCar(N)
        S.obspec(H, Nfft, nu0)

        H = Hanning(N)
        S.obspec(H, Nfft, nu0)



main()








