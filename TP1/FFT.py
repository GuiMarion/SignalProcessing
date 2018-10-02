import cmath
import math

def FFT(X):
	L = []

	for i in range(len(X)):
		temp = 0

		for k in range(len(X)):

			temp += X[k]*cmath.exp(2j * math.pi * (k/len(X)) * i)

		L.append(temp)

	return L


Y = FFT([1,2,3,4,5,5,4,3,2,1])

for elem in Y:
	print(elem.imag, elem.real)
