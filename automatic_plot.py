import numpy as np
import os
from Menu import *
import matplotlib.pyplot as plt
from vasp_plot_band import *


class automatic_plot:
    def __init__(self,which_frame_work):
        if which_frame_work=="1":
            print("VASP plot")
            self.vasp_pl=vasp_plot_band()
            self.vasp_pl.run()


        elif which_frame_work=="2":
            print("Quantum Espresso plot is under release..")

        else:
            print("just_plot")

        self.plot_choises={
            "1" : self.dos_plot,
            "2" : self.band_plot
        }


    def dos_plot(self):
        pass

    def band_plot(self):
        pass
