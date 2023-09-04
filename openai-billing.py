"""Prep for nuitka build."""
# ruff: noqa: F401
# import gradio_client  # nuitka
# import loguru
# import pyperclip
# import rich
# import typer

from openai_billing.__main__ import app

if __name__ == "__main__":
    app()
