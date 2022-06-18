def parse_depths(input_path: str) -> list[int]:
  with open(input_path, "r") as fp:
    return [int(line) for line in fp]


def part_one(input_path: str) -> int: 
  depths = parse_depths(input_path)

  increasing = 0
  prev = depths[0]
  for depth in depths[1:]:
    if depth > prev:
      increasing += 1
    
    prev = depth

  return increasing


def part_two(input_path: str) -> int:
  depths = parse_depths(input_path)

  increasing = 0
  prev = sum(depths[0:3])
  for i in range(1, len(depths) - 2):
    curr = sum(depths[i:i + 3])
    if curr > prev:
      increasing += 1

    prev = curr

  return increasing 


if __name__ == "__main__":
  print(part_one("./days/data/1.txt"))
  print(part_two("./days/data/1.txt"))
