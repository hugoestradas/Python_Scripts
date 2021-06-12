import numpy as np
import matplotlib.pyplot as plt

Ro  = 2
r   = 1
tht = np.linspace(0, 2* np.pi, 50)
phi = np.linspace(0, 2* np.pi, 50)

tht, phi = np.meshgrid(tht, phi)

x = (Ro + r* np.cos(tht))* np.cos(phi)
y = (Ro + r* np.cos(tht))* np.sin(phi)
z = r* np.exp(-tht)

fig = plt.figure('Parametric Surfaces')
ax  = fig.add_subplot(111, projection='3d')

h = ax.plot_surface(x, y, z, cmap = 'jet', edgecolor = 'k')

fig.colorbar(h)

ax.set_xlabel('X', fontweight = 'bold', fontsize = 14)
ax.set_ylabel('Y', fontweight = 'bold', fontsize = 14)
ax.set_zlabel('Z', fontweight = 'bold', fontsize = 14)

ax.set_title('Hugos Cup (Torus-like surface)', fontweight = 'bold', fontsize = 16)

plt.show()
