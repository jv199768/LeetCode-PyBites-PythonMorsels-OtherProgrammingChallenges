import typer
import time
from rich.progress import track
import algo


app = typer.Typer()
app.add_typer(algo.app, name="algo")

@app.command()
def sum(a: int = typer.Argument(help="The value of the first summand", show_default=False), b: int = typer.Argument(help="The value of the second summand", show_default=False)):
    typer.echo(f"The sum of {a} and {b} is {a + b}.")
    total = 0
    for value in track(range(2), description="Processing..."):
        # Fake processing time
        time.sleep(0.01)
        total += 1
    print(f"Processed {total} things.")
@app.command()
def compare(d: int, c: int):
    if d > c:
        typer.echo(f"d={d} is greater than c={c}.")
    elif c > d:
        typer.echo(f"d={d} is lesser than c={c}.")
    total = 0
    for value in track(range(2), description="Processing..."):
        # Fake processing time
        time.sleep(0.01)
        total += 1
    print(f"Processed {total} things.")

if __name__ == "__main__":
    app()
    #typer.run(main)
