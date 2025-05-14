texts_for_base_title = [
    """
_1/5:_

Начнем с основ. Чтобы создать собственного бота, нам понадобится его токен и немного кода на Python.

Чтобы получить токен бота, необходимо создать его в главном Telegram-боте: [@BotFather](https://t.me/BotFather).

1. Переходим к @BotFather и создаем нового бота.
2. Копируем токен, который будет выглядеть примерно так:
`7855332191:AAGHexenIUI_W5O1xQkNH-JYOJJ3BHw2g`

3. В @BotFather можно задать базовые настройки для бота: добавить изображение, описание и многое другое.

Теперь у вас есть токен, с которым можно работать! 

    """,
    """
_2/5:_
Теперь я держу надежду, что вы умеете программировать на Python и вопросов лишиних не будет
Если не умеете, то без прочтения не возвращаитесь /learn\_python

Нам нужна библеотека для работы с ботом, увы она не встроена поэтому устанавливаем
`pip install pyTelegramBotAPI`

И далее мы добавляем модули:
```
import telebot
# Для удобства
from telebot import types
    ```

    """,
    """
_3/5:_
Отлично! Теперь добавим в наш код строку с апишкой и разберем что произошло

```
API_TOKEN = '7855332191:AAGHexenIUI_W5O1xQkNH-JYOJJ3BHw2g'
bot = telebot.TeleBot(API_TOKEN)

# Далее идет основная часть кода, она у всех разная и ситуативная

if __name__ == '__main__':
    print("Бот запущен...")
    bot.infinity_polling() 
```
bot = telebot.TeleBot(API_TOKEN) - делает экземпляр класса бота к которому мы можем обращаться

bot.infinity_polling() - не выключает запуск программы, держит бота в автономном режиме

Так мы связали нашего телеграм бота с нашим кодом, ура  

    """,
    """
_4/5:_
Для того, чтобы заставллять бота делать что-то надо читать 
[Документацию по pyTelegramBotAPI на русском](https://pytba.readthedocs.io/ru/latest/)

Или продолжить пользоваться ботом и вы узнаете, как пользоваться основными функциями бота
Жми /help\_commands и иди по списку вниз, по новым командам

    """,
    """
_5/5:_
Появились вопросы? Обращайся к моему [личному AI-агенту](https://gpt-chatbot.ru/openai-o3-mini)
Знает все, ответит на все вопросы!
Исправит любую ошибку!

    """
]
texts_for_base_script = [
    """
Бот отправляющий картинку в ответ на полученную картинку

```
@bot.message_handler(content_types=['photo'])
def echo_photo(message):
    photo_id = message.photo[-1].file_id
    bot.send_photo(message.chat.id, photo_id)
```
Получили айди фотки и отправили его же через функцию

    """,
    """

Введя слудующую команду бот скинет фото в чат, важно чтобы файл с фото был в директории проекта

```
bot.message_handler(commands=['get_photo_vulkan'])
def inline(message):
    bot.reply_to(message, "Сейчас я пришлю тебе красивый вулкан; это ответ  на твое сообщение")

    try:
        with open('vulkan.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption="Это подпись к картинке.")
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка при отправке фото: {e}")
```


    """,
    """
Бот вернет вам ваш телеграмм стикер в ответ на ваш телеграм стикер, и выдаст его айди

```
@bot.message_handler(content_types=['sticker'])
def echo_sticker(message):
    sticker_id = message.sticker.file_id
    bot.reply_to(message, "Айди этого стикера: "+sticker_id)
    bot.send_sticker(message.chat.id, sticker_id)
```


    """,
    """
Бот вернет указанный в айди телеграмм стикер по соответствующей команде

```
@bot.message_handler(commands=['get_sticker'])
def send_sticker(message):
    sticker_id = 'CAACAgIAAxkBAAIBqmgi_zt-MU8bStQBr-a7urNighUnAALYGAACO7hBSM-pC_BdrnNtNgQ'
    bot.send_sticker(message.chat.id, sticker_id)
```

    """,
    """
Этот код скидывает документ, в нем есть защита от спама с помощью глобальной переменной
Также при отправке файла бот будет иметь подпись что отправляется файл

```
@bot.message_handler(commands=['learn_python'])
def send_document(message):
    global one_start_file
    if one_start_file:
        one_start_file = False
        chat_id = message.chat.id
        bot.send_message(chat_id, "Подождите, файл отправляется...")
        bot.send_chat_action(chat_id, action='upload_document')
        try:
            with open('learnPython.pdf', 'rb') as doc:
                bot.send_document(message.chat.id, doc, caption="Выучи Python за месяц!")
        except Exception as e:
            bot.send_message(message.chat.id, f"Ошибка при отправке документа: {e}")
        one_start_file = True
```
    """,
    """
Рассмотрим код который позволяет вывести сообщение рядом с которым будут кнопки или инлайн кнопки.
Для этого применяется метод send\_message с параметром reply\_markup, в который передается объект InlineKeyboardMarkup.
Мы это сделаем через функцию

```
def create_inline_keyboard():
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Нажми меня", callback_data="button_pressed")
    button2 = types.InlineKeyboardButton(text="Назад", callback_data="back_button")
    markup.row(button1, button2)
    return markup

@bot.message_handler(commands=['example_inline_keyboard'])
def start_command(message):
    markup = create_inline_keyboard()
    bot.send_message(
        chat_id=message.chat.id,
        text="Привет! Это демонстрационное сообщение с инлайн кнопками.",
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data in ("button_pressed", "back_button"))
def callback_handler(call):
    if call.data == "button_pressed":
        bot.answer_callback_query(call.id, "Кнопка нажата!")
        bot.send_message(call.message.chat.id, "Вы нажали первую кнопку.")
    elif call.data == "back_button":
        bot.answer_callback_query(call.id, "Кнопка Назад нажата!")
        bot.send_message(call.message.chat.id, "Вы нажали кнопку 'Назад'.")
    else:
        bot.answer_callback_query(call.id, "Неизвестное действие.")
```
Кода много давай разбираться:
Для обработки нажатий на инлайн кнопки используется специальный декоратор, который принимает функцию-обработчик 
колбэков. Делается с помощью @bot.callback_query_handler. Обработчик получает объект call, 
из которого можно извлечь данные, такие как call.data, call.message, call.id и т.д.

Можешь попробовать в живую /example\_inline\_keyboard
    """,
    """
Реализация удалений сообщений через бота

```
@bot.message_handler(commands=['/to\_be\_a\_millionaire'])
def delete_text_message(message):
    try:
        bot.delete_message(chat_id=message.chat.id, message_id=message.message\_id)
        print(f"Удалено сообщение {message.message\_id}")
    except Exception as e:
        print(f"Ошибка при удалении сообщения {message.message\_id}: {e}")
```
Попробуй /to\_be\_a\_millionaire
    """,
    """
Сообщает время

```
@bot.message_handler(commands=['time'])
def send_time(message):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bot.send_message(message.chat.id, f"Текущее время: {current_time}")
```
/time
    """,
    """
Реализация защиты от спама

```
# Словарь для хранения данных о пользователях
user_data = {}

# Значения лимита
LIMIT_MESSAGES = 2   # максимальное количество сообщений
LIMIT_TIME = 2       # за сколько секунд


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.from_user.id
    current_time = time()

    if user_id not in user_data:
        user_data[user_id] = {
            'count': 1,
            'last_time': current_time
        }
    else:
        elapsed = current_time - user_data[user_id]['last_time']

        if elapsed < LIMIT_TIME:
            user_data[user_id]['count'] += 1
        else:
            # Если прошло достаточное время, сбрасываем счётчик
            user_data[user_id]['count'] = 1

        # Обновляем время последнего сообщения
        user_data[user_id]['last_time'] = current_time

    # Если число сообщений превышает лимит, принимаем меры
    if user_data[user_id]['count'] > LIMIT_MESSAGES:
        try:
            # Например, удаляем сообщение
            bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            # Или отправляем предупреждение
            bot.send_message(message.chat.id, f"@{message.from_user.username}, слишком много сообщений!")
        except Exception as e:
            print(f"Ошибка при удалении сообщения {message.message_id}: {e}")
```
Попробуй сюда заспамить, дружок;)
    """,

]
