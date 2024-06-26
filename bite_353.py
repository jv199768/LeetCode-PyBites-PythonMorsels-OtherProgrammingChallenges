import typer

app = typer.Typer()

@app.command()
def add(a: int = typer.Argument(help="The value of the first summand", show_default=False), b: int = typer.Argument(help="The value of the second summand", show_default=False)):
    typer.echo(f"The sum of {a} and {b} is {a + b}.")

if __name__ == "__main__":
    app()
