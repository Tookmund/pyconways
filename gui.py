#!/usr/bin/python3
from conway import Conway
import tkinter as tk

#https://stackoverflow.com/a/4785224
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Conway's Game of Life")
        self.canvas = tk.Canvas(self,width=500,height=500)
        self.canvas.pack(side="top",fill="both",expand=True)
        self.rows = 100
        self.columns = 100
        self.size = 10
        self.rect = {}
        for r in range(self.rows):
            for c in range(self.columns):
                x1 = c*self.size
                y1 = r*self.size
                x2 = x1+self.size
                y2 = y1+self.size
                self.rect[r,c] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="white")
                
        self.con = Conway(self.rows,self.columns)
        self.con.populate()
        self.redraw(10)
        
    def redraw(self,delay):
        self.con.generation()
        for r in range(self.rows):
            for c in range(self.columns):
                if self.con.board[r][c] == '.':
                    self.canvas.itemconfig(self.rect[r,c],fill="black")
                else:
                    self.canvas.itemconfig(self.rect[r,c],fill="white")
        self.after(delay,lambda: self.redraw(delay))

if __name__ == "__main__":
    app = App()
    app.mainloop()
