import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import scrolledtext
from tkinter import Spinbox
from operator import attrgetter


LARGE_FONT= ("Verdana", 12)


class View(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Container

        self.win = tk.Tk()
        self.win.title('Pizza App')
        self.win.geometry('700x450+200+200')
        self.create_widgets()

    def create_widgets(self):
        """ all of the widgets for our view
        """
        # frames
        self.container = ttk.Frame(self)
        self.container.grid(column=0, row=0)
        self.left_frame = ttk.Frame(self.container)
        self.left_frame.grid(column=0, row=0, padx=20,sticky=tk.E+tk.W)
        self.right_frame = ttk.Frame(self.container)
        self.right_frame.grid(column=1, row=0, padx=20,sticky=tk.E+tk.W)




    def start_view(self):
        self.win.mainloop()


class aTabControl(ttk.Notebook):

    def __init__(self, parent, display_text):
        ttk.Notebook.__init__(self, *args, **kwargs)
        self.tab_control = ttk.Notebook(parent)
        self.tab_frame = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_frame, text=display_text)
        self.tab_control.grid(column=0, row=0)


class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, _cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 27
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))

        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                      background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()


