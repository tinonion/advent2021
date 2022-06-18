import importlib
import os
import typer

app = typer.Typer()

@app.command()
def day(day_number: str, use_sample_input=typer.Option(False, "--use-sample-input", "-s", is_flag=True, flag_value=True)):
  solution_path = f"days.{day_number}"
  try:
    day_solution = importlib.import_module(solution_path)
  
  except ModuleNotFoundError:
    typer.echo(f"solution for day {day_number} not found")
    return

  if use_sample_input:
    day_input = f"src/days/input/{day_number}-sample.txt"
  else:
    day_input = f"src/days/input/{day_number}.txt"

  if not os.path.exists(day_input):
    type.echo(f"can't find input file {day_input}")
    return

  try:
    typer.echo(f"part one: {day_solution.part_one(day_input)}")

  except AttributeError:
    typer.echo(f"day {day_number} solution is missing a part one")

  try:
    typer.echo(f"part two: {day_solution.part_two(day_input)}")

  except AttributeError:
    typer.echo(f"part two solution missing")


def main():
  app()