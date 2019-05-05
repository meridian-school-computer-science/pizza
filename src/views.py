import tkinter as tk
from tkinter import ttk


LARGE_FONT= ("Verdana", 12)


class ExApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # frames

        self.frames = {}
        for each_frame in (StartPage, PageOne, PageTwo):
            frame = each_frame(container, self)
            self.frames[each_frame] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # show frame of the start page
        self.show_frame(StartPage)

    def show_frame(self, a_container):
        frame = self.frames[a_container]
        frame.tkraise()


def qf(quick_print):
    print(quick_print)


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Visit Page 1",
                           command=lambda: controller.show_frame(PageOne))
        button1.pack()

        button2 = ttk.Button(self, text="Go to Page One",
                           command=lambda: controller.show_frame(PageOne))
        button2.pack()

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page One", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Back to Start",
                           command=lambda: controller.show_frame(StartPage))
        button.pack()
        button2 = ttk.Button(self, text="Go to Page Two",
                           command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Start",
                           command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Go to Page One",
                           command=lambda: controller.show_frame(PageOne))
        button2.pack()


root = ExApp()

root.mainloop()
