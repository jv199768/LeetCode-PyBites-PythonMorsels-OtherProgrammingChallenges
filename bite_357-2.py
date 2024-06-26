import typer
from rich.progress import track
import time

app = typer.Typer()

@app.command()
def sum(a: int, b: int):
    typer.echo(f"The sum of {a} and {b} is {a + b}.")
    total = 0
    for value in track(range(2), description="Processing..."):
        # Fake processing time
        time.sleep(0.01)
        total += 1
    print(f"Processed {total} things.")


@app.command()
def subtract(a: int, b: int):
    typer.echo(f"Subtraction of {a} and {b} yields {a - b}.")
    total = 0
    for value in track(range(2), description="Processing..."):
        # Fake processing time
        time.sleep(0.01)
        total += 1
    print(f"Processed {total} things.")


if __name__ == "__main__":
    app()
