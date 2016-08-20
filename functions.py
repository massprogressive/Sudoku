def duplicates(lst):
    """
    Function checks for duplicate in element.
    :param lst:
    :return:
    """
    for number in range(1, 10):
        if lst.count(number) > 1:
            return False
    return True


def delete_zeros(lst):
    _lst = []
    for element in lst:
        if element != 0:
            _lst.append(element)
    return _lst


# *********************************
# ANALYZING DRAFTS

def select_lines(lines, number):
    """
    Select lines with appropriate number
    :param lines: list of lines
    :param number: number for select
    :return: dictionary line_index: line
    """
    result = dict()
    for line in range(len(lines)):
        if number in lines[line]:
            result[line] = lines[line]
    return result


def detach_horizontal(lines, block_num):
    det_block, det_lines_1, det_lines_2 = [], [], []
    data_1, data_2, data_3 = [0, 1, 2], [3, 4, 5], [6, 7, 8]
    if block_num in data_1:
        other_blocks = [x for x in data_1 if x != block_num]
        for i in range(len(lines)):
            det_block.append(lines[i][data_1.index(block_num) % 3 * 3:data_1.index(block_num) % 3 * 3 + 3])
            det_lines_1.append(lines[i][data_1.index(other_blocks[0]) % 3*3:data_1.index(other_blocks[0]) % 3*3+3])
            det_lines_2.append(lines[i][data_1.index(other_blocks[1]) % 3*3:data_1.index(other_blocks[1]) % 3*3+3])
    elif block_num in data_2:
        other_blocks = [x for x in data_2 if x != block_num]
        for i in range(len(lines)):
            det_block.append(lines[i][data_2.index(block_num) % 3 * 3:data_2.index(block_num) % 3 * 3 + 3])
            det_lines_1.append(lines[i][data_2.index(other_blocks[0]) % 3*3:data_2.index(other_blocks[0]) % 3*3+3])
            det_lines_2.append(lines[i][data_2.index(other_blocks[1]) % 3*3:data_2.index(other_blocks[1]) % 3*3+3])
    elif block_num in data_3:
        other_blocks = [x for x in data_3 if x != block_num]
        for i in range(len(lines)):
            det_block.append(lines[i][data_3.index(block_num) % 3 * 3:data_3.index(block_num) % 3 * 3 + 3])
            det_lines_1.append(lines[i][data_3.index(other_blocks[0]) % 3*3:data_3.index(other_blocks[0]) % 3*3+3])
            det_lines_2.append(lines[i][data_3.index(other_blocks[1]) % 3*3:data_3.index(other_blocks[1]) % 3*3+3])
    return det_block, det_lines_1, det_lines_2


def detach_vertical(lines, block_num):
    det_block = []
    det_block_1 = []
    det_block_2 = []
    data_1 = [0, 3, 6]
    data_2 = [1, 4, 7]
    data_3 = [2, 5, 8]
    if block_num in data_1:
        other_blocks = [x for x in data_1 if x != block_num]
        for i in range(3):
            det_block.append(lines[i][data_1.index(block_num) % 3 * 3 : data_1.index(block_num) % 3 * 3 + 3])
            det_block_1.append(lines[i][data_1.index(other_blocks[0]) % 3 * 3 : data_1.index(other_blocks[0]) % 3 * 3 + 3])
            det_block_2.append(lines[i][data_1.index(other_blocks[1]) % 3 * 3 : data_1.index(other_blocks[1]) % 3 * 3 + 3])
    elif block_num in data_2:
        other_blocks = [x for x in data_2 if x != block_num]
        for i in range(3):
            det_block.append(lines[i][data_2.index(block_num) % 3 * 3 : data_2.index(block_num) % 3 * 3 + 3])
            det_block_1.append(lines[i][data_2.index(other_blocks[0]) % 3 * 3 : data_2.index(other_blocks[0]) % 3 * 3 + 3])
            det_block_2.append(lines[i][data_2.index(other_blocks[1]) % 3 * 3 : data_2.index(other_blocks[1]) % 3 * 3 + 3])
    elif block_num in data_3:
        other_blocks = [x for x in data_3 if x != block_num]
        for i in range(3):
            det_block.append(lines[i][data_3.index(block_num) % 3 * 3 : data_3.index(block_num) % 3 * 3 + 3])
            det_block_1.append(lines[i][data_3.index(other_blocks[0]) % 3 * 3 : data_3.index(other_blocks[0]) % 3 * 3 + 3])
            det_block_2.append(lines[i][data_3.index(other_blocks[1]) % 3 * 3 : data_3.index(other_blocks[1]) % 3 * 3 + 3])
    return det_block, det_block_1, det_block_2

