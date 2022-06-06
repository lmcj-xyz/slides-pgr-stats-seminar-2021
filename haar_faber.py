import matplotlib.pyplot as plt
import numpy as np

j = 4
m = 6
x = np.arange(0, 1, 1/2**(j+8))
haar = np.zeros(len(x))
faber = np.zeros(len(x))

for i in range(len(x)):
    if (m+0.5)/2**j > x[i] >= m/2**j:
        haar[i] = 1
        faber[i] = x[i]
    elif (m+1)/2**j > x[i] >= (m+0.5)/2**j:
        haar[i] = -1
        faber[i] = 1-x[i]
    else:
        haar[i] = 0
        faber[i] = 0

plt.figure()
plt.plot(haar)
plt.plot(faber)
plt.show()

