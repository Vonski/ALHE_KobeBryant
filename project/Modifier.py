import numpy as np
import math

def generateAvarageValuesTable(X, y, cx, cy):
    hitted = np.zeros((901,601))
    missed = np.zeros((901,601))
    for i in range(X.shape[0]):
        hitted[(X[i][1]+100, X[i][0]+300)]+=y[i]
        missed[(X[i][1]+100, X[i][0]+300)]+=1-y[i]

    mul_x = math.floor(hitted.shape[1]/cx)
    mul_y = math.floor(hitted.shape[0]/cy)
    ret = np.ones((cx, cy))
    for ix in range(cx):
        for iy in range(cy):
            s1 = np.sum(hitted[iy*mul_y:(iy+1)*mul_y,ix*mul_x:(ix+1)*mul_x])
            s2 = np.sum(missed[iy*mul_y:(iy+1)*mul_y,ix*mul_x:(ix+1)*mul_x])
            if s2:
                ret[ix, iy] = np.clip(s1/s2, 0.5, 2)
            else:
                if s1:
                    ret[ix, iy] = 2
                else:
                    ret[ix, iy] = 1
    return ret