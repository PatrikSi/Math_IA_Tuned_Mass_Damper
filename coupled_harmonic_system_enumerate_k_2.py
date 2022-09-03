import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

b_1 = 1
k_1 = 2
b_2 = 1
k_2_list = np.linspace(0.1, 10, 100)
m_2 = 0.5
initial = [0, 4, 0, 0]

building_displacements = []
damper_displacements = []

for k_2 in k_2_list:
    def solver(Y, t):
        return [Y[1],
                -(k_1 + k_2) * Y[0] - (b_1 + b_2) * Y[1] + k_2 * Y[2] + b_2 * Y[3],
                Y[3],
                (k_2/m_2)*Y[0] + (b_2/m_2)*Y[1] - (k_2/m_2)*Y[2] - (b_2/m_2)*Y[3]]


    a_t = np.arange(0, 25.0, 0.01)
    asol = integrate.odeint(solver, initial, a_t)
    print(asol)
    building_displacements.append(round(np.amax(asol[:, 0]), 3))
print(building_displacements)
print(min(building_displacements))
plt.title(f'building displacement vs k_2, minimum={min(building_displacements)} at k_2={k_2_list[building_displacements.index(min(building_displacements))]}, b_2=1')
plt.xlabel('k_2')
plt.ylabel('max_building_displacement')
plt.plot(k_2_list, building_displacements)
plt.show()