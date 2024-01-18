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

x_intersection = (y+(x/m_bestfit)-c_bestfit)/(m_bestfit+(1/m_bestfit))
y_intersection = (m_bestfit)*x_intersection+c_bestfit
m_botpath=[]
c_botpath=[]
# Plot the perpendicular lines

# # Define the line
# m = 1  # slope
# c = 0  # y-intercept
# x = np.linspace(0, 10, 100)
# y = m * x + c

# # Create the figure and the line that we will manipulate
fig, ax = plt.subplots()
ax.scatter(x,y)
for i in range(number_of_bots):
    m_botpath.append((y[i]-y_intersection[i])/(x[i]-x_intersection[i]))
    c_botpath.append(y[i]-m_botpath[i]*x[i])
    ax.plot([x[i], x_intersection[i]], [y[i], y_intersection[i]], color='g')
    #This works because when ax.plot() is given two lists as arguments,it draws a line passing throught the first point and the second point
#points = ax.scatter([bestfit_parameters[0]], [(y_bestfit(bestfit_parameters))[0]],color='forestgreen')
points = ax.scatter([x[0]], [y[0]],color='forestgreen')
one=np.linspace(x[0],x_intersection[0],100)
two=one*m_botpath[0]+c_botpath[0]
ax.plot(bestfit_parameters, y_bestfit(bestfit_parameters), color='r')

def update(num,x,y,points):
    points.set_offsets([x[num],y[num]])
    return points,

ani = animation.FuncAnimation(fig, update, 100, fargs=[one,two,points],
                              interval=100, blit=True)

plt.show()