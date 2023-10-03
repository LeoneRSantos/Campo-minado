
from tkinter import *

class Frame1(Frame):
    def __init__(self, ws):
        Frame.__init__(self, ws, bg="#006699")
        self.ws = ws
        self.widgets()

    def widgets(self):
        self.grid(row=0, column=0, padx=20, pady=20) # margins


class Win(Tk):

    def __init__(self, ws):
        Tk.__init__(self, ws)
        self.ws = ws
        self.title('Campo Minado')
        self.geometry('500x500')
        self.main()

    def main(self):
        self.w = Frame1(self)
        self.w.pack()

if __name__== "__main__":
    app = Win(None)
    app.mainloop()