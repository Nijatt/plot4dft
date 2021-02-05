import numpy as np
import os
from Menu import *
import matplotlib.pyplot as plt


class read_data:
    def __init__(self):
        self.quit = True
        self.filename = ""
        self.filename_with_dir = ""
        self.dir = os.path.dirname(os.path.abspath(__file__)).__add__('\\')
        self.file_data = []
        self.data_name_for_x = "X data"
        self.data_name_for_y = "Y data"

        self.input_choses = {
            "1": self.set_name,
            "2": self.read_data,
            "3": self.get_name,
            "4": self.get_file_path,
            "5": self.display_data,
            "0": self.menu
        }

    def __del__(self):
        print("CLOSED")

    # self.set_name()
    # self.get_name()
    # self.read_data()
    # self.print_data()

    def display_menu(self):
        print(""" READ DATA---->
                      1.  Set file name
                      2.  Read data file
                      3.  Display file name
                      4.  Display file dir 
                      5.  Show file data 
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

        x_data = [line.split()[0] for line in lines if len(line.split()) == 2]
        y_data = [line.split()[1] for line in lines if len(line.split()) == 2]

        x_data = np.array(x_data)
        x = x_data.astype(np.float)

        y_data = np.array(y_data)
        y = y_data.astype(np.float)
        self.file_data.append(x)
        self.file_data.append(y)
        print("file successfully stored.")

    def display_data(self):
        print(self.data_name_for_x)
        print(self.file_data[0])
        print(self.data_name_for_y)
        print(self.file_data[1])

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


    def menu(self):
        self.quit = False
