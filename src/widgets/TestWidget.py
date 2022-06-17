import tkinter as tk


class TestWidget(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        # create frame with white background for easier debug
        tk.Frame.__init__(self, parent, bg="white", *args, **kwargs)
        self.example_text = "Example text"
        self.example_text_label = tk.Label(self, text=self.example_text, font=("Helvetica", 20), fg="white", bg="black")
        self.example_text_label.pack(side=tk.TOP, anchor=tk.E)