# *********************************
# NINTH TEST


def last_digit_in_row(lines):
    possible_moves = []
    for line in lines:
        if len(delete_zeros(list(line))) == 8:
            number = list(range(1, 10))
            for element in delete_zeros(list(line)):
                if element in number:
                    number.pop(number.index(element))
            if len(number) == 1:
                number = number[0]
                y = lines.index(line)
                x = line.index(0)
                block = int(lines.index(line) / 3) * 3 + int(line.index(0) / 3)
                possible_moves.append((number, block, y % 3, x % 3))
    return possible_moves


def last_digit_in_column(lines):
    possible_moves = []
    for line in lines:
        if len(set(delete_zeros(line))) == 8:
            number = list(range(1, 10))
            for element in delete_zeros((list(line))):
                if element in number:
                    number.pop(number.index(element))
            if len(number) == 1:
                number = number[0]
                y = line.index(0)
                x = lines.index(line)
                block = int(x / 3) + int(y / 3) * 3
                possible_moves.append((number, block, y % 3, x % 3))
    return possible_moves


def ninth_test(inst):
    from_horizontal = last_digit_in_row(inst.horizontal)
    from_vertical = last_digit_in_column(inst.vertical)
    for move in from_horizontal + from_vertical:
        inst.set_number(move[0], move[1], move[2], move[3])
    inst.horizontal_lines()
    inst.vertical_lines()
    return inst


# *****************************************************
# LINES TEST (ONE DIGIT IN HORIZONTAL and VERTICAL LINE

def analyze_lines(lines):
    numbers = list(range(1, 10))
    line = lines[0] + lines[1]
    for element in line:
        if element in numbers:
            numbers.pop(numbers.index(element))
    return numbers


# *****************************************************
# COMMON MOVES TEST


def calculate_common(data):
    lst = []
    for new in data:
        lst += data[new]
    moves = sorted(set(lst))
    result = []
    for move in moves:
        count = 0
        for number in data:
            if move in data[number]:
                count += 1
            if count > 1:
                result.append(move)
                break
    return result


def calculate_moves(data, common, key):
    for move in common:
        for digit in data[key]:
            if move in data[key][digit]:
                data[key][digit].pop(data[key][digit].index(move))
    return data


def parse_moves(data, board_inst):
    for block in data:
        for digit in data[block]:
            if len(data[block][digit]) == 1:
                board_inst.set_number(digit, block, data[block][digit][0][0], data[block][digit][0][1])

# *****************************************************
# DOUBLES


def find_doubles(data):
    result = dict()
    for block in data.keys():
        block_data = data[block]
        for digit in block_data:
            digits = list(block_data.keys())
            digits.pop(digits.index(digit))
            for dig in digits:
                repeated = dict()
                if block_data[dig] == block_data[digit]:
                    repeated[(digit, dig)] = block_data[digit]
                    if len(list(repeated.keys())[0]) == len(list(repeated.values())[0]):
                        result[block] = repeated
    return result


# *****************************************************
# ANALYZING BOARD

def ninth_test(board_inst):
    """
    Finding lines with 8 digits.
    """
    from_horizontal = last_digit_in_row(board_inst.horizontal)
    from_vertical = last_digit_in_column(board_inst.vertical)
    for move in from_horizontal + from_vertical:
        board_inst.set_number(move[0], move[1], move[2], move[3])
    board_inst.horizontal_lines()
    board_inst.vertical_lines()
    return board_inst


def check_in_both_lines(board_inst):
    """
    Find out unique digit in horizontal-
    vertical cross.
    """
    start = board_inst.get_first_empty_block()
    if start is not None:
        for block in range(start, 9):
            moves = board_inst.get_moves_for_block(block)
            for move in moves:
                horizontal_line = board_inst.horizontal[block - (block % 3) + move[0]]
                vertical_line = board_inst.vertical[(block % 3) * 3 + move[1]]
                lines = [horizontal_line, vertical_line]
                number = analyze_lines(lines)
                if len(number) == 1:
                    board_inst.set_number(number[0], block, move[0], move[1])
    return board_inst


# *****************************************************


def print_drafts(inst):
    for draft in inst.drafts:
        print('Draft for number', inst.drafts.index(draft) + 1)
        print()
        print(draft)
        print('-' * 40)
        print()


def print_data(data):
    for block_num in data:
        print('Block', block_num)
        for line in data[block_num]:
            print(line, data[block_num][line])


def print_list(lst):
    for line in lst:
        print(line)

