# TANG YONG HUA 24/03/2021

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.interpolate import pchip

mpl.rcParams['text.usetex'] = True
mpl.rc('font', family='Arial')

mperrev = 1E-4  # m
area_al = 5.8E-6  # m^2
force_per_div_al = 13.25  # N
area_steel = 14.87E-6  # m^2
force_per_div_steel = 104.79  # N

# [*number of revolutions*, *DTI read-out divisions*]
al_cold = np.array([
    [0, 0],
    [5, 16],
    [8, 30],
    [11, 45],
    [13, 55],
    [15, 65],
    [19, 70],
    [27, 78],
    [37, 84],
    [46, 89],
    [81, 97.5]
])

al_cold[:, 0] = al_cold[:, 0] * mperrev / 80E-3
al_cold[:, 1] = al_cold[:, 1] * force_per_div_al / area_al / 1E9  # GPa

al_room = np.array([
    [0, 0],
    [10, 25.5],
    [20, 65.5],
    [30, 74.5],
    [40, 81],
    [50, 87],
    [60, 89.5],
    [70, 93],
    [80, 93.5]
])

al_room[:, 0] = al_room[:, 0] * mperrev / 71E-3
al_room[:, 1] = al_room[:, 1] * force_per_div_al / area_al / 1E9  # GPa

al_hot = np.array([
    [0, 0.0],  ###
    [6, 4],
    [10, 23],
    [12, 32],
    [14, 43],
    [16, 53],
    [18, 65],
    [20, 76],
    [22, 81],
    [24, 96],
    [26, 100],
    [28, 102],
    [30, 104],
    [32, 105],
    [34, 106],
    [36, 106],
    [38, 108],
    [40, 108],
    [42, 108],
    [44, 109],
    [46, 109],
    [48, 109],
    [50, 110]
])

al_hot[:, 0] = al_hot[:, 0] * mperrev / 70E-3
al_hot[:, 1] = al_hot[:, 1] * force_per_div_al / area_al / 1E9  # GPa

steel_cold = np.array([
    [0, 0],
    [4, 27],
    [5, 40],
    [7, 49],
    [8, 56.5],
    [9, 64],
    [10, 71.5],
    [11, 79],
    [12, 84.5],
    [13, 90],
    [14, 91],
    [15, 103],
    [20, 138],
    [25, 176],
    [30, 213],
    [35, 242],
    [40, 265],
    [45, 281],
    [48, 287],
    [51, 292],
    [54, 296],
    [57, 305],
    [60, 315],
    [63, 319],
    [66, 323],
    [69, 326],
    [72, 334],
    [75, 336],
    [79, 346],
    [83, 356],
    [87, 361],
    [91, 357],
    [95, 363],
    [99, 366],
    [103, 361],
    [113, 375],
    [123, 376],
    [133, 378],
    [141, 382],
    [161, 388],
    [171, 400],
    [181, 394]
])

steel_cold[:, 0] = steel_cold[:, 0] * mperrev / 50E-3
steel_cold[:, 1] = steel_cold[:, 1] * force_per_div_steel / area_steel / 1E9  # GPa

steel_room = np.array([
    [0, 0.0],
    [5, 55],
    [10, 106],
    [15, 152],
    [20, 163],
    [25, 197],
    [30, 229],
    [35, 265],
    [40, 303],
    [45, 335],
    [50, 349],
    [55, 366],
    [60, 379],
    [65, 391],
    [70, 400],
    [75, 408],
    [85, 422],
    [95, 431],
    [130, 433],
    [245, 420]
])

steel_room[:, 0] = steel_room[:, 0] * mperrev / 50.67E-3
steel_room[:, 1] = steel_room[:, 1] * force_per_div_steel / area_steel / 1E9  # GPa

steel_hot = np.array([
    [0, 0.0],
    [10, 63],
    [16, 109],
    [20, 130],
    [26, 174],
    [30, 200],
    [35, 212],
    [40, 230],
    [45, 241],
    [50, 250],
    [55, 255],
    [60, 263],
    [63, 268],
    [69, 273],
    [75, 277],
    [80, 282],
    [83, 284],
    [88, 285],
    [95, 289],
    [100, 291],
    [105, 293],
    [110, 294],
    [115, 296],
    [120, 297],
    [125, 299],
    [130, 299],
    [140, 300],
    [150, 302],
    [155, 300],
    [170, 298],
    [180, 299],
    [185, 296],
    [195, 290],
    [205, 275],
    [210, 270]
])

steel_hot[:, 0] = steel_hot[:, 0] * mperrev / 52.5E-3
steel_hot[:, 1] = steel_hot[:, 1] * force_per_div_steel / area_steel / 1E9  # GPa

if __name__ == '__main__':
    # al_cold
    xnew_al_cold = np.linspace(al_cold[0, 0], al_cold[len(al_cold)-1, 0], 300)
    spl = pchip(al_cold[:, 0], al_cold[:, 1])
    spline_al_cold = spl(xnew_al_cold)

    # al_room
    xnew_al_room = np.linspace(al_room[0, 0], al_room[len(al_room) - 1, 0], 300)
    spl = pchip(al_room[:, 0], al_room[:, 1])
    spline_al_room = spl(xnew_al_room)

    # al_hot
    xnew_al_hot = np.linspace(al_hot[0, 0], al_hot[len(al_hot) - 1, 0], 300)
    spl = pchip(al_hot[:, 0], al_hot[:, 1])
    spline_al_hot = spl(xnew_al_hot)

    # steel_cold
    xnew_steel_cold = np.linspace(steel_cold[0, 0], steel_cold[len(steel_cold) - 1, 0], 300)
    spl = pchip(steel_cold[:, 0], steel_cold[:, 1])
    spline_steel_cold = spl(xnew_steel_cold)

    # steel_room
    xnew_steel_room = np.linspace(steel_room[0, 0], steel_room[len(steel_room) - 1, 0], 300)
    spl = pchip(steel_room[:, 0], steel_room[:, 1])
    spline_steel_room = spl(xnew_steel_room)

    # steel_hot
    xnew_steel_hot = np.linspace(steel_hot[0, 0], steel_hot[len(steel_hot) - 1, 0], 300)
    spl = pchip(steel_hot[:, 0], steel_hot[:, 1])
    spline_steel_hot = spl(xnew_steel_hot)

    plt.xlabel('Strain, $\epsilon$')
    plt.ylabel('Stress, $\sigma$ (GPa)')

    # choose the material to plot
    material = 'steel'

    if material == 'al':
        plt.plot(xnew_al_cold, spline_al_cold, 'b-', label='Al, cold')
        plt.plot(xnew_al_room, spline_al_room, 'g-', label='Al, room')
        plt.plot(xnew_al_hot, spline_al_hot, 'r-', label='Al, hot')
    elif material == 'steel':
        plt.plot(xnew_steel_cold, spline_steel_cold, 'b-', label='Steel, cold')
        plt.plot(xnew_steel_room, spline_steel_room, 'g-', label='Steel, room')
        plt.plot(xnew_steel_hot, spline_steel_hot, 'r-', label='Steel, hot')

    plt.grid()
    plt.legend()
    plt.show()
