import typer
from typing_extensions import Annotated


def main(
    a: Annotated[int, typer.Option(help="")],
    b: Annotated[int, typer.Option(help="")],
    c: Annotated[int, typer.Option(help="")] = False,
):
    """
    Say hi to NAME, optionally with a --lastname.

    If --formal is used, say hi very formally.
    """
    if c:
        if (a + b) > c:
            print(f"The sum is {a + b} and {c} is smaller")
    else:
        print(f"The sum of {a} and {b} is {a + b}.")


if __name__ == "__main__":
    typer.run(main)
