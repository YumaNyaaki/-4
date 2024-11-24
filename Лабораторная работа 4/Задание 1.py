import json


def task() -> float:
    # Чтение данных из JSON файла
    with open('input.json', 'r') as file:
        data = json.load(file)

    # Нахождение суммы произведений значений словарей "score" и "weight"
    Sum_of_the_product = sum(item['score'] * item['weight'] for item in data)

    return round(Sum_of_the_product, 3)


print(task())
