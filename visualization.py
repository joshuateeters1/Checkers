from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Visual:

    def __init__(self):
        root = Tk()
        root.title("Checkers")

        self.mainframe = ttk.Frame(root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        style = ttk.Style()
        style.configure('Tan.TLabel', background='tan')
        style.configure('Green.TLabel', background='green')

        b_piece_file = Image.open('checkers_pieces/b_piece.png')
        r_piece_file = Image.open('checkers_pieces/r_piece.png')
        b_king_file = Image.open('checkers_pieces/b_king.png')
        r_king_file = Image.open('checkers_pieces/r_king.png')
        self.b_piece = ImageTk.PhotoImage(b_piece_file.resize((100,100),Image.ANTIALIAS))
        self.r_piece = ImageTk.PhotoImage(r_piece_file.resize((100,100),Image.ANTIALIAS))
        self.b_king = ImageTk.PhotoImage(b_king_file.resize((100,100),Image.ANTIALIAS))
        self.r_king = ImageTk.PhotoImage(r_king_file.resize((100,100),Image.ANTIALIAS))

        root.mainloop()

    def updateVisual(self, board):
        for r in range(8):
            for c in range(8):
                s = 'Tan.TLabel' if ((r * 7) + c) % 2 == 0 else 'Green.TLabel'
                #match piece:
                    #case
                button = ttk.Button(self.mainframe, image=self.b_king, style=s).grid(row=r, column=c)
