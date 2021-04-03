from analysis import wind_direction,speed
from windrose import WindroseAxes
import matplotlib.cm as cm
import numpy as np
import matplotlib.pyplot as plt

wind_direction=np.round(wind_direction)

ax = WindroseAxes.from_ax()
ax.contourf(wind_direction, speed, bins=np.arange(0, 8, 1), cmap=cm.winter)
ax.set_legend()
xlabels = ('E','N-E','N','N-W','W','S-W','S','S-E')
ax.set_xticklabels(xlabels)

plt.show()


