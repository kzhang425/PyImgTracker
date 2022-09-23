import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RangeSlider
import pims

def gui(input_img):
# read in an image, usually np.array kind. This one will be a stack of images
# Initialize the frame number to be zero, since array indexing
    frame = 0
    img = input_img

    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    plt.subplots_adjust(bottom=0.25)


    im = axs[0].imshow(img[frame])
    axs[1].hist(img.flatten(), bins='auto')
    axs[1].set_title('Histogram of pixel intensities')

    # Create the RangeSlider
    slider_ax = plt.axes([0.20, 0.1, 0.60, 0.03])
    slider = RangeSlider(slider_ax, "Threshold", img[frame].min(), img[frame].max())

    # Create the Vertical lines on the histogram
    lower_limit_line = axs[1].axvline(slider.val[0], color='k')
    upper_limit_line = axs[1].axvline(slider.val[1], color='k')


    def update(val):
        # The val passed to a callback by the RangeSlider will
        # be a tuple of (min, max)

        # Update the image's colormap
        im.norm.vmin = val[0]
        im.norm.vmax = val[1]

        # Update the position of the vertical lines
        lower_limit_line.set_xdata([val[0], val[0]])
        upper_limit_line.set_xdata([val[1], val[1]])

        # Redraw the figure to ensure it updates
        fig.canvas.draw_idle()


    slider.on_changed(update)
    plt.show()

# Test case
gui(np.array(pims.open("./example/Single_molecule_moving.tif")))