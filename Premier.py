import random
import matplotlib.pyplot as plt
import time


def x(i, N):

	X = []

	for e in range(N):
		X.append(e+1)

	if i < N:
		return X[i]

	else :
		return 0

def h(i, N):

	X = []

	for i in range(N):
		X.append(1)

	if i < N:
		return X[i]

	else :
		return 0


def h2(i, M):

	X = []

	for i in range(M):
		X.append(1/M)

	if i < M:
		return X[i]

	else :
		return 0

def xBruit(i, N):

	X = []

	for e in range(N):
		X.append(e+1 + random.random()*10)

	if i < N and i >=0:
		return X[i]

	else :
		return 0

def conv(N, M):

	Max = max(N,M)

	Y = []

	for n in range(Max):

		ret = 0
		for i in range(2*Max):
			ret += h2(i, N)*xBruit(n-i, M)

		Y.append(ret)

	return Y

N = 200

X = []

for i in range(N):
	X.append(xBruit(i, N))

time_start = time.clock()
Y = conv(5,N)
time_elapsed = (time.clock() - time_start)

print(time_elapsed)

plt.plot(Y, 'k')
plt.plot(X)
plt.show()


