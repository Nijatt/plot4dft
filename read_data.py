import numpy as np
import matplotlib.pyplot as plt


class read_data:
    def __init__(self):
        self.filename = ""
        self.file_data = []
       # self.set_name()
       # self.get_name()
       # self.read_data()
       # self.print_data()

    def read_data(self):
        with open(self.filename) as f:
            lines = f.readlines()

        x_data = [line.split()[0] for line in lines if len(line.split()) == 2]
        y_data = [line.split()[1] for line in lines if len(line.split()) == 2]

        x_data = np.array(x_data)
        x = x_data.astype(np.float)

        y_data = np.array(y_data)
        y = y_data.astype(np.float)
        self.file_data.append(x)
        self.file_data.append(y)

    def display_data(self):
        print(self.file_data[0])
        print(self.file_data[1])

    def get_name(self):
        print(self.filename)

    def set_name(self):
        data_name = input("Enter file name >> ")
        self.filename = data_name
