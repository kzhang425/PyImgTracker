# Imports are here:
import numpy as np
import pims
import nd2
import trackpy as tp
import matplotlib.pyplot as plt
import plotting as pt
import tkinter as tk
from tkinter import filedialog as fd
import menu
import os
import sys

# Test parameters are here:
default_file = "./example/Single_molecule_moving.tif"
use_default_file = False

# Helper functions
def cls():
    os.system('clear' if os.name=='posix' else 'cls')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if use_default_file:
        filepath = default_file
    else:
        root = tk.Tk()
        root.withdraw()
        filepath = fd.askopenfilename()
        root.destroy()


    # Assign data to a Handler object which will be the centerpiece of this wrapper. See menu.py.
    if filepath[-4:] == '.nd2':
        # Handle nikon filetypes
        handler = menu.Handler(nd2.imread(filepath))
    else:
        handler = menu.Handler(pims.open(filepath))


    while True:
        cls()
        handler.print_logo()
        selection = menu.show_menu()
        match selection:
            case 1:  # Simply continuously plot stuff until user wants to quit
                pt.viewer(np.stack(handler.frames))

            case 2:  # A little more complex workflow, requires more user input. Finds features.

                # Here we need an odd integer as a diameter
                while True:
                    dia = menu.get_int_input(
                        "Estimate the diameter of the particles to be tracked (in pixels):"
                    )
                    if dia % 2 == 1:
                        break
                    else:
                        print("Diameter must be odd. Please enter an odd integer")
                        continue

                min_mass = menu.get_float_input("Minimum \"Mass\" to be considered:")
                handler.find_features(dia, min_mass)
                if input("Features found, write to file? (Type 'y' to confirm)") == 'y':
                    handler.features.to_csv("features.csv")
                else:
                    continue

            case 3:  # View the found features as annotations on the plots
                if handler.features is None:
                    print("Features have not been found yet")
                    continue

                handler.show_annotations()

            case 4:
                sys.exit()







