ai_search_examples.py

Many compact problem implementations:
- 8-puzzle (A* with Manhattan)
- Eight queens (backtracking)
- Water jug (BFS)
- Cryptarithmetic (send+more=money style backtracking)
- Missionaries & Cannibals (BFS)
- Vacuum-cleaner simple-state search (reflex + BFS as example)
- Generic BFS and DFS examples
- Traveling Salesman (brute-force exact for small n)
- Generic A* example (used in 8-puzzle)
- Map coloring (backtracking)
- Tic-Tac-Toe with Minimax and alpha-beta pruning
- Decision tree vs simple neural net training (sklearn & keras-like via sklearn MLP)
"""

from collections import deque, namedtuple
import heapq
import itertools
import math
import random
