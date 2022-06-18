import dataclasses
import re
from typing import Literal

@dataclasses.dataclass
class Step():
  direction: Literal["forward", "down", "up"]
  magnitude: int

def parse_input(input_path: str) -> list[Step]:
  step_pat = re.compile(r"^(\w+) (\d+)$")

  steps = []
  with open(input_path, "r") as fp:
    for line in fp:
      m = step_pat.match(line)

      if not m:
        raise ValueError(f"could not parse line {line}")

      steps.append(Step(m[1], int(m[2])))

  return steps


def part_one(input_path: str) -> int:
  steps = parse_input(input_path)

  depth = 0
  horiz = 0
  for step in steps:
    match step.direction:
      case 'forward':
        horiz += step.magnitude

      case 'down':
        depth += step.magnitude

      case 'up':
        depth -= step.magnitude

  return depth * horiz


def part_two(input_path: str) -> int:
  steps = parse_input(input_path)

  aim = 0
  depth = 0
  horiz = 0
  for step in steps:
    match step.direction:
      case 'forward':
        horiz += step.magnitude
        depth += aim * step.magnitude

      case 'down':
        aim += step.magnitude

      case 'up':
        aim -= step.magnitude

  return depth * horiz