import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

b = 1
k = 2
initial = [0, 4]


def solver(Y, t):
    return [Y[1], -k * Y[0] - b * Y[1]]


a_t = np.arange(0, 25.0, 0.01)
asol = integrate.odeint(solver, initial, a_t)
print(asol)
plt.title(f'Only building, mass normalized, b={b}, k={k}')
plt.plot(asol[:, 0], label='position')
plt.plot(asol[:, 1], label='velocity')
plt.xlim(0, 1000)
plt.legend()
plt.show()
