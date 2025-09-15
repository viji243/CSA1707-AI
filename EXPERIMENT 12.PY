import math
import random

EMPTY = " "
HUMAN = "X"
AI = "O"

def print_board(b):
    print("\n".join(["|".join(b[i:i+3]) for i in range(0,9,3)]))
    print()

def winner(b):
    lines = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b1,c in lines:
        if b[a] == b[b1] == b[c] != EMPTY:
            return b[a]
    return None

def available_moves(b):
    return [i for i,v in enumerate(b) if v==EMPTY]

def is_terminal(b):
    return winner(b) or not available_moves(b)
