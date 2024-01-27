f=open('input1.txt','rt')
a=f.readline()
n, m=map(int,a.split())
data=f.read().split()
import numpy as np
arr=np.array(data, dtype=int)
matrix=arr.reshape(n,m,m)
mat_list=[]
det_list=[]
for i in range (n):
    for j in range (i+1,n):
           zarb=np.dot(matrix[i],matrix[j])
           mat_list.append([zarb,[matrix[i],matrix[j]]])
for x in mat_list:
    det=np.linalg.det(x[1][0]) 
    det_list.append(det)
    
a=max(det_list)  
b=det_list.index(a) 
mat1, mat2 = mat_list[b][1]

det_mat1 = np.linalg.det(mat1)
det_mat2 = np.linalg.det(mat2)

if det_mat1 > det_mat2:
    mat3=np.dot(mat1,mat2)
elif det_mat2 > det_mat1:
    mat3=np.dot(mat2,mat1)
else:
    index_mat1 = np.where((matrix == mat1).all(axis=(1,2)))[0][0]
    index_mat2 = np.where((matrix == mat2).all(axis=(1,2)))[0][0]
    if index_mat1 > index_mat2:
        mat3=np.dot(mat2,mat1)
    else:
        mat3=np.dot(mat1,mat2)
mat4=np.linalg.inv(mat3)        
for v in mat4:
    for t in v:
        print(t,end=" ")
    print()    



    




    