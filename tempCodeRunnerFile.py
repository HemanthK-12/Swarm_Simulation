# Create the figure and the line that we will manipulate
# fig, ax = plt.subplots()
# line, = ax.plot(bestfit_parameters, y_bestfit(bestfit_parameters), color='b')

# # The function that makes the animation.
# def update(num, x, y, line):
#     line.set_data(x[:num], y[:num])
#     line.axes.autoscale()
#     return line,

# ani = animation.FuncAnimation(fig, update, number_of_bots, fargs=[bestfit_parameters, y_bestfit(bestfit_parameters), line],
#                               interval=100, blit=True)
