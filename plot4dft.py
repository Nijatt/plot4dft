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
            "0": self.quit
        }

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
                      0.  Quit """)

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



    def qespresso(self):
        print("Quantum Espresso ----->")


    def plot_dos(self):
        print("Density of States plot....")
        plotdos=DOS_plot()
        #plotdos.plot()



    def plot_band(self):
        print("Band Structure plot.....")
        plotband=BAND_plot()

    def quit(self):
        print(""" Thank you for using plot4DFT...
                   Developed by Nijat Shukurov / Ankara University
                   (c) All Right are reserved..
                    """)
        sys.exit(0)

Menu().run()
