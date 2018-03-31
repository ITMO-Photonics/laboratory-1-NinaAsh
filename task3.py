import numpy as np
import scipy.linalg as linalg

n=100
A=np.zeros((n,n))
i,j=np.indices((n,n))
A[i==j]=1
A[i==j+1]=1
A[i==j+2]=1
C=np.arange(n)
c=linalg.solve(A,C)
print(c)
