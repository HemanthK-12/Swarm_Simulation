import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the line
m = 1  # slope
c = 0  # y-intercept
x = np.linspace(0, 10, 100)
y = m * x + c


# Create the figure and the line that we will manipulate
fig, ax = plt.subplots()
line, = ax.plot(x, y, color='k')

# The function that makes the animation.
def update(num, x, y, line):
    line.set_data(x[:num], y[:num])
    line.axes.axis([0, 10, 0, 10])
    return line,

ani = animation.FuncAnimation(fig, update, len(x), fargs=[x, y, line],
                              interval=100, blit=True)

plt.show()