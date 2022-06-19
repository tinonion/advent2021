import dataclasses
import functools
from io import TextIOWrapper
import re


@dataclasses.dataclass
class BoardNum:
    marked: bool
    val: int


class Board:
    width = 5
    height = 5

    def __init__(self, nums: list[int]):
        if len(nums) != self.width * self.height:
            raise ValueError(
                f"must supply {self.width * self.height} nums to fill board, got {len(nums)} {nums=}"
            )

        self.flat_mat = [BoardNum(False, num) for num in nums]
        self.has_won = False

    def __repr__(self) -> str:
        s = ""

        for i, board_num in enumerate(self.flat_mat):
            if i > 0 and i % self.width == 0:
                s += "\n"

            s += f"({board_num.val:>3}, {'x' if board_num.marked else 'o'})"

        return s

    def col_from_ind(self, ind: int) -> int:
        return ind % self.width

    def row_from_ind(self, ind: int) -> int:
        return ind // self.width

    def mark_num(self, num: int) -> bool:
        # return true if board has reached win condition
        for i, board_num in enumerate(self.flat_mat):
            if board_num.val == num:
                board_num.marked = True
                self.flat_mat[i] = board_num

                if self.is_winning_col(self.col_from_ind(i)) or self.is_winning_row(
                    self.row_from_ind(i)
                ):
                    self.has_won = True
                    return True

        return False

    def is_winning_row(self, row_ind: int) -> bool:
        start = self.height * row_ind
        return all(
            [
                board_num.marked
                for board_num in self.flat_mat[start : start + self.width]
            ]
        )

    def is_winning_col(self, col_ind: int) -> bool:
        start = col_ind
        return all(
            [board_num.marked for board_num in self.flat_mat[start :: self.width]]
        )

    def get_unmarked_sum(self) -> int:
        s = 0
        for board_num in self.flat_mat:
            if not board_num.marked:
                s += board_num.val

        return s


def parse_input(input_path: str) -> tuple[list[int], list[Board]]:
    def read_chunk(fp: TextIOWrapper) -> tuple[bool, list[str]]:
        chunk = []
        curr_line = fp.readline()
        while curr_line:
            chunk.append(curr_line)
            curr_line = fp.readline()

            if curr_line == "\n":
                return False, chunk

        return True, chunk

    chunks = []
    with open(input_path, "r") as fp:
        at_end = False
        while not at_end:
            at_end, new_chunk = read_chunk(fp)
            chunks.append(new_chunk)

    # flatten the chunk lists
    chunks = [functools.reduce(lambda x, y: x + y, chunk, "") for chunk in chunks]

    draw_numbers = [int(n) for n in chunks[0].split(",")]

    board_nums = [re.split(r"\s+", nums.strip()) for nums in chunks[1:]]
    boards = [Board([int(n) for n in nums]) for nums in board_nums]

    return draw_numbers, boards


def part_one(input_path: str) -> int:
    draw_numbers, boards = parse_input(input_path)

    for n in draw_numbers:
        for board in boards:
            won = board.mark_num(n)

            if won:
                unmarked_sum = board.get_unmarked_sum()

                return unmarked_sum * n


def part_two(input_path: str) -> int:
    draw_numbers, boards = parse_input(input_path)

    boards_won = 0
    for n in draw_numbers:
        for board in boards:
            if board.has_won:
                continue

            won = board.mark_num(n)

            if won:
                if boards_won == len(boards) - 1:
                    unmarked_sum = board.get_unmarked_sum()

                    return unmarked_sum * n

                boards_won += 1
            