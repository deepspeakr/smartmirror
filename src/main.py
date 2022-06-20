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


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.configure(bg="BLACK")
        self.state = False

        self.top = tk.Frame(self.root, bg="BLACK")
        self.top.pack(side=tk.TOP, fill=tk.BOTH)
        self.bottom = tk.Frame(self.root, bg="BLACK")
        self.bottom.pack(side=tk.BOTTOM, fill=tk.BOTH)

        self.time = Clock(self.top)
        self.time.pack(side=tk.RIGHT, anchor=tk.N, padx=40, pady=50)

        self.calendar = Calendar(self.bottom)
        self.calendar.pack(side = tk.RIGHT, anchor=tk.N, padx=40, pady=50)

        self.weather_show = Weather(self.top)
        self.weather_show.pack(side=tk.LEFT, anchor=tk.N, padx=40, pady=50)

        self.greeting = tk.Label(self.root, text="smartmirror by tomsoch & rysje", font="Arial 8", bg="BLACK", fg="WHITE")
        self.greeting.pack(side=tk.BOTTOM, pady=10)
        self.news = News(self.bottom)
        self.news.pack(side=tk.LEFT, anchor=tk.S, padx=40, pady=50)

        self.root.bind("<Return>", self.toggle_fullscreen)
        self.root.bind("<Escape>", close_application)
        self.root.attributes("-fullscreen", 1)
        self.root.mainloop()

    def toggle_fullscreen(self, event=None):
        self.state = not self.state
        self.root.attributes("-fullscreen", self.state)
        return "break"


if __name__ == "__main__":
    print("INFO: Starting smartmirror. Press <ESC> to close.")
    main_window = MainWindow()
    main_window.root.mainloop()
