#VASP plot

import numpy as np
import os
from Menu import *
import matplotlib.pyplot as plt
from read_data import *

class vasp_plot_band(read_data):
    def __init__(self):
        super().__init__()
        self.set_name()
        self.read_data()
        self.set_graph_properties()
        self.plot_pre()
        self.input_choses["8"]=self.plot_pre
        print(self.input_choses["1"])
        self.plot_data()




    def plot_data(self):
        plt.show()


    def plot_pre(self):
        print("BAND Plot Preparation")
        fig = plt.figure()

        ax1 = fig.add_subplot(111)

        ax1.set_title(self.graph_info_data[2])
        ax1.set_xlabel(self.graph_info_data[0])
        ax1.set_ylabel(self.graph_info_data[1])

        ''' has to be changed'''
        lines_file=self.dir+"KLABELS"
        with open(lines_file) as f:
            lines = f.readlines()

        labels = [line.split()[0] for line in lines if len(line.split()) == 2]
        points = [line.split()[1] for line in lines if len(line.split()) == 2]
        print("High Symmetry Points")
        print(labels)
        print(points)
        points= np.array(points)
        x_points = points.astype(np.float)

        for i in range(len(x_points)):
            plt.axvline(x=x_points[i], color='gray', linestyle='--')
            plt.text(x_points[i], ax1.get_ylim()[1], labels[i])

        ax1.plot(self.file_data[0], self.file_data[1], c='r', label='the data')

    def set_name(self):
        self.filename="BAND.dat"
        self.filename_with_dir = self.dir + self.filename

    def set_graph_properties(self):
        self.graph_info_data[0]="K-vector"
        self.graph_info_data[1]="Energy (eV)"
        self.graph_info_data[2]="Band Structure"

