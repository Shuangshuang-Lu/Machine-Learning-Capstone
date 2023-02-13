import numpy as np
import matplotlib.pyplot as plt

# Generate x-values from 0 to 2*pi
x = np.linspace(0, 2*np.pi, 100)

# Compute y-values as the sine of x
y = np.sin(x)

# Plot the sine function
plt.plot(x, y)

# Add labels to the x and y axes
plt.xlabel('x')
plt.ylabel('sin(x)')

# Show the plot
plt.show()
