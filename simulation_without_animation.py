import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

number_of_bots= (int)(input("Enter a number: "))

x = np.random.uniform(0, 50, number_of_bots)
y = np.random.uniform(0, 50, number_of_bots)

def bestfit():
    m=((np.mean(x)*np.mean(y))-np.mean(x*y))/((np.mean(x)*np.mean(x))-np.mean(x*x))
    c=np.mean(y)-m*np.mean(x)
    return (m,c)

m_bestfit,c_bestfit=bestfit()

def y_bestfit(x):
    return (m_bestfit*x)+c_bestfit

bestfit_parameters=np.linspace(0,50,100)
plt.plot(bestfit_parameters,y_bestfit(bestfit_parameters),color='b')

x_intersection = (y+(x/m_bestfit)-c_bestfit)/(m_bestfit+(1/m_bestfit))
y_intersection = (m_bestfit)*x_intersection+c_bestfit

plt.scatter(x, y, color='r')

plt.plot(x, y_bestfit(x), color='b')

# Plot the perpendicular lines
for i in range(number_of_bots):
    plt.plot([x[i], x_intersection[i]], [y[i], y_intersection[i]], color='g')


# Mark the intersection points
plt.scatter(x_intersection, y_intersection, color='y')

plt.grid()
plt.show()


