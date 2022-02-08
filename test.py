import matplotlib.pyplot as plt
import numpy as np
interest = 1.05
yearlyIncrease = 6000
xs = np.linspace(0, 25, 26, endpoint=True)
balance = np.zeros_like(xs)
balance[0] = 6000
for i in range(1, len(xs)):
    balance[i] = balance[i-1]*interest + yearlyIncrease

plt.plot(xs, balance)
plt.show()
