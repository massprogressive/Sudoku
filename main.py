# EVERY TIME YOU ARE TRYING TO SOLVE SUDOKU PUZLE
# YOU NEED INITIALIZE BOARD CLASS INSTANCE AND USE
# set_board METHOD TO SET SPECIFIED BOARD TO SOLVE.

from Drafts import *
from BOARDS import *
from joker_move import joker_line as jl
from move import *


board = Board()
board.set_board(BOARD_15)
board.update()
print(board)
while board.get_first_empty_block() is not None:
    true = move(board)
    if not true:
        break
    print('Moves left ', board.get_moves_quantity())
if board.get_moves_quantity():
    print()
    print('Backtracking... it takes time a lot...')
    print()
    jl(board)
else:
    print()
    print('This is a solution')
    print()
    print(board)
