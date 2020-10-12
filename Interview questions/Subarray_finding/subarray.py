#Python program

import numpy as np
n=int(input())
m=int(input())
A=np.array(list(map(int,input().split()[:n])))
B=np.array(list(map(int,input().split()[:m])))
print((np.intersect1d(A,B)).size)
