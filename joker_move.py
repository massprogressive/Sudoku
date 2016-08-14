from functions import *


def get_zero(lines):
    for y in range(9):
        for x in range(9):
            if lines[y][x] == 0:
                return y, x


def get_line_numbers(line, board, block):
    numbers_in_line = delete_zeros(line) + board.get_block_numbers(block)

    numbers_not_in_line = list(range(1, 10))
    for number in numbers_in_line:
        numbers_not_in_line.pop(numbers_not_in_line.index(number))
    return numbers_not_in_line


def joker_line(board):
    if board.get_moves_quantity() == 0:
        if board.check_horizontal() and board.check_vertical():
            print('This is a solution')
            print()
            print(board)
            return board
    else:
        move = get_zero(board.horizontal)
        position = (move[0] % 3, move[1] % 3)
        block = int(move[0] / 3) * 3 + int(move[1] / 3)
        numbers = board.get_block_numbers(block)

        for number in board.horizontal[move[0]]:
            if number in numbers:
                numbers.pop(numbers.index(number))

        for number in numbers:
            board.set_number(number, block, position[0], position[1])
            board.update()
            if board.check_block_vertical(block) and board.check_block_horizontal(block):
                joker_line(board)

        board.delete_number(block, position[0], position[1])
        board.update()

