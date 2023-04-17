import numpy as np
import matplotlib.pyplot as plt

x_min = (3/2)
x = np.arange(-x_min,x_min,0.01)

plt.figure()
plt.plot(x, np.sin(np.exp(2*x)), x, np.cos(np.exp(2*x)), 'y')
plt.legend(['sin(e^2*x)', 'cos(e^2*x)'])
plt.xlabel('x')
plt.ylabel('y')
plt.title('sin(e^2*x) and cos(e^2*x)')
plt.text(0.2, 0.8, r'$y = \sin(e^{2x})$', fontsize=12, color='blue')
plt.text(-0.3, -0.8, r'$y = \cos(e^{2x})$', fontsize=12, color='blue')
plt.grid()
plt.show()

plt.figure()
plt.suptitle('sin(e^2*x) and cos(e^2*x)')
plt.subplot(211)
plt.ylabel('y')
plt.plot(x, np.sin(np.exp(2*x)))
plt.text(-0.5, 0, r'$y = \sin(e^{2x})$', fontsize=12, color='blue')
plt.legend(['y = sin(e^2*x)'])
plt.grid()

plt.subplot(212)
plt.plot( x, np.cos(np.exp(2*x)), 'y')
plt.text(-0.5, 0, r'$y = \cos(e^{2x})$', fontsize=12, color='blue')
plt.legend(['y = cos(e^2*x)'])
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()