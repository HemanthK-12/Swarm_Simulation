import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Ask the user for an input number n
number_of_bots= int(input("Enter a number: "))

# Generate a list of n random coordinates in the range 0 to 50
x = np.random.uniform(0, 50, number_of_bots)
y = np.random.uniform(0, 50, number_of_bots)

def bestfit():
    m=((np.mean(x)*np.mean(y))-np.mean(x*y))/((np.mean(x)*np.mean(x))-np.mean(x*x))
    c=np.mean(y)-m*np.mean(x)
    return (m,c)

m_bestfit,c_bestfit=bestfit()

def y_bestfit(x):
    return (m_bestfit*x)+c_bestfit

plt.plot(x,y_bestfit(x),color='b')

# model = LinearRegression()
# model.fit(x.reshape(-1, 1), y)
# # Calculate the coefficients of the line equation
# A = -model.coef_[0]
# B = 1
# C = -model.intercept_

# Calculate the intersection points on the best fit line
# x_intersection = (B*(B*x - A*y) - A*C) / (A**2 + B**2)
# y_intersection = (A*(-B*x + A*y) - B*C) / (A**2 + B**2)

x_intersection = (y+(x/m_bestfit)-c_bestfit)/(m_bestfit+(1/m_bestfit))
y_intersection = (m_bestfit)*x_intersection+c_bestfit

# Plot the points
plt.scatter(x, y, color='r')

# Plot the best fit line
plt.plot(x, y_bestfit(x), color='b')

# Plot the perpendicular lines
for i in range(number_of_bots):
    plt.plot([x[i], x_intersection[i]], [y[i], y_intersection[i]], color='g')

if(x[i]<x_intersection[i]):
    x_measure=np.linspace(x[i],x_intersection[i],number_of_bots)
else:
    x_measure=np.linspace(x_intersection[i],x[i],number_of_bots)

y_measure=(-1/m_bestfit)*x_measure+(y[0]+(x[0]/m_bestfit))
# Create the figure and the line that we will manipulate
fig, ax = plt.subplots()
line, = ax.plot(x_measure, y_measure, color='k')

# The function that makes the animation.
def update(num, x_measure, y_measure, line):
    line.set_data(x_measure[:num], y_measure[:num])
    line.axes.axis([0, 10, 0, 10])
    return line,

ani = animation.FuncAnimation(fig, update, len(x_measure), fargs=[x_measure, y_measure, line],
                              interval=100, blit=True)

# Mark the intersection points
plt.scatter(x_intersection, y_intersection, color='y')

plt.grid()
plt.show()


