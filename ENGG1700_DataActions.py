"""
    Classes and function for ENGG1700 data
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class Array:
    def __init__(self, data_set=0):
        self.pre_sets = {
                            0:[0, 1, 2],
                            1:[3,4, 5],
                            2:[6, 7, 8]
                        }
        self.aE = np.empty(shape=(0,0))
        self.aY = np.empty(shape=(0,0))
        self.aU = np.empty(shape=(0,0))
        self.data_set = self.pre_sets[data_set]

    def add(self, data_value):
        self.aE = np.append(self.aE,data_value[self.data_set[0]])
        self.aY = np.append(self.aY, data_value[self.data_set[1]])
        self.aU = np.append(self.aU, data_value[self.data_set[2]])

    def remove_blanks(self):
        x = 0
        for index, value in enumerate(self.aE):
            if value == '':
                self.aE = np.delete(self.aE, index-x)
                x += 1
            else: continue

        x = 0
        for index, value in enumerate(self.aY):
            if value == '':
                self.aY = np.delete(self.aY, index-x)
                x += 1
            else: continue

        x = 0
        for index, value in enumerate(self.aU):
            if value == '':
                self.aU = np.delete(self.aU, index-x)
                x += 1
            else: continue

    def return_values(self):
        return self.aE, self.aY, self.aU

    def scatter(self):
        x =  len(self.aE)+1
        ax = np.arange(1, x, dtype=int)
        y = len(self.aY)+1
        ay = np.arange(1, y, dtype=int)
        z = len(self.aU)+1
        az = np.arange(1, z, dtype=int)

        plt.scatter(ax, self.aE)
        plt.ylabel("young's modulus MPa")
        plt.title("young's modulus scattered")
        plt.grid(True)
        plt.show()

        plt.scatter(ay, self.aY)
        plt.ylabel("Yield Stress MPa")
        plt.title("Yield Stress")
        plt.grid(True)
        plt.show()

        plt.scatter(az, self.aU)
        plt.ylabel("UTS ")
        plt.title("Ultimate tensile strength")
        plt.grid(True)
        plt.show()

def data(file_path, *material):
    arr = np.loadtxt(file_path, delimiter=',', skiprows=1, dtype=str)
    for i in arr:
        material[0].add(i)
        material[1].add(i)
        material[2].add(i)