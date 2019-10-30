from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

filename = "/Users/feilu/Downloads/SD.csv"
data = np.genfromtxt(filename, delimiter=',')
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = data[:,0]
y = data[:,1]
z = data[:,3]

ax.view_init(elev=20, azim=10)
ax.scatter(x, y, z, c='r', depthshade = True, alpha = 0.1)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

'''
for angle in range(0, 360):
    ax.view_init(30, angle)
    plt.draw()
    plt.pause(0.01)
'''

plt.show()
