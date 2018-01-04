import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import future        # pip install future
import builtins      # pip install future
import past          # pip install future
import six           # pip install six
# Iterations;Meilleure Fitness;Moyenne Fitness
file = open("graph.txt", "r")

aux_line = []

for line in file:
   aux_line = line.split(";")
   # print(aux_line)
   # print(aux_line[0]+"-"+aux_line[1]+"-"+aux_line[2])


# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 30)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--')
plt.show()

a = 3

print(a+float(aux_line[0]))