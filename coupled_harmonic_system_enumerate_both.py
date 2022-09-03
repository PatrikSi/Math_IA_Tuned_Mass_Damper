import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

b_1 = 1
k_1 = 2
k_2_list = np.linspace(0, 15, 100)
b_2_list = np.linspace(0, 15, 100)
m_2 = 0.5
initial = [0, 4, 0, 0]

k_x = []
b_y = []
disp_z = []
for k_2 in k_2_list:
    for b_2 in b_2_list:
        def solver(Y, t):
            return [Y[1],
                    -(k_1 + k_2) * Y[0] - (b_1 + b_2) * Y[1] + k_2 * Y[2] + b_2 * Y[3],
                    Y[3],
                    (k_2/m_2)*Y[0] + (b_2/m_2)*Y[1] - (k_2/m_2)*Y[2] - (b_2/m_2)*Y[3]]


        a_t = np.arange(0, 25.0, 0.01)
        asol = integrate.odeint(solver, initial, a_t)
        print(asol)
        k_x.append(k_2)
        b_y.append(b_2)
        disp_z.append(round(np.amax(asol[:, 0]), 3))

ax = plt.axes(projection="3d")
ax.scatter(k_x, b_y, disp_z, s=1)
ax.set_xlabel("k")
ax.set_ylabel("b")
ax.set_zlabel("max_displacement")
plt.show()