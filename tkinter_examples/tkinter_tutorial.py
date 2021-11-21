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


# example button
# button = ttk.Button(root, text="Hello", command="buttonpressed")

# get the 'text' option value
# print(button['text'])

# set the 'text' option value
# button.configure(text='goodbye')

# get all information on the 'text' option
# returns ('text', 'text', 'Text', '', 'goodbye')
#  first is the options name, fourth is default value, fifth is current value.
# print(button.configure('text'))

# get all information on all options for this widget
# print(button.configure())


# use winfo to get more info about a widget (pass in widget w)
def print_hierarchy(w, depth=0):
    print('  '*depth + w.winfo_class() + ' w=' + str(w.winfo_width()) + ' h=' + str(w.winfo_height()) + ' x=' + str(w.winfo_x()) + ' y=' + str(w.winfo_y()))
    for i in w.winfo_children():
        print_hierarchy(i, depth+1)
# useful: winfo_...
#  class, children/parent, toplevel, width/height, reqwidth/reqheight,
#  x/y, rootx/rooty, viewable




# widget examples
#  frame
#    displays a simple rectangle
#    frame = ttk.Frame(parent)
#      requested size, padding, borders, styles
#  label
#    displays text of images, typically not for interaction
#    label = ttk.Label(parent, {text='hello' || textvariable = var})
#      text, textvariable, image, compound, style (preferred), font, foreground, background, relief, anchor, justify
#  button
#    normal rectangle button
#    button = ttk.Button(parent, text='hello', command=functionName)
#      style, text, textvariable, image, compound, default, command
#      state, instate
#  checkbutton
#    toggleable button, like a checkbox.  when clicked, checks button and invokes callback.
#    textToChange = StringVar(value=0)  #this defaults the checkbox to "off"
#    check = ttk.Checkbutton(parent, text='On or Off?', command=callbackFunctionName, variable=textToChange, onvalue='checked!', offvalue='unchecked!')
#      text, textvariable, image, compound, command, variable, onvalue, offvalue
#      invoke, state, instate
#  radiobutton
#    toggleable options, can only choose one option at a time
#    choice = StringVar()
#    choice1 = ttk.Radiobutton(parent, text='Choice 1', variable=choice, value='choice1')
#    choice2 = ttk.Radiobutton(parent, text='Choice 2', variable=choice, value='choice2')
#    choice3 = ttk.Radiobutton(parent, text='Choice 3', variable=choice, value='choice3')
#      text, textvariable, image, compound, command, variable, value
#      state, instate
#  entry
#    single-line text field, able to be typed in
#    username = StringVar()
#    name = ttk.Entry(parent, textvariable=username)
#      textvariable, width, validate, validatecommand
#      get, set, delete, insert, StringVar().trace_add, state, instate
#  combobox
#    entry with a list of choices, a dropdown.  Can also type in own value in uncommon cases.
#    countryvar = StringVar()
#    country = ttk.Combobox(parent, textvariable=countryvar)
#    country.bind('<<ComboboxSelected>>', function)
#      textvariable, values
#      state, instate, get, set, current


# configuration options
#  requested size: x[width] = 350; x[height] = 350m/350c/350m/350i/350p
#  padding: x['padding'] = (left, top, right, bottom)
#  borders: x['borderwidth'] = 2; x['releif'] = {'flat', 'raised', 'sunken', 'solid', 'ridge', 'groove'}
#  styles: you can define styles that combine a bunch of options into one
#    s = ttk.Style()
#    s.configure('Danger.TFrame', background='red', borderwidth=5, relief='raised')
#    x(root, width=200, style='Danger.TFrame').grid()
#  text: x[text] = 'hello'
#  textvariable: var = StringVar(); x['textvariable'] = var; var.set('new value')  (var.get() gets value)
#  image: image = PhotoImage(file='myimage.gif'); x['image'] = image
#  compound: x[compound] = {none, text (text only), image (image only), center (text in center of image), top (image above text), left, bottom, right}
#  font: x['font'] = {"TkDefaultFont", "TkTextFont", "TkFixedFont" (fixed-width), "TkMenuFont", "TkHeadingFont", "TkCaptionFont", "TkSmallCaptionFont", etc}
#  foreground: x['foreground'] = "red" || "#ff340a"
#  background: x['background'] = "red" || "#ff340a"
#  anchor: x['anchor'] = {"n", "ne", "e", "se", "s", "sw", "w", "nw", "center"}
#  justify: x['justify'] = {"left", "center", "right"}
#  default: x['default'] = {"active", "normal"}  #specifies if button should be pressed when "enter" is hit, draws border, still need event handler for enter
#  command: x['command'] = nameOfFunction  (no ""s)
#  variable: x['variable'] = referenceToStringVar  #links to a widget's current value, updated when widget is toggled
#  onvlue: x['onvalue'] = "customOnValue"  #sets a custom value to set ['variable'] to instead of the default 1 when toggled on
#  offvlue: x['onvalue'] = "customOffValue"  #sets a custom value to set ['variable'] to instead of the default 0 when toggled off
#  value: x['value'] = "option1"  #sets the value to set the 'variable' var to when selected
#  validate: x['validate'] = *see validation for more info*
#  validatecommand: x['validatecommand'] = *see validation for more info*
#  values: x['values'] = ('USA', 'Canada', 'Australia')

# functions
#  state: x.state(['disabled']) #sets state flag to true; x.state(['!disabled']) #sets disabled to false
#   list of states: 'active', 'disabled', 'focus', 'pressed', 'selected', 'background'. 'readonly', 'alternate', 'invalid'
#  instate: x.instate(['disabled']) #check if disabled is ture; x.instate(['!disabled'], cmd) #execute 'cmd' if not disabled
#  invoke: x.invoke() #will call the command specified by ['command']
#  get: x.get() #gets the value of the widget
#  set: x.set('hello') #sets the value of the widget
#  current: x.current() #returns an index of currently selected item
#  delete: x.delete(0, 'end') #deletes value between two indices
#  insert: x.insert(0, 'your name') #insert new text at a gicen index
#  trace_add: StringVar().trace_add("write", functionToCallWhenWritten)  #see trace_remove and trace_info
