import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
import matplotlib.animation as animation
import math
import random
# create a new plot
plt.figure(figsize=(8,6))

# get the current axes
fig, ax = plt.subplots()

# allow user to input number of objects
number_of_bots= (int)(input("Enter a number of bots: "))
x = np.random.normal(0, 50, number_of_bots)
y = np.random.normal(0, 50, number_of_bots)

size_of_polygon= (int)(input("Enter no of sides of polygon: "))

# Calculate the vertices of the regular polygon
radius = random.randint(40,80)
angle = 2 * math.pi / size_of_polygon
vertices = [(radius * math.cos(i * angle), radius * math.sin(i * angle)) 
    for i in range(size_of_polygon)]

for vertex in vertices:
    a, s = vertex
    print("Vertex coordinate:", a, s)

polygon = patches.Polygon(vertices, closed=True, linewidth=2, edgecolor='blue', facecolor='none')

# Add the polygon to the plot
ax.add_patch(polygon)

# Set equal aspect ratio to make the polygon look like a polygon
#ax.set_aspect('equal', adjustable='box')



#this is to just number the bots
for i in range(number_of_bots):
    ax.annotate(i+1, (x[i], y[i]), textcoords="offset points", xytext=(0,15), ha='center')

points, = ax.plot(x, y, 'o', color='red')

def update(frame):
    t = min(frame / 100, 1)  # Gradually move the points over 100 frames
    for i in range(min(number_of_bots, size_of_polygon)):
        #idx = sorted_indices[i]
        x[i] = (1 - t) * x[i] + t * vertices[i][0]
        y[i] = (1 - t) * y[i] + t * vertices[i][1]
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=300, blit=True)

plt.grid()
plt.show()
