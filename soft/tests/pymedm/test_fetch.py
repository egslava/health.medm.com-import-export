import unittest, os
from zipfile import ZipFile
from pathlib import Path

import pytest

from pymedm.fetch import dashboard_url, data


@pytest.mark.realrequest
def test_dashboard_url():
    url = dashboard_url(email, passw)
    assert (
            f"https://health.medm.com/en"
            f"/records/{uuid}/dashboard"
            ==
            url
    )


@pytest.mark.realrequest
def test_data_ok():
    Path(actual_path).write_bytes(
        data(
            email, passw, uuid,
            from_date=from_, to_date=to_,
            format='csv', type='bloodpressure'
        )
    )

    msg = (
        f"Test failed: Medm returned unexpected zip. "
        f"The old zip is saved under {expected_path} "
        f"and the new one is under {actual_path}"
    )

    def crc(_): return ZipFile(_).filelist[0].CRC

    assert crc(expected_path) == crc(actual_path), msg


__import__('dotenv').load_dotenv()
email = os.getenv('MEDM_EMAIL')
passw = os.getenv('MEDM_PASSW')
uuid = "86135c4c-b705-416d-a00c-afda45a753f0"

from_ = '2022-12-10T07:10:00.000Z'
to_ = '2022-12-20T07:20:59.999Z'
dir = (
    f"tests/pymedm/data/"
    f"{email} {from_} {to_}/"
).replace(":", "-")
actual_path = dir + "actual.zip"
expected_path = dir + "expected.zip"
Path(dir).mkdir(parents=True,
                exist_ok=True)

if __name__ == '__main__':
    unittest.main()
