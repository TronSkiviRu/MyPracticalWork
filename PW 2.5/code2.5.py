import telebot
from telebot import types
from dialogs import texts_for_base_title, texts_for_base_script
import datetime
import threading


API_TOKEN = '7855332191:AAGHexenIUI_W5O1xQkNH-JYOJJ3BHw2gfk'

user_message_permission = {}


def execution_lock(func):
    def wrapper(message, *args, **kwargs):
        user_id = message.from_user.id
        if user_message_permission.get(user_id, False):
            bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            return
        user_message_permission[user_id] = True  # Устанавливаем флаг, что команда выполняется
        try:
            return func(message, *args, **kwargs)
        finally:
            threading.Timer(3, lambda: user_message_permission.update({user_id: False})).start()
    wrapper.__name__ = func.__name__  # Сохраняем имя оригинальной функции
    wrapper.__doc__ = func.__doc__  # Сохраняем документацию оригинальной функции
    return wrapper


bot = telebot.TeleBot(API_TOKEN)

bot.set_my_commands([
    types.BotCommand("start", "Перезапустить бота"),
    types.BotCommand("help_comands", "Список доступных команд"),
    types.BotCommand("base_title", "Необходимая База для работы"),
    types.BotCommand("base_script", "Базовые функции библеотеки"),
    types.BotCommand("useful_commands", "То, что можно запустить в запустить в боте"),
    types.BotCommand("about_us", "О боте, его реализации и создателе")
])


@bot.message_handler(commands=['help_commands'])
@execution_lock
def help_command(message):
    help_text = (
        "Доступные команды бота:\n"
        "/start - Перезапустить бота\n"
        "/help_commands - Список доступных команд\n"
        "/base_title - Необходимая База для работы\n"
        "/base_script - Базовые функции библеотеки\n"
        "/useful_commands - Это можно запустить в запустить в боте\n"
        "/get_photo_vulkan - Отправить фото\n"
        "/get_sticker - Получить стикер из моего стикер-пака\n"
        "/learn_python - Отправит PDF файл для обучения Python\n"
        "/example_inline_keyboard - Пример, Inline Buttons\n"
        "/force_answer - Вызвать запрос на ответ (ForceReply)\n"
        "/time - Показать текущее время\n"
        "/about_us - Информация о боте и разработчике\n"
        "/Боту можно отправить картинку и стикер\n"
        "Также можно отправить локацию или контакт напрямую."
    )
    bot.send_message(message.chat.id, help_text)


def create_markup_for_text_info(index, action: str, prev: str, nextt: str):
    markup = types.InlineKeyboardMarkup()
    if action == "all":
        btn_prev = types.InlineKeyboardButton("Назад", callback_data=f"{prev}_{index}")
        btn_next = types.InlineKeyboardButton("Вперед", callback_data=f"{nextt}_{index}")
        markup.row(btn_prev, btn_next)
    elif action == "next":
        btn_next = types.InlineKeyboardButton("Вперед", callback_data=f"{nextt}_{index}")
        markup.row(btn_next)
    elif action == "prev":
        btn_prev = types.InlineKeyboardButton("Назад", callback_data=f"{prev}_{index}")
        markup.row(btn_prev)
    return markup


def get_reply_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_location = types.KeyboardButton('Отправить локацию', request_location=True)
    btn_contact = types.KeyboardButton('Отправить контакт', request_contact=True)
    btn_remove = types.KeyboardButton('Удалить клавиатуру')
    markup.add(btn_location, btn_contact)
    markup.add(btn_remove)
    return markup


def get_inline_keyboard():
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Кнопка 1', callback_data='btn1')
    btn2 = types.InlineKeyboardButton('Кнопка 2', callback_data='btn2')
    btn_url = types.InlineKeyboardButton('Перейти на Google', url='https://google.com')
    markup.add(btn1, btn2)
    markup.add(btn_url)
    return markup


def create_inline_keyboard():
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Нажми меня", callback_data="button_pressed")
    button2 = types.InlineKeyboardButton(text="Назад", callback_data="back_button")
    markup.row(button1, button2)
    return markup


