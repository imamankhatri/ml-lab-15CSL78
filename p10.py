# -*- coding: utf-8 -*-
"""
@author: imamankhatri
"""
from math import ceil
import numpy as np
from scipy import linalg  
def lowess(x, y, f= 2. / 3., iter=3):   
    n = len(x) 
    r = int(ceil(f * n)) 
    h = [np.sort(np.abs(x - x[i]))[r] for i in range(n)] 
    w = np.clip(np.abs((x[:, None] - x[None, :]) / h), 0.0, 1.0)
    w = (1 - w ** 3) ** 3  
    ypred = np.zeros(n) 
    delta = np.ones(n)  
    for iteration in range(iter):
        for i in range(n):
            weights = delta * w[:, i] 
            b = np.array([np.sum(weights * y), np.sum(weights * y * x)]) 
            A = np.array([[np.sum(weights), np.sum(weights * x)],
                          [np.sum(weights * x), np.sum(weights * x * x)]]) 
            beta = linalg.solve(A, b) 
            ypred[i] = beta[0] + beta[1] * x[i]            
        residuals = y - ypred   
        s = np.median(np.abs(residuals))  
        delta = np.clip(residuals / (6.0 * s), -1, 1) 
        delta = (1 - delta ** 2) ** 2   
    return ypred

if __name__ == '__main__':  
    import math   
    n = 100  
    
    x = np.linspace(0, 2 * math.pi, n)
    print(x)
    y = np.sin(x) + 0.3 * np.random.randn(n) 
      
    f = 0.25
    ypred = lowess(x, y, f=f, iter=3)   
    import pylab as pl
    pl.clf()
    pl.plot(x, y, label='Y NOISY')
    pl.plot(x, ypred, label='Y PREDICTED')
    pl.legend()
    pl.show()
