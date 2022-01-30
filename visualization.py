from tkinter import *
from tkinter import ttk


class visual:
    root = Tk()
    root.title("Checkers")

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    style = ttk.Style()
    style.configure('T.TLabel', background='tan')
    style.configure('G.TLabel', background='green')

    image = PhotoImage(file='checkers_pieces/b_piece.png')

    for r in range(8):
        for c in range(8):
            s = 'T.TLabel' if ((r * 7) + c) % 2 == 0 else 'G.TLabel'
            button = ttk.Button(mainframe, text='     ', style=s).grid(row=r, column=c)


    root.mainloop()
