#!/usr/bin/env python
import sys
import tkinter as tk

from widgets.TestWidget import TestWidget


def close_application(event=None):
    # TODO: Make sure no other action is necessary (e.g. properly closing the GUI)
    sys.exit(0)


class MainWindow:
    def __init__(self):
        # initialize tkinter root window
        self.tk = tk.Tk()
        self.tk.configure(background="black")
        # start in fullscreen; escape closes the window
        self.tk.attributes("-fullscreen", 1)
        self.tk.bind("<Escape>", close_application)
        # add test widget
        self.test_widget = TestWidget(self.tk)
        # TODO: dimensions should be defined by constants inside the widget
        # in the future, position will be defined in a config file
        self.test_widget.place(height=100, width=300, x=800, y=300)


if __name__ == "__main__":
    w = MainWindow()
    w.tk.mainloop()
