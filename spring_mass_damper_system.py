from __future__ import annotations

import math
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp



def spring_mass_dashpot(u, x):
    diff = u[1], -2 * u[1] - 2 * u[0] + 0
    return diff


y_0 = [0, 5]
ts = np.linspace(0, 20, 5000)
us = odeint(spring_mass_dashpot, y_0, ts)
ys = us[:, 0]
x_intercept_coords = []
t_intercept_coords = []

print(ts)
print(ys)

for x, t in zip(ts, ys):
    if np.isclose(x, 0) or np.isclose(t, 0):
        x_intercept_coords.append(x)
        t_intercept_coords.append(t)
print(x_intercept_coords)
print(t_intercept_coords)
plt.scatter(x_intercept_coords, t_intercept_coords)
plt.plot(ts, ys)
plt.show()

# plt.plot(t, (math.e**(-t)) * (np.sin(t)))
# plt.show()


# def solve_second_order_system(
#         m: float,
#         b: float,
#         k: float,
# ):
#     d = (b ** 2) - (4 * m * k)
#
#     # find two solutions
#     sol1 = (-b - cmath.sqrt(d)) / (2 * m)
#     sol2 = (-b + cmath.sqrt(d)) / (2 * m)
#
#     return {'real': sol1.real, 'imag': abs(sol1.imag)}
#
#
# coefficients = solve_second_order_system(m=2,
#                                          b=0.025,
#                                          k=-5,
#                                          )


# def create_equation(
#         t,
#         real: float,
#         imag: float,
# ):
#     A = 1
#     B = 1
#     print(real)
#     plt.plot(t, (math.e ** (real * t)) * (A*np.sin(imag * t) + B*np.cos(imag * t)))
#     plt.show()
#     return (math.e ** (real * t)) * (A*np.sin(imag * t) + B*np.cos(imag * t))


# print(create_equation(time, **coefficients))
