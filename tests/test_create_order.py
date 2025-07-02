import requests
import allure
import pytest


class TestOrderCreation:

    @allure.title('Проверка создания заказа с разными цветами')
    @allure.description('1. Отправить запрос на создание заказа с определенным типом цвета '
                        '2. Проверить код ответа и тело ответа')
    @pytest.mark.parametrize('color',
                             [{"color": ["BLACK"]}, {"color": ["GREY"]}, {"color": ["BLACK", "GRAY"]}, {"color": []}])
    def test_create_order_order_created(self, color):
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": color["color"]
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', json=payload)

        assert response.status_code == 201
        assert "track" in response.json()