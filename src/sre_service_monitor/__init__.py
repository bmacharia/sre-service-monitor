import logging
import sys
from importlib.metadata import version
from typing import Annotated

import typer

app = typer.Typer(help="Check the health of HTTP, TCP, and systemd targets.")


def show_version(value: bool) -> None:
    if value:
        typer.echo(f"sre-service-monitor {version('sre-service-monitor')}")
        raise typer.Exit()


@app.command()
def run(
    verbose: Annotated[
        bool, typer.Option("--verbose", "-v", help="Enable debug logging")
    ] = False,
    version_requested: Annotated[
        bool,
        typer.Option(
            "--version",
            callback=show_version,
            is_eager=True,
            help="Show the program version and exit",
        ),
    ] = False,
) -> None:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        stream=sys.stderr,
    )
    logging.getLogger(__name__).info("Scaffold ready; checks not implemented yet")


def main() -> None:
    app()
