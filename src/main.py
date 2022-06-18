import importlib
import typer

app = typer.Typer()

@app.command()
def day(day_number: str):
  day_solution = importlib.import_module(f"days.{day_number}")
  day_input = f"src/days/data/{day_number}.txt"

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