@bot.message_handler(commands=['about_us'])
@execution_lock
def help_about(message):
    text = """
    
Чем тебе бот будет полезен?

Тут ты найдешь БАЗОВЫЕ способы реализации бота, используя функционал библеотки pyTelegramBotAPI
Узнаешь как: заставить бота отправить картинку, особое сообщение, код и так далее

Почти на любую операцию бот скидывает код функционала
Боту можно отправить картинку, он отправит её обратно, можно отправить стикер, он его тоже вернет
В остальном можно бота модифицировать, через /useful\_commands
В боте реализована сложная защита от спама
Бот красивый, умничка, могет

Над проетом трудился отзывчивая группастудентов можешь отблагодарить их:
`2202 2050 8788 1279` - Сбер
skutaligor@gmail.com - Почта для связи

С уважением
By @TronSkiviRu 
- Скуталь Игорь Витальевич©

By @Rina8880
- Лаптева Арина Алексеевна©

    """
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

# reply_markup=get_reply_keyboard()


@execution_lock
@bot.message_handler(commands=['start'])
def start(message):
    text = """
Привет! Этот бот призван тебя обучить созданию ботов на Python.

Пиши /help_commands, чтобы узнать больше об командах бота.
В остальном введи /base_title, если готов идти дальше.

Также тебя будут сопровождать такие сообщения снизу, они будут показывать, как реализовать код в самом Python.

Например, вот функция для этого сообщения:

<pre>
@bot.message_handler(commands=['start'])
def start(message):
    text = '''
    # Тут было предисловие
    '''
    bot.send_message(message.chat.id, text, reply_markup=get_reply_keyboard(), parse_mode="Markdown")
    
</pre>
"""
    bot.send_message(message.chat.id, text, parse_mode="HTML")
    help_about(message)


@bot.message_handler(commands=['base_title'])
@execution_lock
def send_navigation(message):
    index = 0
    bot.send_message(message.chat.id, texts_for_base_title[index],
                     reply_markup=create_markup_for_text_info(index, "next", "prev1", "next1"),
                     parse_mode="Markdown", disable_web_page_preview=True)


@bot.message_handler(commands=['base_script'])
@execution_lock
def send_navigation(message):
    index = 0
    bot.send_message(message.chat.id, texts_for_base_script[index],
                     reply_markup=create_markup_for_text_info(index, "next", "prev2", "next2"),
                     parse_mode="Markdown")


