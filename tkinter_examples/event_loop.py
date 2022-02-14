from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Checkers")

count = 0

def start():
    global count
    count = 0
    b.configure(text='Step', command=step)
    l['text'] = 'Working...'

def step():
    global count
    count = count + 1
    p['value'] = count
    if count == 20:  # done!
        result(42)
        return

def result(answer):
    p['value'] = 0
    b.configure(text='Start!', command=start)
    l['text'] = "Answer: " + str(answer) if answer else "No Answer"

f = ttk.Frame(root); f.grid()
b = ttk.Button(f, text="Start!", command=start); b.grid(column=1, row=0, padx=5, pady=5)
l = ttk.Label(f, text="No Answer"); l.grid(column=0, row=0, padx=5, pady=5)
p = ttk.Progressbar(f, orient="horizontal", mode="determinate", maximum=20);
p.grid(column=0, row=1, padx=5, pady=5)

root.mainloop()
