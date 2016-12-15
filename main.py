import math
import matplotlib.pyplot as plot
from plotEC import plotEC

# Set Dimention
P = 7 

# Elliptic curve params
a = 5
b = 18

# Create elliptic curve graph
plotEC(plot, a, b, P)

# Display points
plot.plot([1,2,3,4], [1,4,-5,6], 'ro')


# Show graph
plot.show()

'''from ec import EC
ec = EC(a, b, q)
print ec.at(13)'''