@bot.message_handler(commands=['get_photo_vulkan'])
@execution_lock
def inline(message):
    bot.reply_to(message, "Сейчас я пришлю тебе красивый вулкан; это ответ  на твое сообщение")

    try:
        with open('PW 2.5/vulkan.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption="Это подпись к картинке.")
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка при отправке фото: {e}")
    bot.send_message(message.chat.id, texts_for_base_script[1], parse_mode="Markdown")


@bot.message_handler(content_types=['photo'])
@execution_lock
def echo_photo(message):
    photo_id = message.photo[-1].file_id
    bot.send_photo(message.chat.id, photo_id)
    bot.send_message(message.chat.id, texts_for_base_script[0], parse_mode="Markdown")


@bot.message_handler(content_types=['sticker'])
@execution_lock
def echo_sticker(message):
    sticker_id = message.sticker.file_id
    bot.reply_to(message, "Айди этого стикера: "+sticker_id)
    bot.send_sticker(message.chat.id, sticker_id)
    bot.send_message(message.chat.id, texts_for_base_script[2], parse_mode="Markdown")




@bot.message_handler(commands=['get_sticker'])
@execution_lock
def send_sticker(message):
    sticker_id = 'CAACAgIAAxkBAAIBqmgi_zt-MU8bStQBr-a7urNighUnAALYGAACO7hBSM-pC_BdrnNtNgQ'
    bot.send_sticker(message.chat.id, sticker_id)
    bot.send_message(message.chat.id, texts_for_base_script[3], parse_mode="Markdown")


@bot.message_handler(commands=['learn_python'])
@execution_lock
def send_document(message):
        chat_id = message.chat.id
        bot.send_message(chat_id, "Подождите, файл отправляется...")
        bot.send_chat_action(chat_id, action='upload_document')
        try:
            with open('PW 2.5/learnPython.pdf', 'rb') as doc:
                bot.send_document(message.chat.id, doc, caption="Выучи Python за месяц!")
        except Exception as e:
            bot.send_message(message.chat.id, f"Ошибка при отправке документа: {e}")
        bot.send_message(message.chat.id, texts_for_base_script[4], parse_mode="Markdown")


@execution_lock
@bot.message_handler(commands=['force_answer'])
def force_reply(message):
    markup = types.ForceReply(selective=False)
    bot.send_message(message.chat.id, "Ответьте на это сообщение:", reply_markup=markup)


@execution_lock
@bot.message_handler(commands=['time'])
def send_time(message):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bot.send_message(message.chat.id, f"Текущее время: {current_time}")
# Удаление кастомной клавиатуры

@execution_lock
@bot.message_handler(func=lambda message: message.text == 'Удалить клавиатуру')
def remove_keyboard(message):
    bot.send_message(message.chat.id, "Клавиатура удалена", reply_markup=types.ReplyKeyboardRemove())


@bot.message_handler(content_types=['location'])
def handle_location(message):
    loc = message.location
    bot.send_message(message.chat.id, f"Вы отправили локацию:\nШирота: {loc.latitude}\nДолгота: {loc.longitude}")
# Обработка присланного контакта


@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    contact = message.contact
    bot.send_message(message.chat.id, f"Вы отправили контакт:\nИмя: {contact.full_name}\nНомер: {contact.phone_number}")
# Обработка inline-кнопок (btn1, btn2)


@bot.message_handler(commands=['/to_be_a_millionaire'])
def delete_text_message(message):
    try:
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        print(f"Удалено сообщение {message.message_id}")
    except Exception as e:
        print(f"Ошибка при удалении сообщения {message.message_id}: {e}")


@bot.callback_query_handler(func=lambda call: call.data.startswith('next') or call.data.startswith('prev'))
def handle_navigation(call):
    global str_return, str_prev, str_next
    data = call.data
    try:
        action, index_str = data.split("_")
        current_index = int(index_str)
    except ValueError:
        return
    # Парсим строку вида next1
    action, number_arr_dialogs = action[:-1], action[-1]

    if number_arr_dialogs == "1":
        str_return = texts_for_base_title
        str_prev = "prev1"
        str_next = "next1"
    elif number_arr_dialogs == "2":
        str_return = texts_for_base_script
        str_prev = "prev2"
        str_next = "next2"

    new_index = current_index
    action_for_base_title = "all"
    if action == "next":

        new_index = current_index + 1
        if new_index >= len(str_return):
            new_index = current_index - 1
        if new_index == len(str_return) - 1:
            action_for_base_title = "prev"
    elif action == "prev":
        new_index = current_index - 1
        if new_index < 0:
            new_index = 0
        if new_index == 0:
            action_for_base_title = "next"

    bot.edit_message_text(
        str_return[new_index],
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        parse_mode="Markdown",
        reply_markup=create_markup_for_text_info(new_index, action_for_base_title, str_prev, str_next),
        disable_web_page_preview=True
    )
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data in ['btn1', 'btn2'])
def handle_inline_buttons(call):
    if call.data == 'btn1':
        bot.answer_callback_query(call.id, "Вы нажали кнопку 1")
        bot.send_message(call.message.chat.id, "Вы выбрали кнопку 1")
    elif call.data == 'btn2':
        bot.answer_callback_query(call.id, "Вы нажали кнопку 2")
        bot.send_message(call.message.chat.id, "Вы выбрали кнопку 2")


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


@bot.message_handler(commands=['example_inline_keyboard'])
def start_command(message):
    markup = create_inline_keyboard()
    bot.send_message(
        chat_id=message.chat.id,
        text="Привет! Это демонстрационное сообщение с инлайн кнопками.",
        reply_markup=markup
    )


@bot.message_handler(content_types=['text', 'animation'])
def delete_text_message(message):
    try:
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    except Exception as e:
        print(f"Ошибка при удалении сообщения {message.message_id}: {e}")


if __name__ == '__main__':
    print("Бот запущен...")
    bot.infinity_polling()




