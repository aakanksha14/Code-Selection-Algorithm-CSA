
import numpy as np
from unitcol import unitcol

class minicol:
    def __init__(self):
        pass

    def minicol_cr(self, IN,W):

        # for a given minicolumn i = number of units, j = number of inputs

        i = 3
        j = 12

        # W = zeros(i, j);

        # Column1

        V = np.zeros([1, i])
        uncol = unitcol()

        # calculate V for each unit

        for kk in range(i):
            Wkk = W[kk, :]
            Vkk = uncol.unitcol_cr(IN, Wkk)
            V[:, kk] = Vkk

        # Vx = max(V)
        Vx = V[0].max(0)

        return V, Vx
