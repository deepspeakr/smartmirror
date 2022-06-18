from tkinter import *
from time import *


class Clock(Frame):

    def __init__(self, master):
        Frame.__init__(self, master, background="BLACK")
        self.time1 = ""
        self.label_time = Label(self, font="dreams 40", bg="BLACK", fg="WHITE")
        self.label_time.pack(side=TOP, anchor="e")

        self.day1 = ""
        self.label_day = Label(self, font="dreams 28", bg="BLACK", fg="WHITE")
        self.label_day.pack(side=TOP, anchor="e")

        self.day_of_the_week1 = ""
        self.label_day_of_the_week = Label(self, font="dreams 28", bg="BLACK", fg="WHITE")
        self.label_day_of_the_week.pack(side=TOP, anchor="e")

        self.update_time()

    def update_time(self):
        time2 = strftime('%H:%M:%S')
        day2 = strftime("%B %d, %Y")
        day_of_the_week2 = strftime("%A")
        if self.time1 != time2:
            self.time1 = time2
            self.label_time.config(text=time2)
        if self.day1 != day2:
            self.day1 = day2
            self.label_day.config(text=day2)
        if self.day_of_the_week1 != day_of_the_week2:
            self.day_of_the_week1 = day_of_the_week2
            self.label_day_of_the_week.config(text=day_of_the_week2)
        self.after(200, self.update_time)
