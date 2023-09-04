"""Return a browser."""
# pylint: disable=too-many-branches
import subprocess
from typing import Optional

import rich
from loguru import logger
from playwright._impl._driver import compute_driver_executable, get_driver_env
from playwright.sync_api import Browser, Playwright


def get_browser(
    playwright: Playwright,
    proxy: Optional[str] = None,
    headless: bool = True,
) -> Browser:
    """Return a browser."""
    if proxy is None:
        try:
            browser = playwright.chromium.launch(
                headless=headless,
                # proxy={"server": "per-context"},
            )
        except Exception as exc:
            # exc_ = exc
            _ = "Please run the following command to download"
            if _ in f"{exc}":
                # playwright install chromium
                driver_executable = compute_driver_executable()
                completed_process = subprocess.run(
                    [str(driver_executable), "install", "chromium"],
                    env=get_driver_env(),
                    check=False,
                    capture_output=True,
                )
                if completed_process.returncode:
                    if completed_process.stdout:
                        logger.error(completed_process.stdout.decode())
                    if completed_process.stderr:
                        logger.error(completed_process.stderr.decode())
                    logger.info("Can't insatll chromium, see previous error messages")
                    raise SystemExit(1) from exc
            try:
                browser = playwright.chromium.launch(
                    headless=headless,
                    # proxy={"server": "per-context"},
                )
            except Exception as exc_:
                logger.error(exc)
                raise SystemExit(1) from exc_
    else:
        try:
            browser = playwright.chromium.launch(
                headless=headless,
                proxy={"server": proxy},
            )
        except Exception as exc:
            # exc_ = exc
            _ = "Please run the following command to download"
            if _ in f"{exc}":
                # playwright install chromium
                driver_executable = compute_driver_executable()
                completed_process = subprocess.run(
                    [str(driver_executable), "install", "chromium"],
                    env=get_driver_env(),
                    check=False,
                    capture_output=True,
                )
                if completed_process.returncode:
                    if completed_process.stdout:
                        logger.error(completed_process.stdout.decode())
                    if completed_process.stderr:
                        logger.error(completed_process.stderr.decode())
                    logger.info("Can't insatll chromium, see previous error messages")
                    raise SystemExit(1) from exc
            try:
                browser = playwright.chromium.launch(
                    headless=headless,
                    proxy={"server": proxy},
                )
            except Exception as exc_:
                logger.error(exc)
                if "Invalid URL" in str(exc):
                    rich.print(f"\t probably a problem with the {proxy=} format")
                raise SystemExit(1) from exc_
    return browser
