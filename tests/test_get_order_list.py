import requests
import allure
import pytest


class TestOrderList:

    @allure.title('Проверка получения списка заказов')
    @allure.description('1. Отправить запрос на получение списка заказа'
                        '2. Проверить код ответа и тело ответа')
    def test_get_order_list_list_appeared(self):
        response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders')

        assert response.status_code == 200
        assert type(response.json()['orders']) == list and 'id' in response.json()['orders'][0]

