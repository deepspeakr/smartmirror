import feedparser
import tkinter as tk
import traceback

from PIL import Image, ImageTk

import src.config.config as config


class NewsHeadline(tk.Frame):
    def __init__(self, parent, event_name=""):
        tk.Frame.__init__(self, parent, bg='black')

        image = Image.open("icons/Newspaper.png")
        image = image.resize((25, 25), Image.ANTIALIAS)
        image = image.convert("RGB")
        photo = ImageTk.PhotoImage(image)

        self.iconLbl = tk.Label(self, bg="black", image=photo)
        self.iconLbl.image = photo
        self.iconLbl.pack(side=tk.LEFT, anchor=tk.N)

        self.eventName = event_name
        self.eventNameLbl = tk.Label(
            self, text=self.eventName,
            font=("Helvetica", config.SMALL_TEXT_SIZE),
            fg="white",
            bg="black"
        )
        self.eventNameLbl.pack(side=tk.LEFT, anchor=tk.N)


class News(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.config(bg="black")
        self.title = "News"
        self.newsLbl = tk.Label(
            self,
            text=self.title,
            font=("Helvetica", config.MEDIUM_TEXT_SIZE),
            fg="white",
            bg="black"
        )
        self.newsLbl.pack(side=tk.TOP, anchor=tk.W)
        self.headlinesContainer = tk.Frame(self, bg="black")
        self.headlinesContainer.pack(side=tk.TOP)
        self.get_headlines()

    def get_headlines(self):
        try:
            # remove all children
            for widget in self.headlinesContainer.winfo_children():
                widget.destroy()
            if config.DEBUG:
                print(f"INFO: Using following news url: {config.NEWS_URL}")

            feed = feedparser.parse(config.NEWS_URL)

            for post in feed.entries[0:5]:
                headline = NewsHeadline(self.headlinesContainer, post.title)
                headline.pack(side=tk.TOP, anchor=tk.W)
        except Exception as e:
            traceback.print_exc()
            print("Error: %s. Cannot get news." % e)

        self.after(600000, self.get_headlines)
