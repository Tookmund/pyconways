#!/usr/bin/python3
# Conway's Game of Life in Python

import os, random, time

# https://stackoverflow.com/a/943921
# Get number of rows and columns in terminal
try:
    rows, columns = os.popen('stty size', 'r').read().split()
    rows, columns = int(rows), int(columns)
except:
    rows, columns = 80,40
# https://stackoverflow.com/a/2397150
# Set board to correct size
board = [[' ' for y in range(columns)] for x in range(rows)]

random.seed()

def show():
    for y in board:
        for x in y:
            print(x,end='')
        print()

def populate():
    for row in range(rows):
        for col in range(columns):
            if random.random() > 0.5:
                board[row][col] = '.'

def neighbors(b,row,col):
    # get neighbors
    total = 0
    for r in [row-1,row,row+1]:
        if r == -1 or r == rows:
            continue
        for c in [col-1,col,col+1]:
            if c == -1 or c == columns:
                continue
            if r == row and c == col:
                continue
            if b[r][c] == '.':
                total += 1
    return total

def living(b,row,col):
    n = neighbors(b,row,col)
    if (b[row][col] == '.'):
        if n == 2 or n == 3:
            pass
        else:
            board[row][col] = ' '
    else:
        if n == 3:
            board[row][col] = '.'

#Begin
populate()
show()
while 1:
    b = [r[:] for r in board]
    for row in range(rows):
        for col in range(columns):
            living(b,row,col)
    show()
    #time.sleep(1)

