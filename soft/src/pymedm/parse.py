from io import BytesIO
from typing import Union
import time
from zipfile import ZipFile


def uuid_from_dashboard_url(url):
    """
    >>> uuid_from_dashboard_url(
    ...     'https://health.medm.com/en/records/'
    ...     '33deeb7b-24c9-4f1d-a7ac-b493c833ce44/'
    ...     'dashboard'
    ... )
    '33deeb7b-24c9-4f1d-a7ac-b493c833ce44'
    """
    begin = len('https://health.medm.com/en/records/')
    end = len('/dashboard')
    uuid = url[begin:-end]

    # assertion part...
    lens = *map(len, uuid.split('-')),
    assert (8, 4, 4, 4, 12) == lens
    return uuid


def formatiso(time: Union[str, int]):
    """
    >>> _ = 'Changing the timezone';
    ... __import__('os').environ['TZ'] = "+03:00"
    ... time.tzset()

    >>> formatiso(0)
    '1970-01-01T00:00:00.000Z'

    >>> formatiso('1970-01-01T00:00:00.000Z')
    '1970-01-01T00:00:00.000Z'

    >>> formatiso('13/12/2020')
    '2020-12-12T21:00:00.000Z'

    >>> formatiso('13/12/2020 20:00')
    '2020-12-13T17:00:00.000Z'
    """
    from datetime import datetime, timezone as tz

    if isinstance(time, int):
        date = datetime.fromtimestamp(time, tz.utc)
    else:
        from dateutil.parser import parse
        date = parse(time)
    return (
        date.astimezone(tz.utc)
            .isoformat(timespec='milliseconds')
            .replace("+00:00", "Z")
    )


def csv_from_zip(bytes_):
    with ZipFile(BytesIO(bytes_)) as f:
        filename, = f.namelist()
        with f.open(filename) as f:
            return f.read()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
