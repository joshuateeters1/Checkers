from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class visual:
    root = Tk()
    root.title("Checkers")

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    style = ttk.Style()
    style.configure('Tan.TLabel', background='tan')
    style.configure('Green.TLabel', background='green')

    b_piece_file = Image.open('checkers_pieces/b_piece.png')
    b_piece = ImageTk.PhotoImage(b_piece_file.resize((100,100),Image.ANTIALIAS))
    r_piece_file = Image.open('checkers_pieces/r_piece.png')
    r_piece = ImageTk.PhotoImage(r_piece_file.resize((100,100),Image.ANTIALIAS))
    b_king_file = Image.open('checkers_pieces/b_king.png')
    b_king = ImageTk.PhotoImage(b_king_file.resize((100,100),Image.ANTIALIAS))
    r_king_file = Image.open('checkers_pieces/r_king.png')
    r_king = ImageTk.PhotoImage(r_king_file.resize((100,100),Image.ANTIALIAS))

    for r in range(8):
        for c in range(8):
            s = 'Tan.TLabel' if ((r * 7) + c) % 2 == 0 else 'Green.TLabel'
            button = ttk.Button(mainframe, image=b_piece, style=s).grid(row=r, column=c)


    root.mainloop()
