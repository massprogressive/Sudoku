from copy import deepcopy as dc
from functions import *


class Board:
    """
    Board is a class allows you set specified board, get
    information and manipulate board.
    """
    def __init__(self):
        """
        Creates board class with class with board
        fulfilled zeros.
        """
        self.numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.dimension = 3
        self.vertical_blocks = [0, 3, 6]
        self.horizontal_blocks = [0, 1, 2]
        self.diagonal_blocks = [0, 4, 8]
        self.board_block = [[[0 for x in range(self.dimension)]
                             for y in range(self.dimension)]
                            for z in range(self.dimension ** 2)]

        self.horizontal = None
        self.vertical = None

    def make_board(self):
        """
        Creates board fulfilled zeros.
        """
        add_board = [[[0 for x in range(self.dimension)]
                      for y in range(self.dimension)]
                     for z in range(self.dimension ** 2)]
        return add_board

    def set_board(self, board):
        """
        Set board attribute to board.
        :param board: new board
        """
        self.board_block = board

    def set_horizontal(self, lines):
        self.horizontal = lines

    def set_vertical(self, lines):
        self.vertical = lines

    def get_first_empty_block(self):
        for block in range(9):
            for y in range(3):
                for x in range(3):
                    if self.board_block[block][y][x] == 0:
                        return block

    def get_empty_blocks(self):
        result = []
        for block in range(9):
            for y in range(3):
                for x in range(3):
                    if self.board_block[block][y][x] == 0:
                        if block not in result:
                            result.append(block)
        return result

    def get_moves_quantity(self):
        """
        Computes the number of all available moves.
        :return: the number of all available moves
        """
        count = 0
        for block in self.board_block:
            for y in range(3):
                for x in range(3):
                    if block[x][y] == 0:
                        count += 1
        return count

    def get_moves_for_block(self, block_num):
        """
        Computes moves for specified block.
        :param block_num: block number.
        :return: list of moves (row, column)
        """
        moves = []
        for y in range(self.dimension):
            for x in range(self.dimension):
                if self.board_block[block_num][y][x] == 0:
                    moves.append((y, x))
        return moves

    def get_block_numbers(self, block_num):
        """
        Compute 'numbers not in block' for specified
        block.
        :param block_num: block number
        :return: list of 'numbers not in block'
        """
        numbers = dc(self.numbers)
        for y in range(self.dimension):
            for x in range(self.dimension):
                if self.board_block[block_num][y][x] in numbers:
                    numbers.pop(numbers.index(self.board_block[block_num][y][x]))
        return numbers

    def horizontal_lines(self):
        """
        Convert board in list of horizontal lines.
        """
        for row in range(1, self.dimension):
            one_of_three = []
            for y in range(self.dimension):
                lst = []
                for block in range(self.dimension):
                    for x in range(self.dimension):
                        lst.append(self.board_block[block][y][x])
                one_of_three.append(lst)
            for y in range(self.dimension):
                lst = []
                for block in range(self.dimension, self.dimension * 2):
                    for x in range(self.dimension):
                        lst.append(self.board_block[block][y][x])
                one_of_three.append(lst)
            for y in range(self.dimension):
                lst = []
                for block in range(self.dimension * 2, self.dimension ** 2):
                    for x in range(self.dimension):
                        lst.append(self.board_block[block][y][x])
                one_of_three.append(lst)
        self.horizontal = one_of_three

    def get_horizontal_line_numbers(self):
        """
        Compute list of 'numbers not in line' for each
        horizontal line on board.
        :return: list of lists 'numbers in line'
        """
        lines = []
        for line in self.horizontal:
            numbers = dc(self.numbers)
            for element in line:
                if element in numbers:
                    numbers.pop(numbers.index(element))
            lines.append(numbers)
        return lines

    def vertical_lines(self):
        """
        Convert board in lists of vertical lines.
        (Looks like transposed matrix 9x9)
        """
        one_of_three = []
        for x in range(self.dimension):
            lst = []
            for block in [0, 3, 6]:
                for y in range(self.dimension):
                    lst.append(self.board_block[block][y][x])
            one_of_three.append(lst)
        for x in range(self.dimension):
            lst = []
            for block in [1, 4, 7]:
                for y in range(self.dimension):
                    lst.append(self.board_block[block][y][x])
            one_of_three.append(lst)
        for x in range(self.dimension):
            lst = []
            for block in [2, 5, 8]:
                for y in range(self.dimension):
                    lst.append(self.board_block[block][y][x])
            one_of_three.append(lst)
        self.vertical = one_of_three

    def get_vertical_line_numbers(self):
        """
        Compute list of 'numbers not in line' for each
        vertical line on board.
        :return: list of lists 'numbers not in line'
        """
        lines = []
        for line in self.vertical:
            numbers = dc(self.numbers)
            for element in line:
                if element in numbers:
                    numbers.pop(numbers.index(element))
            lines.append(numbers)
        return lines

    def set_number(self, digit, block_num, position_y, position_x):
        """
        Draw the number in specified block, row and column.
        :param digit: digit to draw
        :param block_num: block number
        :param position_x: block column
        :param position_y: block row
        """
        self.board_block[block_num][position_y][position_x] = digit

    def delete_number(self, block_num, position_x, position_y):
        """
        Delete number in specified block, row and column.
        :param block_num: bock number
        :param position_y: row in block
        :param position_x: column in block
        """
        self.board_block[block_num][position_x][position_y] = 0

    def check_horizontal(self):
        """
        Checks all horizontal line on board.
        :return: True in ALL lines consists of
        digits from one to nine.
        """
        for line in self.horizontal:
            if len(set(delete_zeros(line))) != 9:
                return False
        return True

    def check_vertical(self):
        """
        Checks all vertical line on board.
        :return: True if ALL lines consists of
        digits from one to nine.
        """
        for line in self.vertical:
            if len(set(delete_zeros(line))) != 9:
                return False
        return True

    def check_line(self, line):
        """
        Check the number of digits in line
        :param line: list of digits
        :return: True in count of each element
        in list equals one, otherwise False
        """
        for number in self.numbers:
            if line.count(number) > 1:
                return False
        return True

    def check_block_vertical(self, block_num):
        for line in self.vertical[block_num % 3:block_num % 3 + 3]:
            if not (duplicates(line)):
                return False
        return True

    def check_block_horizontal(self, block_num):
        for line in self.horizontal[int(block_num / 3):int(block_num / 3) + 3]:
            if not (duplicates(line)):
                return False
        return True

    def check_all(self):
        return self.check_horizontal() and self.vertical_lines()

    def get_blocks_to_move(self):
        """
        Returns list of blocks with empty squeares
        """
        lst = []
        for block in range(9):
            if len(self.get_moves_for_block(block)) > 0:
                lst.append(block)
        return lst

    def update(self):
        self.horizontal_lines()
        self.vertical_lines()

    def clone(self):
        """
        Self cloning. Use copy.deepcopy function.
        :return: copy of self instance
        """
        return dc(self)

    def __str__(self):
        """
        Creates string representation of board.
        """
        to_print = ''
        for w in range(self.dimension):
            for h in range(self.dimension):
                to_print += str(self.board_block[h][w])
                if h < self.dimension - 1:
                    to_print += ' '
                else:
                    to_print += '\n'
        to_print += ('-' * 29 + '\n')
        for w in range(self.dimension):
            for h in range(self.dimension, 6):
                to_print += str(self.board_block[h][w])
                if h < self.dimension * 2 - 1:
                    to_print += ' '
                else:
                    to_print += '\n'
        to_print += ('-' * 29 + '\n')
        for w in range(self.dimension):
            for h in range(self.dimension * 2, self.dimension ** 2):
                to_print += str(self.board_block[h][w])
                if h < self.dimension ** 2 - 1:
                    to_print += ' '
                else:
                    to_print += '\n'
        return to_print

