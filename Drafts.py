from Board import *


class Draft(Board):
    """
    Data object which makes and and manipulate
    drafts: make, edit and save tool.
    """
    def __init__(self):
        Board.__init__(self)

    def not_empty(self):
        """
        Check draft for possible moves
        """
        for block in self.board_block:
            for y in range(3):
                for x in range(3):
                    if block[y][x] != 0:
                        return True
        return False

    def get_moves_for_block(self, block_num):
        """
        Get moves for block in draft.
        :param block_num: block number
        """
        result = []
        for y in range(3):
            for x in range(3):
                if self.board_block[block_num][y][x] != 0:
                    result.append((y, x))
        return result


class Drafts:
    def __init__(self, inst, cls=Draft):
        self.drafts = []
        self.inst = inst
        self.data = {}
        self.cls = cls

    def make_draft(self):
        """
        Makes drafts for all digits on board
        """
        for number in range(1, 10):
            draft = self.cls()
            for block in range(9):
                moves = self.inst.get_moves_for_block(block)
                numbers = self.inst.get_block_numbers(block)
                if number in numbers:
                    for move in moves:
                        clone = self.inst.clone()
                        clone.set_number(number, block, move[0], move[1])
                        clone.update()
                        v_l = clone.horizontal[block - (block % 3) + move[0]]
                        h_l = clone.vertical[block % 3 * 3 + move[1]]
                        if clone.check_line(h_l) and clone.check_line(v_l):
                            draft.set_number(number, block, move[0], move[1])
            self.drafts.append(draft)

    def drafts_data(self):
        """
        Represent drafts data dictionary like
        """
        for block_num in range(9):
            block = dict()
            for draft in self.drafts:
                if draft.not_empty():
                    moves = draft.get_moves_for_block(block_num)
                    if len(moves) > 0:
                        block.update({self.drafts.index(draft)+1: moves})
            self.data[block_num] = block

    def horizontal_analyze_by_line(self):
        """
        Analyzing drafts for horizontal intersections
        """
        for draft in self.drafts:
            number = self.drafts.index(draft) + 1
            for block in range(9):
                clone = draft.clone()
                clone.horizontal_lines()
                if block in [0, 1, 2]:
                    lines = clone.horizontal[0:3]
                elif block in [3, 4, 5]:
                    lines = clone.horizontal[3:6]
                elif block in [6, 7, 8]:
                    lines = clone.horizontal[6:9]
                det_block, block_1, block_2 = detach_horizontal(lines, block)
                for comp_block in [block_1, block_2]:
                    sel_lines = select_lines(comp_block, number)
                    if len(sel_lines) == 1:
                        for x in range(3):
                            draft.delete_number(block, list(sel_lines.keys())[0], x)
                    elif len(sel_lines) == 2:
                        pass

    def vertical_analyze_draft_by_line(self):
        """
        Analyzing drafts for vertical intersections
        """
        for draft in self.drafts:
            number = self.drafts.index(draft) + 1
            for block in range(9):
                clone = draft.clone()
                clone.vertical_lines()
                lines = clone.vertical[(block % 3)*3:(block % 3)*3+3]
                det_block, block_1, block_2 = detach_vertical(lines, block)
                for comp_block in [block_1, block_2]:
                    sel_lines = select_lines(comp_block, number)
                    if len(sel_lines) == 1:
                        for y in range(3):
                            draft.delete_number(block, y, list(sel_lines.keys())[0])
                    elif len(sel_lines) == 2:
                        pass

    def doubles(self):
        """
        Finding 'naked doubles'
        """
        doubles = find_doubles(self.data)
        for block in doubles:
            for digits in doubles[block]:
                drafts_idx = list(range(9))
                for dig in digits:
                    drafts_idx.pop(drafts_idx.index(dig-1))
                for idx in drafts_idx:
                    self.drafts[idx].delete_number(block, doubles[block][digits][0][0], doubles[block][digits][0][1])
                    self.drafts[idx].delete_number(block, doubles[block][digits][1][0], doubles[block][digits][1][1])

    def common(self):
        """
        Finding common moves
        """
        for key in self.data:
            current_data = self.data[key]
            common = calculate_common(current_data)
            result = calculate_moves(self.data, common, key)
            parse_moves(result, self.inst)
