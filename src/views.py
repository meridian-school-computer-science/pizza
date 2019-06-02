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
        super().__init__(baseName='Pizza App')
        #tk.Tk.__init__(self, *args, **kwargs)
        self.title('Pizza App')
        self.geometry('900x450+200+200')
        self.base_choice = tk.StringVar
        """ all of the widgets for our view
        """
        # frames
        self.left_frame = ttk.Frame(self)
        self.left_frame.grid(column=0, row=0, padx=20,sticky=tk.E+tk.W)
        self.right_frame = ttk.Frame(self)
        self.right_frame.grid(column=1, row=0, padx=20,sticky=tk.E+tk.W)

        self.tab_control = ttk.Notebook(self.left_frame)
        self.tab_control.pack(expand=1, fill="both")
        self.pizza_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.pizza_tab, text='Pizza')
        self.drink_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.drink_tab, text='Drinks')
        self.dessert_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.dessert_tab, text='Dessert')

        # add pizza_tab widgets here
        self._size = ttk.Checkbutton(self.pizza_tab, width=12, )

        self.base_pizza = ttk.Combobox(self.pizza_tab, width=12, textvariable=self.base_choice)
        self.base_pizza['values'] = ('Choose..', 'Cheese', 'Pepperoni', 'Sausage', 'Vegetarian', 'Combo')
        self.base_pizza.current(0)
        self.base_pizza.grid(column=0, row=1)



# class ToolTip(object):
#     def __init__(self, widget):
#         self.widget = widget
#         self.tipwindow = None
#         self.id = None
#         self.x = self.y = 0
#
#     def showtip(self, text):
#         "Display text in tooltip window"
#         self.text = text
#         if self.tipwindow or not self.text:
#             return
#         x, y, _cx, cy = self.widget.bbox("insert")
#         x = x + self.widget.winfo_rootx() + 27
#         y = y + cy + self.widget.winfo_rooty() +27
#         self.tipwindow = tw = tk.Toplevel(self.widget)
#         tw.wm_overrideredirect(1)
#         tw.wm_geometry("+%d+%d" % (x, y))
#
#         label = tk.Label(tw, text=self.text, justify=tk.LEFT,
#                          background="#ffffe0", relief=tk.SOLID, borderwidth=1,
#                          font=("tahoma", "8", "normal"))
#         label.pack(ipadx=1)
#
#     def hidetip(self):
#         tw = self.tipwindow
#         self.tipwindow = None
#         if tw:
#             tw.destroy()


if __name__ == '__main__':
    test = View()
    test.mainloop()
