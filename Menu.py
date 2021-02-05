# basic plot program
#Nijat Shukurov
'''
DFT outputs:
    * BAND structure
    * Density of States

Output of DFT programs:
    * VASP
    * Quantum Espresso
'''

import sys
from BAND_plot import *
from DOS_plot import *
from read_data import *
from automatic_plot import *



class Menu:
    def __init__(self):
        self.input_choses={
            "1": self.plot_band,
            "2": self.plot_dos,
            "3": self.run,
        }

        self.framework_choises={
            "1": self.vasp,
            "2": self.qespresso,
            "0": self.quit,
            "4": self.input_data,
            "5": self.automatic

        }
        self.test_data=read_data()

    def display_plot_menu(self):
        print("""
               1. BAND Structure
               2. Density of States
               3. Back to Menu
              """)

    def display_menu(self):
            print(""" Notebook Menu
                      1.  VASP
                      2.  Quantum Espresso
                      0.  Quit 
                      4.  Manual 2D plot
                      5.  Automatic Plot """)

    def display_intro(self):
            print("""^
                     |                  *
                     |     * *         *
                     |   *     *      *
                     |  *       *    *
                     | *          * *
                     0--------------------->   PLOT4DFT ....""")

    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_intro()
            self.display_menu()
            choice = input("Enter an option>> ")
            action = self.framework_choises.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def vasp(self):
        while True:
            print("VASP ------>")
            self.display_plot_menu()
            choice = input("Enter an option for vasp >> ")
            action = self.input_choses.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def automatic(self):
        auto_plot=automatic_plot("1")



    def qespresso(self):
        print("Quantum Espresso ----->")


    def plot_dos(self):
        print("Density of States plot....")
        plotdos=DOS_plot()
        #plotdos.plot()



    def plot_band(self):
        print("Band Structure plot.....")
        plotband=BAND_plot()

    def input_data(self):
        self.test_data.set_quit_true()
        self.test_data.run()
        print("end ")



    def quit(self):
        print(""" Thank you for using plot4DFT...
                   Developed by Nijat Shukurov / Ankara University
                   (c) All Right are reserved..
                    """)
        sys.exit(0)

#Menu().run()
