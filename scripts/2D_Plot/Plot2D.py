import numpy as np
import os
from Menu import *
import matplotlib.pyplot as plt
import numbers

class Plot2D:
    def __init__(self):
        self.quit = True
        self.filename = ""
        self.filename_with_dir = ""
        self.dir = os.path.dirname(os.path.abspath(__file__)).__add__('\\')
        self.file_data = []
        #graph names

        self.graph_info_data=[]
        self.graph_info_data.append("X data")
        self.graph_info_data.append("Y data")
        self.graph_info_data.append("Title: 2D plot")

        self.input_choses = {
            "1": self.set_name,
            "2": self.read_data,
            "3": self.get_name,
            "4": self.get_file_path,
            "5": self.display_data,
            "6": self.change_graph_info,
            "7": self.plot_data,
            "0": self.menu
        }

    def __del__(self):
        pass

    # self.set_name()
    # self.get_name()
    # self.read_data()
    # self.print_data()

    def display_menu(self):
        print(
 """ 
 ************READ DATA**************
 1.  What is name of file?"""+ " --> "+self.filename+ """
 2.  Read data file.
 3.  Display file name.
 4.  Display file directory. 
 5.  Show data.
 6.  Change graph parameters. 
 7.  Plot data graph.
 0.  Close """)

    def run(self):
        '''Display the menu and respond to choices.'''
        while self.quit == True:
            self.display_menu()
            choice = input("Enter an option>> ")
            action = self.input_choses.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def read_data(self):
        with open(self.filename_with_dir) as f:
            lines = f.readlines()

        print(lines)

        x_data=[]
        y_data=[]
        for line in lines:
            if len(line.split())==2:
                try:
                    x_data.append(float(line.split()[0]))
                    y_data.append(float(line.split()[1]))
                except:
                    print("Data Line Error")

        #x_data = [line.split()[0] for line in lines if len(line.split()) == 2 and isinstance(float(line.split()[0]),numbers.Number) ]
        #y_data = [line.split()[1] for line in lines if len(line.split()) == 2 and isinstance(float(line.split()[0]),numbers.Number) ]

        x_data = np.array(x_data)
        x = x_data.astype(np.float)

        y_data = np.array(y_data)
        y = y_data.astype(np.float)

        self.file_data.append(x)
        self.file_data.append(y)
        print("File Successfully Stored.")

    def display_data(self):
        print(self.graph_info_data[0])
        print(self.file_data[0])
        print(self.graph_info_data[1])
        print(self.file_data[1])


    def change_graph_info(self):
        for i in range(len(self.graph_info_data)):
            self.graph_info_data[i] = input(self.graph_info_data[i]+" --> ")



    def get_name(self):
        print(self.filename)

    def get_file_path(self):
        print(self.dir)
        print(self.filename_with_dir)

    def set_name(self):
        data_name = input("Enter file name >> ")
        self.filename = data_name
        self.filename_with_dir = self.dir + self.filename

    def store_data(self):
        pass

    def set_quit_true(self):
        self.quit=True


    def plot_data(self):
        fig = plt.figure()

        ax1 = fig.add_subplot(111)

        ax1.set_title(self.graph_info_data[2])
        ax1.set_xlabel(self.graph_info_data[0])
        ax1.set_ylabel(self.graph_info_data[1])

        ax1.plot(self.file_data[0], self.file_data[1], c='r', label='the data')

        plt.show()

    def menu(self):
        self.quit = False
