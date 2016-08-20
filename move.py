from Analyzer import analyzer
from Drafts import Drafts
from functions import *


def move(board):
    moves1 = board.get_moves_quantity()
    drafts = Drafts(board)
    drafts.make_draft()
    drafts.horizontal_analyze_by_line()
    drafts.vertical_analyze_draft_by_line()
    drafts.drafts_data()
    drafts.doubles()
    drafts.common()
    drafts.drafts_data()
    for draft in drafts.drafts:
        number = drafts.drafts.index(draft) + 1
        for block_num in range(9):
            moves = draft.get_moves_for_block(block_num)
            if len(moves) == 1:
                board.set_number(number, block_num, moves[0][0], moves[0][1])
    board.update()
    ninth_test(board)
    check_in_both_lines(board)
    moves2 = board.get_moves_quantity()
    if moves1 == moves2:
        return False
    return True



