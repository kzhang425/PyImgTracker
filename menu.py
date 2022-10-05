# Import packages and dependencies
import plotting
import sys
import trackpy as tp
import numpy as np
import matplotlib.pyplot as plt


# These are function shortcuts. Don't retype code!
def get_int_input(prompt='') -> int:
    """
    Function that receives user input and returns it as an integer if possible.
    :return:
    int - A pure integer number
    """
    while True:
        try:
            option = int(input(prompt))
        except ValueError:
            print("Invalid Input. Please enter an integer.")
            continue
        else:
            return option

def get_float_input(prompt='') -> float:
    while True:
        try:
            option = float(input(prompt))
        except ValueError:
            print("Invalid Input. Please enter a floating point number.")
            continue
        else:
            return option

# The main class definition starts here:
def show_menu():
    # Define some internal functions for shorthand code

    # Set up menu options with print statements here.
    print("|| MAIN MENU ||")
    print("Input number to select options. For example, input '3' to quit.")
    print("[1] View Input Frames")
    print("[2] Show Histograms")
    print("[2] Locate Features")
    print("[3] View Found Features")
    print("[4] Change Channel")

    # Collect user input
    selection = get_int_input()

    return selection


class Handler:
    def __init__(self, frames):
        # Initialize class attributes
        self.logo = """
#### ##  ### ##     ##      ## ##   ##  ###  ### ##   ##  ##      `|||||`
# ## ##   ##  ##     ##    ##   ##  ##  ##    ##  ##  ##  ##   ~|||  .  |||~~
  ##      ##  ##   ## ##   ##       ## ##     ##  ##  ##  ##   || .  __   ||
  ##      ## ##    ##  ##  ##       ## ##     ##  ##   ## ##   ~||  |++| . ||~
  ##      ## ##    ## ###  ##       ## ###    ## ##     ##     `||.  --    ||
  ##      ##  ##   ##  ##  ##   ##  ##  ##    ##        ##      `|| .  .  ||~~
 ####    #### ##  ###  ##   ## ##   ##  ###  ####       ##        `|||||||`
        """

        self.frames = np.stack(frames)

        # Initialize self.channel, where we can actually choose the channel to work with
        if len(self.frames.shape) == 3:
            self.channel = self.frames
        else:
            self.channel = self.frames[:, 0, :, :]
        # Initialize to None since features are not found yet. This prevents user accessing stuff
        # they shouldn't.
        self.features = None

    # Important functions that do stuff associated with the handler
    def change_channel(self, channel=0):
        # Standardize usage of the frames to this function, where multi-channel things need to be accounted for
        if len(self.frames.shape) == 3:
            print("Image has only one channel, don't bother changing.")
            pass
        else:
            try:
                self.channel = self.frames[:, channel, :, :]
                print("Channel successfully changed.")

            except IndexError:
                print("No channel exists at this index")

    def find_features(self, diameter, min_mass, channel=0):
        self.features = tp.batch(self.channel, diameter, minmass=min_mass)

    def gen_intensity_histograms(self):
        his = np.histogram(np.flatten())


    def show_annotations(self, lower, upper):
        for i in range(lower, upper):
            df = self.features
            df_i = df.loc[df['frame'] == i]
            tp.annotate(df_i, self.channel[i])


    def refine_features(self):
        pass

    # Accessory functions
    def print_logo(self):
        print(self.logo)
