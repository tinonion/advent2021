class FishClock:
    init_time = 2
    r_time = 7

    def __init__(self, start_times: list[int]):
        self.init_clock = [0 for _ in range(self.init_time)]
        self.init_ind = 0
        self.r_clock = [0 for _ in range(self.r_time)]
        self.r_ind = 0

        for t in start_times:
            self.r_clock[t] += 1

    def advance_init_clock(self, new_children: int) -> int:
        # returns number of newly grown up fish
        new_adults = self.init_clock[self.init_ind]
        self.init_clock[self.init_ind] = new_children
        self.init_ind = (self.init_ind + 1) % len(self.init_clock)
        return new_adults

    def advance_clock(self):
        new_children = self.r_clock[self.r_ind]
        new_adults = self.advance_init_clock(new_children)
        self.r_clock[self.r_ind] += new_adults
        self.r_ind = (self.r_ind + 1) % len(self.r_clock)

    def get_total_fish(self):
        return sum(self.init_clock) + sum(self.r_clock)


def parse_input(input_path: str) -> FishClock:
    with open(input_path, "r") as fp:
        nums = [int(n) for n in fp.readline().split(",")]

    return FishClock(nums)


def part_one(input_path: str) -> int:
    fish_clock = parse_input(input_path)

    for _ in range(80):
        fish_clock.advance_clock()

    return fish_clock.get_total_fish()

def part_two(input_path: str) -> int:
    fish_clock = parse_input(input_path)

    for _ in range(256):
        fish_clock.advance_clock()

    return fish_clock.get_total_fish()
