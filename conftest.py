import pytest
import requests
from data import Data


# Фикстура авторизации и удаление курьера
@pytest.fixture
def login_and_delete_account():

    payload = {
        "login": Data.generate_random_string(10),
        "password": Data.generate_random_string(5),
        "firstName": Data.generate_random_string(10)
    }
    created_id = []

    yield payload

    login_response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
    assert login_response.status_code == 200
    courier_id = login_response.json().get("id")
    created_id.append(courier_id)


    for courier_id in created_id:
        delete_response = requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}')
        assert delete_response.status_code == 200
        assert delete_response.json() == {'ok': True}

# Фикстура создания и удаление курьера
@pytest.fixture
def valid_courier():
    payload = {
        "login": Data.generate_random_string(10),
        "password": Data.generate_random_string(5),
        "firstName": Data.generate_random_string(10)
    }

    create_response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
    assert create_response.status_code == 201
    assert create_response.json() == {'ok': True}

    login_response = requests.post(
        'https://qa-scooter.praktikum-services.ru/api/v1/courier/login',
        data={"login": payload["login"], "password": payload["password"]}
    )
    assert login_response.status_code == 200
    courier_id = login_response.json().get("id")

    yield {
        "login": payload["login"],
        "password": payload["password"],
        "id": courier_id
    }

    delete_response = requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}')
    assert delete_response.status_code == 200
    assert delete_response.json() == {'ok': True}