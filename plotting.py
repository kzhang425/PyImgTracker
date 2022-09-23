import matplotlib.pyplot as plt
import trackpy as tp
import pims
import sys
import napari



def show_frame(frames, n):
    plt.imshow(frames[n])
    plt.show()

# Note necessarily useful
def frame_plot(frames):
    # Define some useful parameters here:
    length = frames.frame_shape[0]

    # Here, define user input/logic section
    while True:
        print("Enter frame number to view. Input 'Q' to quit and return to main menu.")
        f_num = input("Enter frame # to view:")
        if f_num == "Q":
            break
        try:
            f_int = int(f_num)
        except ValueError:
            print("Input is not a number, please try again.")
            continue
        else:
            try:
                show_frame(frames, f_int-1)
            except:
                print("Index out of range.")
                print("Max frame number is " + str(length) + ".")
                print("Min frame number is 1.")
                continue

def viewer(data):
    viewer = napari.view_image(data)
    napari.run()