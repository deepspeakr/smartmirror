#!/usr/bin/env python
import tkinter as tk


class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.attributes("-fullscreen", 1)
        self.configure(background="black")


if __name__ == "__main__":
    main_window = MainWindow()
    main_window.mainloop()
