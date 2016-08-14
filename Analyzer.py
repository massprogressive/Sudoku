from Drafts import *


class Analyzer(Board):

    @staticmethod
    def ninth_test(board):
        """
        Finding lines with 8 digits.
        """
        from_horizontal = last_digit_in_row(board.horizontal)
        from_vertical = last_digit_in_column(board.vertical)
        for move in from_horizontal + from_vertical:
            board.set_number(move[0], move[1], move[2], move[3])
        board.horizontal_lines()
        board.vertical_lines()
        return board

    @staticmethod
    def check_in_both_lines(board):
        """
        Find out unique digit in horizontal-
        vertical cross.
        """
        start = board.get_first_empty_block()
        if start is not None:
            for block in range(start, 9):
                moves = board.get_moves_for_block(block)
                for move in moves:
                    horizontal_line = board.horizontal[block - (block % 3) + move[0]]
                    vertical_line = board.vertical[(block % 3) * 3 + move[1]]
                    lines = [horizontal_line, vertical_line]
                    number = analyze_lines(lines)
                    if len(number) == 1:
                        board.set_number(number[0], block, move[0], move[1])
        return board

analyzer = Analyzer()
