"""Define openai_billing."""
# pylint: disable=broad-exception-raised
import rich
from loguru import logger
from playwright.sync_api import BrowserContext, Page  # ._generated


def login_page(
    email: str,
    password: str,
    context: BrowserContext,
    # headless: bool = False,
) -> Page:
    r"""
    Login and return page.

    based on deepl-fanyi\login-openai1.py
    """
    page = context.new_page()
    page.goto("https://platform.openai.com/account/usage")
    page.get_by_role("button", name="Log in‍").click()
    page.get_by_label("Email address").fill(email)
    page.get_by_role("button", name="Continue", exact=True).click()

    logger.trace(" Email address clicked")

    page.wait_for_selector("html")
    _ = page.locator("html").inner_text().lower()

    # email is not valid
    if "email is not valid" in _:
        _ = page.locator("span").get_by_text("wrong email or password").inner_text()
        rich.print(f"[bold red]\tUnable to login, [yellow]reasone: {_}")
        page.close()
        # raise SystemExit(1)
        raise Exception("email is not valid")

    page.wait_for_selector("#password")
    _ = (
        "Unable to locate the password field, "
        "net down? proxy invalid? "
        "openai uasage page layout changed? ",
        "contact the dev to fix it if feasible. ",
    )
    assert page.locator("#password").count() == 1, _
    page.locator("#password").fill(password)

    page.get_by_role("button", name="Continue", exact=True).click()
    logger.trace(" Email/password submitted")

    page.wait_for_selector("html")
    _ = page.locator("html").inner_text().lower()

    # wrong email or password
    if "wrong email or password" in _:
        _ = page.locator("span").get_by_text("wrong email or password").inner_text()
        rich.print(f"[bold red]\tUnable to login, [yellow]reasone: {_}")
        page.close()
        # raise SystemExit(1)
        raise Exception("wrong email or password")

    # ip not good enough
    if "not avail" in page.locator("html").inner_text().lower():
        _ = page.locator("html").inner_text()
        rich.print(
            f"[bold red] Cannot login to [green] https://platform.openai.com/account/usage. [yellow]Reason: {_} [red] Use a good proxy/vpn and try again"
        )
        page.close()
        raise SystemExit(1)

    # page.wait_for_selector(".usage-grants")
    page.wait_for_selector(".month-tokens")

    return page


def openai_billing(page: Page) -> str:
    """
    Fetch various information pieces.

    "https://platform.openai.com/account/usage"
        .month-tokens .usage-grants
    "https://platform.openai.com/account/billing/overview"
        .billing-credit-balance-value
    """
    logger.trace(f" {page.url=} ")

    month_tokens = ""
    if page.locator(".month-tokens").count() == 1:
        month_tokens = page.locator(".month-tokens").inner_text()
    else:
        logger.warning("Unable to retrieve .months-tokens, check it out")

    usage_grants = ""
    if page.locator(".usage-grants").count() == 1:
        usage_grants = page.locator(".usage-grants").inner_text()
    else:
        logger.warning("Unable to retrieve .usage-grants, check it out")

    used, _, total = month_tokens.partition(" / ")
    expiration_date = usage_grants.split("\t")[-1]

    return f"{total}, {used} (used), {expiration_date}"
