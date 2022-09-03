import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

b_1 = 1
k_1 = 2
b_2 = 0.9
k_2 = 3.2
m_2 = 0.5
initial = [0, 4, 0, 0]


def solver(Y, t):
    return [Y[1],
            -(k_1 + k_2) * Y[0] - (b_1 + b_2) * Y[1] + k_2 * Y[2] + b_2 * Y[3],
            Y[3],
            (k_2/m_2)*Y[0] + (b_2/m_2)*Y[1] - (k_2/m_2)*Y[2] - (b_2/m_2)*Y[3]]


a_t = np.arange(0, 25.0, 0.01)
asol = integrate.odeint(solver, initial, a_t)
print(asol)
plt.title(f'b_1={b_1}, k_1={k_1}, b_2={b_2}, k_2={k_2}, maximum_building_displacement={round(np.amax(asol[:, 0]), 3)}')
plt.plot(asol[:, 0], label='building position')
plt.plot(asol[:, 1], label='building velocity')
plt.plot(asol[:, 2], label='damper position')
plt.plot(asol[:, 3], label='damper velocity')
plt.xlim(0, 1000)
plt.legend()
plt.show()
