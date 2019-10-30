import numpy as np
a = np.array([1,2,3])
print ("Dimension number is ", a.ndim)
print(a.shape)
print(a.__len__())
print(len(a))

b = np.array([[0, 1, 2], [3, 4, 5]])
print(b.ndim)
print(b.shape)
print(len(b))
print(b.__len__())

a = np.arange(10)
print(a)

c = np.linspace(0, 1, 6)
print(c)

d = np.linspace(0, 1, 5, endpoint = False)
print (d)

a = np.ones((3,3))
print(a)

b = np.zeros((2,2))
print(b)
c = np.eye(3)
print(c)

d = np.diag(np.array([1,2,3,4]))
print(d)

a = np.random.rand(4)
print (a)

b = np.random.randn(4)
print(b)

c = np.empty((2,2))
print(c)

a = np.array([1,2,3])
print(a.dtype)

b = np.array([1., 2.])
print(b.dtype)

c = np.array([1,2,3], dtype=float)

a = np.ones((1,1))
print(a.dtype)

b = np.array([True, False])
print(b.dtype)

c = np.array(["ab", "cde"])
print(c.dtype)

d = np.array(['ab', 'cde'])
print(d.dtype)

import matplotlib.pyplot as plt

x = np.linspace(0,3,20)
y = np.linspace(0,3,20)
plt.plot(x,y)
plt.show()

image = np.random.rand(30,30)
plt.imshow(image, cmap=plt.cm.hot)
plt.colorbar()
plt.show()


