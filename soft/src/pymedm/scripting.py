from . import fetch, parse
from .parse import csv_from_zip, formatiso


def load_medm(email, password,
              from_date='2022-11-05T21:00:00.000Z',
              to_date='2022-12-05T20:59:59.999Z',
              type_='bloodpressure'):
    url = fetch.dashboard_url(email, password)
    uuid = parse.uuid_from_dashboard_url(url)

    bytes_ = fetch.data(
        email=email,
        password=password,
        uuid=uuid,
        from_date=formatiso(from_date),
        to_date=formatiso(to_date),
        format='csv',
        type=type_
    )

    return csv_from_zip(bytes_)
