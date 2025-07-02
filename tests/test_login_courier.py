import requests
import allure
import pytest
from data import Data

class TestLoginCourier:

    @allure.title('Проверка авторизации курьера с валидными значениями')
    @allure.description('1. Отправить запрос на авторизацию курьера '
                        '2. Проверить код ответа и тело ответа'
                        '3. Удалить курьера')
    def test_login_courier_account_login_done(self,valid_courier):
        login_payload = {
            "login": valid_courier["login"],
            "password": valid_courier["password"]
        }
        login_response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=login_payload)
        assert login_response.status_code == 200
        assert 'id' in login_response.text



    @allure.title('Проверка авторизации курьера с невалидными значениями')
    @allure.description('1. Отправить запрос на авторизацию курьера с неверным логином/паролем '
                        '2. Проверить код ответа и тело ответа'
                        '3. Удалить курьера')
    @pytest.mark.parametrize('fake_fields', [
        {'login': 'fake_login', 'password': Data.generate_random_string(5),},
        {'login': Data.generate_random_string(10), 'password': 'fake_password',}
    ])
    def test_login_courier_account_fake_fields_error_is_appeared(self,valid_courier,fake_fields):

        login_response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=fake_fields)
        assert login_response.status_code == 404
        assert login_response.json().get("message") == "Учетная запись не найдена"


    @allure.title('Проверка авторизации курьера с пустыми значениями полей')
    @allure.description('1. Отправить запрос на авторизацию курьера с пустым значением логина/пароля'
                        '2. Проверить код ответа и тело ответа'
                        '3. Удалить курьера')
    @pytest.mark.parametrize('empty_fields', [
        {'login': '', 'password': Data.generate_random_string(5),},
        {'login': Data.generate_random_string(10), 'password': '',}
    ])
    def test_login_courier_account_empty_fields_error_is_appeared(self,valid_courier, empty_fields):

        login_response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=empty_fields)
        assert login_response.status_code == 400
        assert login_response.json().get("message") == "Недостаточно данных для входа"
