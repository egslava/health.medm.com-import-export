import pytest

from pymedm.parse import (uuid_from_dashboard_url,
                          csv_from_zip)

from unittest import TestCase
from glob import glob

FILENAMES = glob('tests/pymedm/data/*/actual.zip')


def test_uuid_from_redirect():
    uuid = '33deeb7b-24c9-4f1d-a7ac-b493c833ce44'
    url = (
        f"https://health.medm.com/en/records/"
        f"{uuid}/dashboard"
    )

    assert uuid == uuid_from_dashboard_url(url)


@pytest.mark.parametrize('filename', FILENAMES)
def test_csv_from_zip(filename):
    # assert does not fail
    with open(filename, 'rb') as file:
        bytes = file.read()
        csv_from_zip(bytes)
