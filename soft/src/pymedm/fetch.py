import requests

_BASE_URL = "https://health.medm.com"
_HEADERS = dict(
    headers={
        'Content-Type': 'application/x-www-form-urlencoded',
    }
)


def data(
        email,
        password,
        uuid,
        from_date='2022-11-05T21:00:00.000Z',
        to_date='2022-12-05T20:59:59.999Z',
        format='csv',
        type='bloodpressure'
):
    url = f"{_BASE_URL}/en" \
          f"/records/{uuid}/export_result"

    params = {
        'from_date': from_date,
        'to_date': to_date,
        'select-all': 1,
        'measurement_types[]': type,
        'format': format,
        'group_by': 'type',
    }
    response = requests.get(
        url,
        params=params,
        data={'email': email,
              'password': password},
        **_HEADERS
    )

    return response.content


def dashboard_url(email, password):
    url = f"{_BASE_URL}/en/user/login"

    payload = {'email': email, 'password': password}

    # returns 401, but redirects to the correct url
    response = requests.post(url, payload, **_HEADERS)

    return response.url
