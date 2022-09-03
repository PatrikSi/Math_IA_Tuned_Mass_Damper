import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt


def solver(Y, t):
    return [Y[1], -2 * Y[0] - Y[1]]


a_t = np.arange(0, 25.0, 0.01)
asol = integrate.odeint(solver, [0, 4], a_t)
print(asol)
plt.plot(asol[:, 0], label='position')
plt.plot(asol[:, 1], label='velocity')
plt.legend()
plt.show()
