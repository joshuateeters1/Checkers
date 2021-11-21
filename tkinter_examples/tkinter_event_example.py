from tkinter import *
from tkinter import ttk
root = Tk()
l =ttk.Label(root, text="Starting...")
l.grid()
l.bind('<Enter>', lambda e: l.configure(text='Moved mouse inside'))
l.bind('<Leave>', lambda e: l.configure(text='Moved mouse outside'))
l.bind('<ButtonPress-1>', lambda e: l.configure(text='Clicked left mouse button'))
l.bind('<3>', lambda e: l.configure(text='Clicked right mouse button')) # this is shorthand for "Button-Press-3"
l.bind('<Double-1>', lambda e: l.configure(text='Double clicked'))
l.bind('<B3-Motion>', lambda e: l.configure(text='right button drag to %d,%d' % (e.x, e.y)))
root.mainloop()

# lambda represents Python's anonymous functions for insta-defining simple actions.
#  you should almost always use real functions instead of these.

# to capture two keys pressed in a row, <KeyPress-A><KeyPress-B> or simply <ab>.  weird key names found here: https://tcl.tk/man/tcl8.6/TkCmd/keysyms.htm
# if you set up a binding for a toplevel window, it will trigger when a matching event occours anywhere in that window
# you can bind to e.g. all buttons

# Avaliable events:
# <Activate>        - window has become active
# <Deactivate>      - window has become deactivated
# <MouseWheel>      - scroll wheel on mouse has been moved
# <KeyPress>        - key on keyboard has been pressed down
# <KeyRelease>      - key has been released
# <ButtonPress>     - a mouse button has been pressed
# <ButtonRelease>   - a mouse button has been released
# <Motion>          - mouse has been moved
# <Configure>       - widget has changed size or position
# <Destroy>         - widget is being destroyed
# <FocusIn>         - widget has been given keyboard focus
# <FocusOut>        - widget has lost keboard focus
# <Enter>           - mouse pointer enters widget
# <Leave>           - mouse pointer leaves widget

# modifiers include Double, Triple, B1 or Button1 = mouse being held down, Control, Shift, Alt, Option, Command...


# virtual events are higher level events in angle brackets <<>>, avoids platform specific bindings
#  e.g. <<ListboxSelect>> is generated when a listbox widget item gets clicked
#  e.g. <<Cut>>, <<Copy>>, <<Paste>>
#  you can define your own e.g. root.event_generate("<<MyOwnEvent>>")



# example of binding <Return> globally to the button defined as default
action = ttk.Button(root, text="Action", default="active", command=myaction)
root.bind('<Return>', lambda e: action.invoke())
