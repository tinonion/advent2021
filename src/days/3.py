from copy import copy


def parse_input(input_path: str) -> tuple[int, list[int]]:
    digit_count = None
    nums = []
    with open(input_path, "r") as fp:
        lines = [line for line in fp]
        digit_count = len(lines[0]) - 1
        nums = [int(num, 2) for num in lines]

    return digit_count, nums


def part_one(input_path: str) -> int:
    digit_count, nums = parse_input(input_path)

    gamma_rate = 0
    epsilon_rate = 0

    for col in range(digit_count):
        total_ones = 0
        for i, num in enumerate(nums):
            if num & 1:
                total_ones += 1

            nums[i] >>= 1

        if total_ones > len(nums) / 2:
            gamma_rate += pow(2, col)

        else:
            epsilon_rate += pow(2, col)

    return gamma_rate * epsilon_rate


def prune_nums(nums: list[int], col: int, desired_bit: int) -> list[int]:
    pruned_nums = []
    for num in nums:
        if num & pow(2, col) and desired_bit:
            pruned_nums.append(num)

        elif not num & pow(2, col) and not desired_bit:
            pruned_nums.append(num)

    return pruned_nums


def find_rating(
    nums: list[int], digit_count: int, prefer_ones: bool, prefer_common: bool
) -> int:
    nums_copy = copy(nums)
    for col in range(digit_count - 1, -1, -1):
        one_bits = 0
        for num in nums_copy:
            if num & pow(2, col):
                one_bits += 1

        if one_bits == len(nums_copy) / 2:
            prune_bit = 1 if prefer_ones else 0

        else:
            is_one_common = True if one_bits > len(nums_copy) / 2 else False
            """
            is_one_common prefer_common
            1 1 -> 1
            0 1 -> 0
            1 0 -> 0
            0 0 -> 1
            """
            prune_bit = 1 if not (is_one_common ^ prefer_common) else 0

        nums_copy = prune_nums(nums_copy, col, prune_bit)

        if len(nums_copy) == 1:
            return nums_copy[0]

    raise Exception(f"Could not find rating, nums down to {nums_copy}")


def part_two(input_path: str) -> int:
    digit_count, nums = parse_input(input_path)

    oxygen_rating = find_rating(nums, digit_count, True, True)
    co2_rating = find_rating(nums, digit_count, False, False)

    return oxygen_rating * co2_rating
