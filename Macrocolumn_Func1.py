
import numpy as np
from minicol import minicol
# from mlabwrap import matlab
# from scipy.interpolate import interp1d
import random

class  Macrocolumn_Func1:

    def __init__(self):
        pass

    def Macrocolumn_Func1_cr(self, input, iter, wc, overlap):

        q = 4
        i = 3
        j = 12

        # for a given minicolumn i = number of units, j = number of inputs, q = number of minicolumns,
        # Wc = zeros(i, j, q);
        # max of V
        VxC = np.zeros([1, q])

        Vint = np.zeros([q, i])
        Psi = np.zeros([q, i])
        Roi = np.zeros([q, i])
        F2i = np.zeros([q, i])

        mincol = minicol()

        for kk in range(q):
            print("kk", kk)
            # print(wc.shape)
            Wkk = wc[:, :, kk]
            X, Voutkk = mincol.minicol_cr(input, Wkk)

            VxC[:, kk] = Voutkk
            Vint[kk, :] = X

        print("Vxc", VxC)

        G = sum(VxC[0]) / q

        # G to eta mapping

        Gmap = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
        etamap = [0, 0, 0.2, 5, 12, 100]

        eta = np.interp(G, Gmap, etamap)

        print("eta", eta)

        Lamda = 28
        Phi = -5

        for kk in range(q):
            for jj in range(i):
                Psijj = (eta / (1 + np.exp(-Lamda * Vint[kk, jj] - Phi))) + 1
                Psi[kk, jj] = Psijj

        print("Psi ", Psi)

        for kk in range(q):
            for jj in range(i):
                Psijj = Psi[kk, :]
                Roi[kk, jj] = Psi[kk, jj] / sum(Psijj)

        print("Roi ", Roi)

        if iter == 1:
            F2i[0, :] = [0, 0, 1]
            F2i[1, :] = [0, 1, 0]
            F2i[2, :] = [1, 0, 0]
            F2i[3, :] = [0, 0, 1]
        else:

            if overlap == 0:
                newMiniColumns = q
            else:
                newMiniColumns = q - (overlap - 1)

            print("newMiniCoulms: ", newMiniColumns)

            randomMiniCoumns = random.sample(range(0, 4), newMiniColumns)

            print(" randomMiniColumns", randomMiniCoumns)

            # WTA with in each minicolumn

            for kk in range(q):
                Roijj = Roi[kk, :]

                print("Roijj", Roijj)

                (m, IND) = max((v, i) for i, v in enumerate(Roijj))
                print(m, " ", IND)

                if kk in randomMiniCoumns:
                    n = random.randint(0, 2)
                    print("n", n)

                    while IND == n:
                        n = random.randint(0, 2)
                        print("n1", n)

                    F2i[kk, n] = 1

                else:
                    F2i[kk, IND] = 1

        return F2i