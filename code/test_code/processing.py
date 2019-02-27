import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt

def box():
    plt.interactive(False)
    h_b = 1.054571800e-34
    dx = 0.1e-9
    m = 1-20
    d = (h_b**2)/(m*dx**2)
    print(d)
    e = d*-(1/2)
    print(e)
    w,v = scipy.linalg.eigh_tridiagonal(d,e)
    plt.quiver(v)
    plt.xlim(-10,10)
    plt.ylim(-10,10)
    plt.show()
    return

box()


