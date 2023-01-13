
# slicy

import numpy as np

# arr = np.array([
#     [5,4,3,1],
#     [7,3,9,3],
#     [6,4,2,4]

# ])

# print(arr[:2])
# print(arr,arr.shape)
# s_arr=arr[:2,1:3]
# print(s_arr,s_arr.shape)
# print(arr[:2,1:3])

# print(arr)
# print("now start from here")
# # extract last row and col 0, col 1
# print(arr[-1, :2])
# # extract second row 
# print(arr[-2, :])

# # extract third columm
# print(arr[:, 2:3])
# # extract col 1 and col 2
# print(arr[:, 1:3])

# boolean start frrom here

arr = np.array([
    [5,4,3,1],
    [7,3,9,3],
    [6,4,2,4]

])
# print(arr)
# bool_idx = [arr>3]  # print the value which is greater then 3 the true either false
# print(bool_idx)

# print(arr[arr>3]) # print all the value which is greater then 3

#  mathermatical operation and numpy array

# x = np.array([
#     [2,4],
#     [5,3]
# ])
# print(x)

# y = np.array([
#     [6,7],
#     [3,5]
# ])
# print(y)

# print(x+y)
# print("addition")
# print(np.add(x,y))
# print("subtraction")
# print(np.subtract(x,y))
# print("multiply")
# print(np.multiply(x,y))
# print("division")
# print(np.divide(x,y))

# print("square root")
# print(np.sqrt(x))

x = np.array([
    [2,4],
    [5,3]
])
print(x)

y = np.array([
    [6,7],
    [3,5]
])
print(y)

v =np.array([4,5])
w=np.array([3,6])

print(v.dot(w))      # find the dot product  
print(np.dot(v,w))  

print(x.dot(w))
print(np.dot(x,w))

print(x.dot(y))
print(np.dot(x,y))

print(x)
print(x.T)  # transpose of matrix

u = np.array([
    [3,0,5],
    [6,7,3],
    [6,8,4]
])

# print(u)
# print(u.T)

# print("sum of all element of u : ", np.sum(u))
# print("sum of each column: ", np.sum(u, axis=0))
# print("sum of all rows :", np.sum(u,axis=1))


# Brodcasting in numpy


print("start form here for braodcastiing")

x = np.array([
    [3,4,5],
    [2,6,3],
    [8,4,1]
])
v=np.array([1,0,1])

#for loop route

# y = np.empty_like(x)
# print(y)

# for i in range(len(x)):
#     y[i, :] =x[i, :] + v  # addition
# print(x)
# print(y)

#mathematical approach 
print("mathematical approach  from here :")
stacked_v = np.tile(v,(3,1))

print(stacked_v)
print(x +stacked_v)


print(x+v)






x = np.array([1,2,3])

print(np.reshape(x, (3,1)))

x=np.array([
    [3,4,5],
    [6,2,1.]
])

print(np.reshape(x, (3,2)))



 
