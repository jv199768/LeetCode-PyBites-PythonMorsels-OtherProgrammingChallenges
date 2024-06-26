import typer
import time
from rich.progress import track

app = typer.Typer()

@app.command()
def add(a: int = typer.Argument(help="The value of the first summand", show_default=False), b: int = typer.Argument(help="The value of the second summand", show_default=False)):
    typer.echo(f"The sum of {a} and {b} is {a + b}.")
    total = 0
    for value in track(range(2), description="Processing..."):
        # Fake processing time
        time.sleep(0.01)
        total += 1
    print(f"Processed {total} things.")

if __name__ == "__main__":
    app()
    #typer.run(main)
