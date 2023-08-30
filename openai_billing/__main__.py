"""Prep __main__.py."""
# pylint: disable=invalid-name
import sys
from pathlib import Path
from typing import Optional

import typer
from loguru import logger

from openai_billing import __version__, openai_billing

del sys
# logger.remove()
# logger.add(sys.stderr, level="TRACE")

del Path, logger, openai_billing

app = typer.Typer(
    name="openai_billing",
    add_completion=False,
    help="openai_billing help",
)


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{app.info.name} v.{__version__} -- ...")
        raise typer.Exit()


@app.command()
def main(
    version: Optional[bool] = typer.Option(  # pylint: disable=(unused-argument
        None,
        "--version",
        "-v",
        "-V",
        help="Show version info and exit.",
        callback=_version_callback,
        is_eager=True,
    ),
):
    """Define."""


if __name__ == "__main__":
    app()
