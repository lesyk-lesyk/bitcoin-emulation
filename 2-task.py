import math
import matplotlib.pyplot as plot
from coord import Coord

# Set Dimention
P = 11 

# Elliptic curve params
a = 2
b = 4

from ec import EC
ec = EC(a, b, P)

# Adding points
p1 = Coord(2, 4)
p2 = Coord(3, 9)
p3 = ec.add(p1, p2)

print p1
print p2
print p3

# Snversing points
p4 = ec.neg(p3)
print p4

# multiplying by the number
p5 = ec.mul(p1, 2)
print p5

# All points on Elliptic curve
points = []
for i in range(P):
  for j in range (P):
    if ec.is_valid(Coord(i, j)):
      points.append(Coord(i, j))


# All points on Elliptic curve
plot.scatter(*zip(*points), color='b')

# Start points
plot.scatter(*zip(*[p1,p2]), color='y', s=100)

# Sum
plot.scatter(*zip(*[p3]), color='g', s=100)

# Inverse
plot.scatter(*zip(*[p4]), color='r', s=100)
plot.plot(*zip(*[p3,p4]), color='r')

# Multiplication
plot.scatter(*zip(*[p5]), color='#800080', s=100)

plot.show()
