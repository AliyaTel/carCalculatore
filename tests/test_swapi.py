import pytest
import requests

URL = 'https://wexler.io'


@pytest.fixture
def token():
    url = f'{URL}/user/login/'
    res = requests.post(url, data={
        'username': 'teltaevaaliya@gmail.com',
        'password': 'aliya1206'
    })
    data = res.json()
    return data['access']


def test_get_car_engines(token):
    url = f"{URL}/garage/car_engines/"
    res = requests.get(url, headers={'Authorization': f'Bearer {token}'})
    assert res.status_code == 200
    data = res.json()
    assert isinstance(data, dict)


def test_swapi_people():
    url = 'https://swapi.dev/api/people'
    res = requests.get(url)
    assert res.status_code == 200
    data = res.json()
    person_found = False
    for person in data['results']:
        if person['name'] == 'Luke Skywalker':
            assert person['eye_color'] == 'blue'
            person_found = True
    assert person_found
