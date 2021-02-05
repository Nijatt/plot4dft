import numpy as np
import matplotlib.pyplot as plt


class BAND_plot:
    def __init__(self):
        self.plot()

    def plot(self):
        with open('BAND.dat') as f:
            lines = f.readlines()


        x_data = [line.split()[0] for line in lines if len(line.split())==2]
        y_data = [line.split()[1] for line in lines if len(line.split())==2]



        x_data = np.array(x_data)
        x = x_data.astype(np.float)


        y_data = np.array(y_data)
        y = y_data.astype(np.float)

        # print(x)
        # print(y)

        fig = plt.figure()

        ax1 = fig.add_subplot(111)

        ax1.set_title("Band Structure  [BC unit cell] ")
        ax1.set_xlabel('K-vector')
        ax1.set_ylabel('Energy (eV) ')

        #ax1.set_title("Density of States  [BC unit cell] ")
        #ax1.set_xlabel('Energy (eV)')
        #ax1.set_ylabel('DOS ')

        plt.axvline(x=0.000,color='gray',linestyle='--')
        plt.text(0.000, ax1.get_ylim()[1],"G")

        plt.axvline(x=1.353,color='gray',linestyle='--')
        plt.text(1.353, ax1.get_ylim()[1],"M")

        plt.axvline(x=2.134,color='gray',linestyle='--')
        plt.text(2.134, ax1.get_ylim()[1],"K")

        plt.axvline(x=3.695,color='gray',linestyle='--')
        plt.text(3.695, ax1.get_ylim()[1],"G")

        ax1.plot(x, y, c='r', label='the data')

        plt.show()
