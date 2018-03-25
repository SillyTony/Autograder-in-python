"""

"""
from Grading_GUI import GraderGui
from tkinter import *

WINDOW_WIDTH = 670
WINDOW_HEIGHT = 400

def main():
    root = Tk()

    # get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (WINDOW_WIDTH / 2)
    y = (hs / 2) - (WINDOW_HEIGHT / 2)
    # set the dimensions of the screen and where it is placed
    root.geometry('%dx%d+%d+%d' % (WINDOW_WIDTH, WINDOW_HEIGHT, x, y))
    root.wm_title("Grading Program")

    myGui = GraderGui(root)

    root.mainloop()


main()