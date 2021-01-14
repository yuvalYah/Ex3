import numpy as np
import matplotlib.pyplot as plt
from numpy.matlib import rand



def G_10_80():
    plt.bar([1, 3, 5], [0.0, 0.0, 0.0], width=0.5)  # ntworkx
    plt.bar([1.5, 3.5, 5.5], [0.001, 0.0, 0.000999], width=0.5)  # python
    plt.bar([2, 4, 6], [0.488, 0.06, 0.09], width=0.5)  # java
    x = [u'networkx', u'python', u'java', u'networkx', u'python', u'java', u'networkx', u'python', U'java']
    plt.legend(["ntworkx", "python", "java"], loc="upper right")
    plt.xlabel("     shortest path          connected_components           connected_component")

    plt.title(f'G_10_80')

    plt.show()


def G_100_800():
    plt.bar([1, 3, 5], [0.007126, 0.0, 0.0], width=0.5)  # ntworkx
    plt.bar([1.5, 3.5, 5.5], [0.43533, 0.0093, 0.0079], width=0.5)  # python
    plt.bar([2, 4, 6], [0.19758, 0.8, 0.6432], width=0.5)  # java
    plt.legend(["ntworkx", "python", "java"], loc="upper right")
    plt.xlabel("     shortest path          connected_components           connected_component")

    plt.title(f'G_100_800')
    plt.show()

def G_1000_8000():
    plt.bar([1, 3, 5], [0.00918, 0.0, 0.0], width=0.5)  # ntworkx
    plt.bar([1.5, 3.5, 5.5], [1.319, 0.1741, 0.016], width=0.5)  # python
    plt.bar([2, 4, 6], [3.6, 22.37, 17.10999], width=0.5)  # java
    plt.legend(["ntworkx", "python", "java"], loc="upper right")
    plt.xlabel("     shortest path          connected_components           connected_component")

    plt.title(f'G_1000_8000')
    plt.show()

def G_10000_80000():
    plt.bar([1, 3, 5], [0.0426991, 0.0, 0.0], width=0.5)  # ntworkx
    plt.bar([1.5, 3.5, 5.5], [30, 25, 15], width=0.5)  # python
    plt.bar([2, 4, 6], [38.765, 29.34, 23.152], width=0.5)  # java
    plt.legend(["ntworkx", "python", "java"], loc="upper right")
    plt.xlabel("     shortest path          connected_components           connected_component")

    plt.title(f'G_10000_80000')
    plt.show()

def G_20000_160000():
    plt.bar([1, 3, 5], [0.135, 0.0151, 0.0], width=0.5)  # ntworkx
    plt.bar([1.5, 3.5, 5.5], [2.2, 2, 1.5], width=0.5)  # python
    plt.bar([2, 4, 6], [3.6, 3.1, 2.1099], width=0.5)  # java
    plt.legend(["ntworkx", "python", "java"], loc="upper right")
    plt.xlabel("     shortest path          connected_components           connected_component")

    plt.title(f'G_20000_160000')
    plt.show()




if  __name__ == '__main__':
    G_10_80()
    G_100_800()
    G_1000_8000()
    G_10000_80000()
    G_20000_160000()