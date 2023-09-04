# openai-billing-playwright
[![pytest](https://github.com/ffreemt/openai-billing-playwright/actions/workflows/routine-tests.yml/badge.svg)](https://github.com/ffreemt/openai-billing-playwright/actions)[![python](https://img.shields.io/static/v1?label=python+&message=3.8%2B&color=blue)](https://www.python.org/downloads/)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/openai_billing.svg)](https://badge.fury.io/py/openai-billing)

Fetch openai billing info from command line

## Install it

```shell
pip install openai-billing
# pip install git+https://github.com/ffreemt/openai-billing-playwright
# poetry add git+https://github.com/ffreemt/openai-billing-playwright
# git clone https://github.com/ffreemt/openai-billing-playwright && cd openai-billing-playwright
```

## Use it
```bash
python -m openai_billing

# or
openai-billing

# help
python -m openai_billing --help

# check two pairs
python -m openai_billing u@gmai.com pw1 u2@gmai.com pw2

# or special characters (&, * etc) in passwords
python -m openai_billing "u@gmai.com pw*1 u2@gmai.com pw2&"

# check pairs in clipboard
python -m openai_billing

# check pairs in a file
python -m openai_billing --filename email-pw-pairs.txt

# use a proxy
python -m openai_billing --proxy soscks5://127.0.0.1:1080 u@gmai.com pw1 u2@gmai.com pw2

# turn on browser: to see the whole thing in action
python -m openai_billing u@gmai.com pw1 --headful

# turn on debug
set LOGURU_LEVEL=TRACE
python -m openai_billing u@gmai.com pw1 --headful

```
