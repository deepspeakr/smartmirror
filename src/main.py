#!/usr/bin/env python
import sys
import tkinter as tk
from tkinter import LEFT, TOP, Frame, Label, N, W, BOTH, BOTTOM, RIGHT
from src.widgets.clock import Clock
from src.widgets.weather import Weather
from widgets.TestWidget import TestWidget


def close_application(event=None):
    # TODO: Make sure no other action is necessary (e.g. properly closing the GUI)
    sys.exit(0)


class Final:
    def __init__(self):
        self.root = tk.Tk()
        self.root.configure(bg="BLACK")
        self.state = False

        self.top = Frame(self.root, bg="BLACK")
        self.top.pack(side=TOP, fill=BOTH)
        self.bottom = Frame(self.root, bg="BLACK")
        self.bottom.pack(side=BOTTOM, fill=BOTH)

        self.time = Clock(self.top)
        self.time.pack(side=RIGHT, anchor=N, pady=60)

        self.weather_show = Weather(self.top)
        self.weather_show.pack(side=LEFT, anchor=N, padx=50, pady=60)

        self.greeting = Label(self.root, text="smartmirror by tomsoch & rysje", font="Arial 10", bg="BLACK", fg="WHITE")
        self.greeting.pack(side=BOTTOM, pady=10)

        self.root.bind("<Return>", self.toggle_fullscreen)
        self.root.bind("<Escape>", self.end_fullscreen)
        self.root.attributes("-fullscreen", 1)
        self.root.mainloop()

    def toggle_fullscreen(self, event=None):
        self.state = not self.state
        self.root.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.root.attributes("-fullscreen", False)
        return "break"


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
    # w = MainWindow()
    # w.tk.mainloop()
    start = Final()
    start.root.mainloop()
