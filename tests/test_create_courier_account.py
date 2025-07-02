import requests
import allure
import pytest

from data import Data

class TestCourierCreation:

    @allure.title('Проверка создания курьера с валидными значениями во всех обязательных полях')
    @allure.description('1. Отправить запрос на создание курьера '
                        '2. Проверить код ответа и тело ответа'
                        '3. Удалить курьера')
    def test_courier_account_is_created(self, login_and_delete_account):

        payload = login_and_delete_account

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        assert response.status_code == 201
        assert response.json() == {'ok': True}



    @allure.title('Негативная проверка создания курьера при повторном использовании логина')
    @allure.description('1. Отправить запрос на создание курьера '
                        '2. Проверить код ответа и тело ответа'
                        '3. Отправить запрос на создание курьера с теми же данными'
                        '4. Проверить код ответа и тело ответа'
                        '5. Удалить курьера')
    def test_same_login_creation_courier_account_error_is_appeared(self,login_and_delete_account):

        payload = login_and_delete_account

        response_1 = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        assert response_1.status_code == 201
        assert response_1.json() == {'ok': True}

        response_2 = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        assert response_2.status_code == 409
        assert response_2.json().get("code") == 409
        assert "Этот логин уже используется" in response_2.json().get("message", "")



    @allure.title('Негативная проверка создания курьера при отсутствии заполнения обязательного поля')
    @allure.description('1. Отправить запрос на создание курьера '
                        '2. Проверить код ответа и тело ответа')
    @pytest.mark.parametrize('empty_fields', [
        {'login': '', 'password': Data.generate_random_string(5), 'firstName': Data.generate_random_string(10)},
        {'login': Data.generate_random_string(10), 'password': '', 'firstName': Data.generate_random_string(10)}
    ])
    def test_create_courier_missing_required_fields(self,empty_fields):
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=empty_fields)
        assert response.status_code == 400
        assert response.json().get("message") == "Недостаточно данных для создания учетной записи"
        assert response.json().get("code") == 400

