#!/usr/bin/env python
import sys
import tkinter as tk

from widgets.calendar import Calendar
from widgets.clock import Clock
from widgets.news import News
from widgets.weather import Weather
from widgets.TestWidget import TestWidget


def close_application(event=None):
    # TODO: Make sure no other action is necessary (e.g. properly closing the GUI)
    sys.exit(0)


class Final:
    def __init__(self):
        self.root = tk.Tk()
        self.root.configure(bg="BLACK")
        self.state = False

        self.top = tk.Frame(self.root, bg="BLACK")
        self.top.pack(side=tk.TOP, fill=tk.BOTH)
        self.bottom = tk.Frame(self.root, bg="BLACK")
        self.bottom.pack(side=tk.BOTTOM, fill=tk.BOTH)

        self.time = Clock(self.top)
        self.time.pack(side=tk.RIGHT, anchor=tk.N, pady=60)

        self.calendar = Calendar(self.bottom)
        self.calendar.pack(side = tk.RIGHT, anchor=tk.N, padx=0, pady=60)

        self.weather_show = Weather(self.top)
        self.weather_show.pack(side=tk.LEFT, anchor=tk.N, padx=50, pady=60)

        self.greeting = tk.Label(self.root, text="smartmirror by tomsoch & rysje", font="Arial 10", bg="BLACK", fg="WHITE")
        self.greeting.pack(side=tk.BOTTOM, pady=10)
        self.news = News(self.bottom)
        self.news.pack(side=tk.LEFT, anchor=tk.S, padx=100, pady=60)

        self.root.bind("<Return>", self.toggle_fullscreen)
        self.root.bind("<Escape>", close_application)
        self.root.attributes("-fullscreen", 1)
        self.root.mainloop()

    def toggle_fullscreen(self, event=None):
        self.state = not self.state
        self.root.attributes("-fullscreen", self.state)
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
    print("INFO: Starting smartmirror. Press <ESC> to close.")
    start = Final()
    start.root.mainloop()
