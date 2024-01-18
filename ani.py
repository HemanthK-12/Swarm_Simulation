# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# import numpy as np

# fig, ax = plt.subplots()

# x = np.arange(0, 2*np.pi, 0.01)
# line, = ax.plot(x, np.sin(x))

# def animate(i):
#     line.set_ydata(np.sin(x + i / 50))  # update the data.
#     return line,

# ani = animation.FuncAnimation(
#     fig, animate, interval=20, blit=True, save_count=50)

# plt.show()

# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# import numpy as np

# fig, ax = plt.subplots()

# # Define the line along which the dot will move
# x = np.linspace(0, 10, 100)
# y = x  # This makes the line oblique. Adjust as needed.

# # Plot the dot at the first position
# dot, = ax.plot(x[0], y[0], 'ro')

# # Set the axes limits
# ax.set_xlim(-10, 10)
# ax.set_ylim(-15,5)

# def animate(i):
#     dot.set_data(x[i],5-2*x[i])  # update the position of the dot
#     return dot,

# ani = animation.FuncAnimation(
#     fig, animate, frames=len(x), interval=100, blit=True)

# plt.show()

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()

# Define the line along which the dot will move
x = np.linspace(0, 10, 100)
y = x  # This makes the line oblique. Adjust as needed.

# Plot the dots at the first position
dots = [ax.plot(x[0], y[0], 'ro')[0] for _ in range(5)]

# Set the axes limits
ax.set_xlim(-10, 10)
ax.set_ylim(-15, 5)

def animate(i):
    for dot in dots:
        dot.set_data(x[i], 5 - 2 * x[i])  # update the position of the dot
    return dots

ani = animation.FuncAnimation(
    fig, animate, frames=len(x), interval=100, blit=True)

plt.show()