import csv
import unittest
from unittest.mock import MagicMock

__import__('dotenv').load_dotenv()
import os

# 1. new medm account
# 2. env variables
# 3. Run tests locally

# 4. add login/pass to secrets +
# 5. run some tests only on ci/cd on github

# class TestMedm:
#     def test_medm_didnt_change_api:

from pymedm import load_medm, fetch


def mock() -> None:
    from pathlib import Path

    fetch.data = MagicMock(
        return_value=Path(
            "tests/pymedm/data/medm@egslava"
            ".ru 2022-12-10T07-10-00.000Z "
            "2022-12-20T07-20-59.999Z/actual.zip"
        ).read_bytes()
    )

    uuid = '33deeb7b-24c9-4f1d-a7ac-b493c833ce44'
    fetch.dashboard_url = MagicMock(
        return_value=f"https://health.medm.com/en/"
                     f"records/{uuid}/dashboard"
    )

mock()

def test_load_medm():
    result = load_medm(
        os.getenv('MEDM_EMAIL'),
        os.getenv('MEDM_PASSW')
    )
