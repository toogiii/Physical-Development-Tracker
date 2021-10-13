# <examples/doc_model_gaussian.py>
import matplotlib.pyplot as plt
import numpy as np

from lmfit import Model

x = [0, 1, 2, 3, 4, 20, 40, 60, 80]
y = [1, 1, 2, 3, 4, 5, 25, 75, 96]

def sigmoidalcurve(x, b, x0):
    return 101 * (np.exp(np.float64(b * x - x0)) / (1 + np.exp(np.float64(b * x - x0))))

gmodel = Model(sigmoidalcurve)
result = gmodel.fit(y, x=x, b=1/10, x0 = 5)
print(result.fit_report())
plt.plot(x, y, 'bo')
plt.plot(x, result.init_fit, 'k--', label='initial fit')
plt.plot(x, result.best_fit, 'r-', label='best fit')
plt.legend(loc='best')
plt.show()