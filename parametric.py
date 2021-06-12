import numpy as np

r   = 1
tht = np.linspace(0, 10* np.pi, 1000)

x = r* np.cos(tht)
y = r* np.sin(tht)
z = np.exp(-tht)

import matplotlib.pyplot as plt
fig = plt.figure('Parametric curves')
ax  = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, '-r', linewidth = 3)

ax.set_xlabel('X', fontweight = 'bold', fontsize = 14)
ax.set_ylabel('Y', fontweight = 'bold', fontsize = 14)
ax.set_zlabel('Z', fontweight = 'bold', fontsize = 14)

plt.title('Parametric Curve', fontweight = 'bold', fontsize = 16)

plt.show()
