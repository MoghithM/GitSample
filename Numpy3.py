import numpy as np
A=np.array(([1,2],[3,4]))
B=np.array(([2,0],[1,3]))
print(np.dot(A,B))
print(np.transpose(A))
print(np.linalg.inv(A))

arr=np.array([[10,20,30],[40,50,60]])
print(arr[0,1])
print(arr[:, 1])
print(arr[1])