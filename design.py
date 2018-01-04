import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
# evenly sampled time at 200ms intervals
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import future        # pip install future
import builtins      # pip install future
import past          # pip install future
import six           # pip install six
# Iterations;Meilleure Fitness;Moyenne Fitness


file = open("graph1.txt", "r")

aux_line = []
y =[[] for _ in range(4)]
# Moyenne Fitness


for line in file:
   aux_line = line.split(";")
   print(aux_line)
   y[0].append(float(aux_line[0]))
   y[1].append(float(aux_line[1]))
   y[2].append(float(aux_line[2]))
   y[3].append(float(aux_line[3]))
   # print(aux_line)
   # print(aux_line[0]+"-"+aux_line[1]+"-"+aux_line[2])


# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 30)

# red dashes, blue squares and green triangles


fig0 = plt.figure()
ax0 = fig0.add_subplot(111)
ax0.grid(True)
gridlines = ax0.get_xgridlines() + ax0.get_ygridlines()

plt.yscale('linear')
plt.xscale('linear')
print(gridlines)
for line in gridlines:
    line.set_linestyle('-.')
# ax0.grid(color='b', linestyle='-', linewidth=0.1)


plt.plot(y[0], y[3], 'bs',y[0], y[3])
plt.ylabel('Distance')
plt.xlabel('Iterations')

# Meilleure Fitness;Moyenne Fitness
blue_patch = mpatches.Patch(color='blue', label='Moyenne Distance')
plt.legend(handles=[blue_patch])

plt.show()