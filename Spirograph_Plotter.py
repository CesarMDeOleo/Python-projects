import numpy as np
import matplotlib.pyplot as plt

x_min = (4*np.pi)
t = np.arange(-x_min,x_min,0.01)


plt.figure()
plt.plot(np.cos(t) + np.cos(t/4)*2, np.sin(t) - np.sin(t/4)*2)
plt.title('Plot of x and y values')
plt.xlabel('x')
plt.ylabel('y')
plt.text(1, -3, r'$x = \cos(t) + 2\cos(\frac{t}{4})$', fontsize=12)
plt.text(-2, 2, r'$y = \sin(t) - 2\sin(\frac{t}{4})$', fontsize=12)
plt.grid()
plt.show()