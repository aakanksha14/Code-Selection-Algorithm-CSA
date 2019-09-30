import numpy as np

class Hebbs:
    def __init__(self):
        pass

    def Hebbs_cr(self, prev, IN, F2i):

        i = 3
        j = 12
        q = 4
        W = np.zeros([i, j, q])

        for kk in range(q):
            for jj in range(j):
                for ii in range(i):
                    if IN[jj] == 1 and F2i[kk, ii] == 1 and prev[jj] == 1:
                        W[ii, jj, kk] = 1

        return W