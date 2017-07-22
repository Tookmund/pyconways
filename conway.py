#!/usr/bin/python3
# Conway's Game of Life in Python

import os, random, time

class Conway:
    def __init__(self, rows, columns, show, wraparound):
        self.rows = rows
        self.columns = columns
        self.show = show
        self.wraparound = wraparound
        # https://stackoverflow.com/a/2397150
        # Set board to correct size
        self.board = [[' ' for y in range(columns)] for x in range(rows)]
        random.seed()

    def populate(self):
        for row in range(self.rows):
            for col in range(self.columns):
                if random.random() > 0.9:
                    self.board[row][col] = '.'

    def neighbors(self, b, row, col):
        # get neighbors
        total = 0
        ra = [row-1,row,row+1]
        ca = [col-1,col,col+1]
        if self.wraparound:
            if ra[0] == -1:
                ra[0] = self.rows-1
            elif ra[2] == self.rows:
                ra[2] = 0
            if ca[0] == -1:
                ca[0] = self.columns-1
            elif ca[2] == self.columns:
                ca[2] = 0
        for r in ra:
            if r == -1 or r == self.rows:
                continue
            for c in ca:
                if c == -1 or c == self.columns:
                    continue
                if r == row and c == col:
                    continue
                if b[r][c] == '.':
                    total += 1
        return total

    def living(self, b, row, col):
        n = self.neighbors(b,row,col)
        if (b[row][col] == '.'):
            if n == 2 or n == 3:
                pass
            else:
                self.board[row][col] = ' '
        else:
            if n == 3:
                self.board[row][col] = '.'

    def run(self):
        while 1:
            b = [r[:] for r in self.board]
            for row in range(self.rows):
                for col in range(self.columns):
                    self.living(b,row,col)
            self.show(self.board)

if __name__ == "__main__":
    def show(board):
        for y in board:
            for x in y:
                print(x,end='')
            print()
    # https://stackoverflow.com/a/943921
    # Get number of rows and columns in terminal
    try:
        rows, columns = os.popen('stty size', 'r').read().split()
        rows, columns = int(rows), int(columns)
    except:
        rows, columns = 80,40
    con = Conway(rows,columns,show,True)
    con.populate()
    con.run()


