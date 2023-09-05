"""
Prep for nuitka build.

# https://github.com/Nuitka/Nuitka/issues/1029
set PLAYWRIGHT_BROWSERS_PATH=0
python -m playwright install chromium
"""
import os

from openai_billing.__main__ import app

# https://github.com/Nuitka/Nuitka/issues/1029
os.environ["PLAYWRIGHT_BROWSERS_PATH"] = "0"

if __name__ == "__main__":
    app()
