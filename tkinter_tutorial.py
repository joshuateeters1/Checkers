from tkinter import *
from tkinter import ttk


def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass


root = Tk()
root.title("Feet to meters")

# create a main frame to put all other sub-frames
# add the frame to the main application window in a grid pattern
# configure the frame to fill any extra space if window is resized

# ttk.Frame(parent, padding="l, t, r, b")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# create the var to store feet
# create the widget itself
# put the widget on screen

# Entry sets parent, # chars width to appear (optional), global var to be used
#  in functions. Can be .get() and .set(), must be instance of StringVar class.
# sticky is optional to describe how to align within the specified grid cell
feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters) \
    .grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate) \
    .grid(column=3, row=3, sticky=E)

ttk.Label(mainframe, text="feet") \
    .grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to") \
    .grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters") \
    .grid(column=3, row=2, sticky=W)

# add padding to every child, focus on text entry, set enter = calculate
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
feet_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()
