from __future__ import annotations

import cmath
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def solve_second_order_system(
        m: float,
        b: float,
        k: float,
):
    d = (b ** 2) - (4 * m * k)

    # find two solutions
    sol1 = (-b - cmath.sqrt(d)) / (2 * m)
    sol2 = (-b + cmath.sqrt(d)) / (2 * m)


solve_second_order_system(1, 1, 1)
