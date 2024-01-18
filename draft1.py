import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

number_of_bots=(int)(input("Enter the number of bots: "))
x=np.random.uniform(0,50,number_of_bots)
y=np.random.uniform(0,50,number_of_bots)


def bestfit():
    m=((np.mean(x)*np.mean(y))-np.mean(x*y))/((np.mean(x)*np.mean(x))-np.mean(x*x))
    c=np.mean(y)-m*np.mean(x)
    return (m,c)

m_bestfit,c_bestfit=bestfit()

def y_bestfit(x):
    return (m_bestfit*x)+c_bestfit

plt.scatter(x,y,color='r')
plt.plot(x,y_bestfit(x),color='b')


def botpath():
    m_botpath=(-1/m_bestfit)
    c_botpath=y-m_botpath*x
    x_intersection=(c_bestfit-c_botpath)/(m_botpath+(1/m_botpath))
    return (m_botpath,c_botpath,x_intersection)

m_botpath,c_botpath,x_intersection=botpath()

def y_botpath(x):
    return (m_botpath*x)+c_botpath
# fig, ax = plt.subplots()
# for i in x:
#     ax.plot(i,botpath(i,y[x.index(i)])[0],color='m')
#     if(i>botpath(i,y[x.index(i)])):
#         ax.set_xlim(botpath(i,y[x.index(i)])[1],i)
#     else:
#         ax.set_xlim(i,botpath(i,y[x.index(i)])[1])


for i in range(0,number_of_bots-1):
    if(x[i]<x_intersection[i]):
        x_botpath = np.linspace(x[i],x_intersection[i],number_of_bots)
        plt.plot(x_botpath,y_botpath(x_botpath),[x[i],x_intersection[i]] ,color='forestgreen')
        #plt.set_xlim(x[i],x_intersection[i])
    else:
        x_botpath = np.linspace(x_intersection[i],x[i],number_of_bots)
        plt.plot(x_botpath,y_botpath(x_botpath),[x_intersection[i],x[i]], color='forestgreen')
        #plt.set_xlim(x_intersection[i],x[i])


plt.grid()
plt.show()