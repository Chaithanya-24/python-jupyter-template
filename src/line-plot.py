import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 11, 1)
y = x ** 2  
plt.plot(x, y, marker='o', linestyle='-', color='b', label='y = x^2')
plt.title("Line Plot of y = x^2")
plt.xlabel("X Values")
plt.ylabel("Y Values (X Squared)")
plt.grid(True)
plt.legend()
plt.show()
