import time
import numpy as np
import scipy.linalg

N=50
A = np.random.random((N,N))
k = np.arange(N) #возврат равномерно расположенных значений до N

for t in np.linspace(0,10,100):
        b=k/(1.+k*t) # зависимость вектора от времени
        c = scipy.linalg.solve(A,b)
print(c)
lu = scipy.linalg.lu_factor(A)
for t in np.linspace(0,10,100):
        b=k/(1.+k*t)
        c1 = scipy.linalg.lu_solve(lu,b)
print(c1)
A1 = scipy.linalg.inv(A)
for t in np.linspace(0,10,100):
        b=k/(1.+k*t)
        c2 = np.dot(A1,b)
print(c2)

start_time = time.time()
for t in np.linspace(0,10,100):
	c = scipy.linalg.solve(A,b)
stop = time.time()-start_time
print(stop)

start_time = time.time()
lu = scipy.linalg.lu_factor(A)
for t in np.linspace(0,10,100):
	c1 = scipy.linalg.lu_solve(lu,b)
stop = time.time()-start_time
print(stop)

start_time = time.time()
A1 = scipy.linalg.inv(A)
for t in np.linspace(0,10,100):
	c2 = np.dot(A1,b)
stop = time.time()-start_time
print(stop)



