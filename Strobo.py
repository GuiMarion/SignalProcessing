import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack


class Sinus:

    def __init__(self, N, nu0):

        self.N = N
        self.nu0 = nu0
        self.SIN = []
        for i in range(self.N):
            self.SIN.append(math.sin(2*math.pi*self.nu0*i))

    def plot(self):
        plt.plot(self.SIN)
        plt.show()


    def getValues(self,nMin, nMax):

        return self.SIN[nMin : nMax]

    def getAllValues(self):

        return self.SIN

    def getSize(self):
        return self.N

    def plotFFT(self):


        t = np.arange(self.N)
        sp = np.fft.fft(self.SIN)
        freq = np.fft.fftfreq(t.shape[-1])
        plt.plot(freq, sp.real, freq, sp.imag)
        
        plt.show()  


def main():
    N = 1000
    nu0 = 0.48

    S = Sinus(N, nu0)

    #print(S.getValues(1, 10))

    S.plot()
    S.plotFFT()

main()







