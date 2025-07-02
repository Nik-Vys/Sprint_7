import string
import random


class Data:
    # Генерация валидных значений для создания аккаунта курьера
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string