#VASP plot

import numpy as np
import os
from Menu import *
import matplotlib.pyplot as plt
import matplotlib.pyplot

from read_data import *

class QE_Phonon_BAND_DOS_plot(read_data):
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

        #ax1 = fig.add_subplot(121)
        #ax2= fig.add_subplot(122)

       # fig, axs = plt.subplots(1, 2, gridspec_kw={'width_ratios': [3, 1]})
        ax1,ax2=fig.subplots(1, 2, gridspec_kw={'width_ratios': [3, 1]})

        ax1.set_title(self.graph_info_data[2])
        ax1.set_xlabel(self.graph_info_data[0])
        ax1.set_ylabel(self.graph_info_data[1])

        ''' has to be changed'''
        lines_file=self.dir+"KLABELS"
        with open(lines_file) as f:
            lines = f.readlines()

        labels = [line.split()[0] for line in lines if len(line.split()) == 2]
        points = [line.split()[1] for line in lines if len(line.split()) == 2]

       # ax1.xticks(np.arange(0, 1, step=0.2))

        print("High Symmetry Points")
        print(labels)
        print(points)
        points= np.array(points)
        x_points = points.astype(np.float)

        for i in range(len(x_points)):
            ax1.axvline(x=x_points[i], color='gray', linestyle='--')
            #ax1.text(x_points[i], ax1.get_ylim()[1], labels[i]) labels

        ax1.scatter(self.file_data[0], self.file_data[1], c='r', label='the data',s=2)
        ax1.set_xticks(x_points)
        ax1.set_xticklabels(labels)


        ##ax2 for dos calculations
        dos_file = self.dir + "TDOS.txt"
        with open(dos_file) as f:
            lines = f.readlines()

        x_data = [line.split()[0] for line in lines if len(line.split()) == 2]
        y_data = [line.split()[1] for line in lines if len(line.split()) == 2]

        x_data = np.array(x_data)
        x = x_data.astype(np.float)

        y_data = np.array(y_data)
        y = y_data.astype(np.float)

        ax2.yaxis.tick_right()
        #ax2.get_xaxis().set_visible(False)
        ax2.xaxis.set_visible(False)

        ax2.set_title("Phonon DOS")


        #ax2.set_xlabel('Energy (eV)')
        #ax2.set_ylabel('DOS ')

        ax2.plot(y, x, c='b', label='the data')

    def set_name(self):
        self.filename="BAND.dat"
        self.filename_with_dir = self.dir + self.filename

    def set_graph_properties(self):
        self.graph_info_data[0]=""
        self.graph_info_data[1]=r'$Frequency  (cm^{-1})$'
        self.graph_info_data[2]="Phonon BAND Structure"

