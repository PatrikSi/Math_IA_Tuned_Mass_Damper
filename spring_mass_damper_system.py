from __future__ import annotations

import math
import cmath
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq

time = np.linspace(0, 20)
initial_conditions = [4, 0]


def solve_second_order_system(
        m: float,
        b: float,
        k: float,
):
    d = (b ** 2) - (4 * m * k)

    # find two solutions
    sol1 = (-b - cmath.sqrt(d)) / (2 * m)
    sol2 = (-b + cmath.sqrt(d)) / (2 * m)

    return {'real': sol1.real, 'imag': abs(sol1.imag)}


coefficients = solve_second_order_system(m=2,
                                         b=0.025,
                                         k=-5,
                                         )


def create_equation(
        t,
        real: float,
        imag: float,
):
    A = 1
    B = 1
    print(real)
    plt.plot(t, (math.e ** (real * t)) * (A*np.sin(imag * t) + B*np.cos(imag * t)))
    plt.show()
    return (math.e ** (real * t)) * (A*np.sin(imag * t) + B*np.cos(imag * t))


print(create_equation(time, **coefficients))

