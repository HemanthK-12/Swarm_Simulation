import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

number_of_bots= (int)(input("Enter a number: "))
x = np.random.normal(0, 50, number_of_bots)
y = np.random.normal(0, 50, number_of_bots)

def bestfit():
    m=((np.mean(x)*np.mean(y))-np.mean(x*y))/((np.mean(x)*np.mean(x))-np.mean(x*x))
    c=np.mean(y)-m*np.mean(x)
    return (m,c)

m_bestfit,c_bestfit=bestfit()

def y_bestfit(x):
    return (m_bestfit*x)+c_bestfit

fig, ax = plt.subplots()
ax.scatter(x, y, color='r')
x_intersection = (y+(x/m_bestfit)-c_bestfit)/(m_bestfit+(1/m_bestfit))
y_intersection = y_bestfit(x_intersection)
bestfit_parameters=np.linspace(np.min(x_intersection),np.max(x_intersection),1000)
ax.plot(bestfit_parameters, y_bestfit(bestfit_parameters), color='r')

#To label the bots on the graph
for i in range(number_of_bots):
    if(y[i]>y_bestfit(x[i])):
        ax.annotate(i, (x[i], y[i]), textcoords="offset points", xytext=(0,15), ha='center')
    else:
        ax.annotate(i, (x[i], y[i]), textcoords="offset points", xytext=(0,-15), ha='center')

m_botpath=[]
c_botpath=[]
for i in range(number_of_bots):
    m_botpath.append((y[i]-y_intersection[i])/(x[i]-x_intersection[i]))
    c_botpath.append(y[i]-m_botpath[i]*x[i])
    ax.plot([x[i], x_intersection[i]], [y[i], y_intersection[i]], color='g')
    #This works because when ax.plot() is given y_mindist lists as arguments,it draws a line passing throught the first point and the second point

x_min_dist=[]
y_min_dist=[]
for i in range(number_of_bots):
    points=ax.scatter([x[i]], [y[i]],color='forestgreen')
    x_min_dist.append(np.linspace(x[i],x_intersection[i],100))
    y_min_dist.append(x_min_dist[i]*m_botpath[i]+c_botpath[i])

    def update(frame):
        for i in range(number_of_bots):
                x[i] = x[i] + (x_intersection[i]-x[i]) / 100
                y[i] = y[i] + (y_intersection[i]-y[i]) / 100
        points.set_offsets(np.c_[x, y])
        return points,
    ani = animation.FuncAnimation(fig, update, 100,interval=20, blit=True)

plt.show()



