import tkinter as tk
from tkinter import ttk
from src.constants_file import *
from tkinter import Menu
from tkinter import scrolledtext
from tkinter import Spinbox
from operator import attrgetter

# added comment to check connection

LARGE_FONT= ("Verdana", 12)


class View(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Container

        self.win = tk.Tk()
        self.win.title('Pizza App')
        self.win.geometry('700x450+200+200')
        self.base_choices = tk.StringVar
        self.create_frames()
        self.create_tabs()



    def create_frames(self):
        """ all of the widgets for our view
        """
        # frames
        self.container = ttk.Frame(self.win)
        self.container.grid(column=0, row=0)
        self.left_frame = ttk.Frame(self.container)
        self.left_frame.grid(column=0, row=0, padx=20,sticky=tk.E+tk.W)
        self.right_frame = ttk.Frame(self.container)
        self.right_frame.grid(column=1, row=0, padx=20,sticky=tk.E+tk.W)

    def create_tabs(self):
        self.tab_control = ttk.Notebook(self.left_frame)
        self.pizza_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.pizza_tab, text='Pizza')
        self.drink_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.drink_tab, text='Drinks')
        self.tab_control.pack(expand=1, fill="both")

    def build_pizza_tab(self):
        # add pizza_tab widgets here
        self.base_pizza = ttk.Combobox(self.pizza_tab, width=12, textvariable=self.base_choices)
        self.base_pizza['values'] = ('Cheese', 'Pepperoni')
        self.base_pizza.current(0)
        self.base_pizza.grid(column=0, row=0)

    def start_view(self):
        self.win.mainloop()


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


def main():
    test = View()
    test.start_view()

if __name__ == '__main__':
    main()
