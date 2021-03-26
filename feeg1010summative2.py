# TANG YONG HUA 26/03/2021

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.interpolate import pchip

mpl.rcParams['text.usetex'] = True
mpl.rc('font', family='Arial')

# data
temp = [-60., 20., 90.]
impact_energy_al = [9.932, 8.126, 9.932]
impact_energy_steel = [11.747, 11.772, 5.714]


# generate splines
temp_new = np.linspace(temp[0], temp[len(temp)-1], 300)

spl = pchip(temp, impact_energy_al)
spline_al = spl(temp_new)

spl = pchip(temp, impact_energy_steel)
spline_steel = spl(temp_new)


# plot graphs
plt.plot(temp, impact_energy_al, 'k.')
plt.plot(temp, impact_energy_steel, 'kx')
plt.plot(temp_new, spline_al, 'r-', label='Aluminium')
plt.plot(temp_new, spline_steel, 'b-', label='Steel')
plt.xlabel('Temperature ($^{\circ}$C)')
plt.ylabel('Impact energy $K$ (J)')
plt.xlim(-60., 100)
plt.grid()
plt.legend()
plt.show()
