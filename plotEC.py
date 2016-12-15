import numpy as np

def plotEC(plt, a=5, b=4, p=10):
    y, x = np.ogrid[-p:p:100j, -p:p:100j]
    plt.contour(x.ravel(), y.ravel(), pow(y, 2) - pow(x, 3) - x * a - b, [0])
    plt.grid()

if __name__ == '__main__':
    plotEC()