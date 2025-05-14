from random import choice

import requests

CAT_API_URL = 'https://api.thecatapi.com/v1/images/search'
CAT_API_KEY = 'live_jISbjZpCsZlb35iH0j4bZSKnkOior5RAxVusNrNOhw8WtuToscEYA3VcgZIoadhh'


def select_item():
    item3_arr = ["👊", "✋", "✌"]
    return choice(item3_arr)


def result(player_arm, bot_arm):
    if player_arm == bot_arm:
        return "Ничья"
    elif (player_arm == "👊" and bot_arm == "✌" or
          player_arm == "✋" and bot_arm == "👊" or
          player_arm == "✌" and bot_arm == "✋"):
        return "Победа"
    else:
        return "Поражение"


def send_random_cat():
    headers = {
        'x-api-key': CAT_API_KEY
    }
    response = requests.get(CAT_API_URL, headers=headers)
    if response.status_code == 200:
        cat_data = response.json()
        cat_image_url = cat_data[0]['url']
        return cat_image_url
    else:
        return "Не удалось получить изображение котенка. Попробуйте позже."


cat_names = ("Муся", "Шкурка", "Мадонна", "Мася", "Пушинка", "Фрикаделька", "Киса", "Кися",
            "ТракторМурка", "Лизоок", "Ням-ня")

start_phrase = [
    "Истина",
    "Бытие",
    "Смысл существования",
    "Путь души",
    "Свет разума"
]

main_phrase = [
    "находится в глубине",
    "отражается в",
    "проявляется через",
    "исходит из",
    "оживляет"
]

end_phrase = [
    "вечности",
    "моря времени",
    "безмолвия ночи",
    "огня бытия",
    "тишины вселенной"
]


def generate_profile():
    part0 = choice(cat_names)
    part1 = choice(start_phrase)
    part2 = choice(main_phrase)
    part3 = choice(end_phrase)
    return f"{part0}:\n{part1} {part2} {part3}."
