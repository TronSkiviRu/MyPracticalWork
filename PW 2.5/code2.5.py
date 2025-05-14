import telebot
from telebot import types
from dialogs import texts_for_base_title, texts_for_base_script, texts_for_useful_script
from emoji import EMOJI_DATA
import code_play
import datetime
import threading


API_TOKEN = '7855332191:AAGHexenIUI_W5O1xQkNH-JYOJJ3BHw2gfk'

user_useful_script_index = {}
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
    types.BotCommand("help_commands", "Список доступных команд"),
    types.BotCommand("base_title", "Необходимая База для работы"),
    types.BotCommand("base_script", "Базовые функции библиотеки"),
    types.BotCommand("useful_script", "Модификации бота"),
    types.BotCommand("about_us", "О боте, его реализации и создателях")
])


@bot.message_handler(commands=['help_commands'])
@execution_lock
def help_command(message):
    help_text = (
        "Доступные команды бота:\n"
        "/start - Перезапустить бота\n"
        "/help_commands - Список доступных команд\n"
        "/base_title - Необходимая База для работы\n"
        "/base_script - Базовые функции библиотеки\n"
        "/useful_script - Модификации бота\n"
        "/get_photo_vulkan - Отправить фото\n"
        "/get_sticker - Получить стикер из моего стикер-пака\n"
        "/learn_python - Отправит PDF файл для обучения Python\n"
        "/example_inline_keyboard - Пример, Inline Buttons\n"
        "/force_answer - Вызвать запрос на ответ (ForceReply)\n"
        "/time - Показать текущее время\n"
        "/fun_panel - Поднимает панель с эмоциями\n"
        "/about_us - Информация о боте и разработчике\n"
        "Боту можно отправить картинку и стикер\n"
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
    elif action == "all+":
        btn_prev = types.InlineKeyboardButton("Назад", callback_data=f"{prev}_{index}")
        btn_next = types.InlineKeyboardButton("Вперед", callback_data=f"{nextt}_{index}")
        btn_play = types.InlineKeyboardButton("Применить", callback_data=f"play3_{index}")
        markup.row(btn_prev, btn_play, btn_next)
    elif action == "next_play":
        btn_next = types.InlineKeyboardButton("Вперед", callback_data=f"{nextt}_{index}")
        btn_play = types.InlineKeyboardButton("Применить", callback_data=f"play3_{index}")
        markup.row(btn_play, btn_next)
    elif action == "prev_play":
        btn_prev = types.InlineKeyboardButton("Назад", callback_data=f"{prev}_{index}")
        btn_play = types.InlineKeyboardButton("Применить", callback_data=f"play3_{index}")
        markup.row(btn_prev, btn_play)
    return markup


def create_inline_keyboard():
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Нажми меня", callback_data="button_pressed")
    button2 = types.InlineKeyboardButton(text="Назад", callback_data="back_button")
    markup.row(button1, button2)
    return markup


def select_keyboard_and_text(index_message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if index_message == 0:
        return types.ReplyKeyboardRemove(), "Конец Играм"
    elif index_message == 1:
        button1 = types.KeyboardButton("👊")
        button2 = types.KeyboardButton("✌")
        button3 = types.KeyboardButton("✋")
        keyboard.add(button1, button2, button3)
        return keyboard, "Игра Камень Ножницы Бумага"
    elif index_message == 2:
        button1 = types.KeyboardButton("❤️")
        button2 = types.KeyboardButton("💌")
        button3 = types.KeyboardButton("👎")
        button4 = types.KeyboardButton("🚫")
        keyboard.add(button1, button2, button3, button4, row_width=4)
        return keyboard, "Да начнется любовь!!!"



@bot.message_handler(commands=['about_us'])
@execution_lock
def help_about(message):
    text = """
    
Чем тебе бот будет полезен?

Тут ты найдешь БАЗОВЫЕ способы реализации бота, используя функционал библиотки pyTelegramBotAPI
Научишься: заставлять бота отправлять картинку, особые сообщения, код и так далее

Почти на любую операцию бот скидывает код функционала
Боту можно отправить картинку, он отправит её обратно, можно отправить стикер, он его тоже вернет
В остальном можно бота модифицировать, через 
/useful\_script
В боте реализована сложная защита от любого спама
Бот не любит пустые слова, поэтому он их удаляет
Бот красивый, умничка, могет...

Над проетом трудилсь отзывчивая группа студентов, можешь отблагодарить их:
`2202 2050 8788 1279` - Сбер
skutaligor@gmail.com - Почта для связи

С уважением
By @TronSkiviRu 
- Скуталь Игорь Витальевич©

By @Rina8880
- Лаптева Арина Алексеевна©

By @pxnchen
- Панченко Николай Иванович©
    """
    bot.send_message(message.chat.id, text, parse_mode="Markdown")


# reply_markup=get_reply_keyboard()


@execution_lock
@bot.message_handler(commands=['start'])
def start(message):
    text = """
Привет! Этот бот призван тебя обучить созданию ботов на Python.

Пиши /help_commands, чтобы узнать больше о командах бота.
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
def send_navigation1(message):
    index = 0
    bot.send_message(message.chat.id, texts_for_base_title[index],
                     reply_markup=create_markup_for_text_info(index, "next", "prev1", "next1"),
                     parse_mode="Markdown", disable_web_page_preview=True)


@bot.message_handler(commands=['base_script'])
@execution_lock
def send_navigation2(message):
    index = 0
    bot.send_message(message.chat.id, texts_for_base_script[index],
                     reply_markup=create_markup_for_text_info(index, "next", "prev2", "next2"),
                     parse_mode="Markdown")


@bot.message_handler(commands=['useful_script'])
@execution_lock
def send_navigation3(message):
    index = 0
    if user_useful_script_index.get(message.from_user.id, 0) == 0:
        user_useful_script_index[message.from_user.id] = 0
        do_action = "next"
    else:
        do_action = "next_play"
    bot.send_message(message.chat.id, texts_for_useful_script[index],
                     reply_markup=create_markup_for_text_info(index, do_action, "prev3", "next3"),
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


@bot.message_handler(commands=['cat'])
@execution_lock
def send_cat_photo(message):
    cat_str = code_play.send_random_cat()
    profile = code_play.generate_profile()
    bot.send_photo(message.chat.id, cat_str, caption=profile)



@bot.message_handler(content_types=['photo'])
@execution_lock
def echo_photo(message):
    photo_id = message.photo[-1].file_id
    bot.send_photo(message.chat.id, photo_id)


@bot.message_handler(content_types=['sticker'])
@execution_lock
def echo_sticker(message):
    sticker_id = message.sticker.file_id
    bot.reply_to(message, "Айди этого стикера: " + sticker_id)
    bot.send_sticker(message.chat.id, sticker_id)


@bot.message_handler(commands=['get_sticker'])
@execution_lock
def send_sticker(message):
    sticker_id = 'CAACAgIAAxkBAAIBqmgi_zt-MU8bStQBr-a7urNighUnAALYGAACO7hBSM-pC_BdrnNtNgQ'
    bot.send_sticker(message.chat.id, sticker_id)


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


@execution_lock
@bot.message_handler(commands=['force_answer'])
def force_reply(message):
    markup = types.ForceReply()
    bot.send_message(message.chat.id, "Ответьте на это сообщение:", reply_markup=markup)


@execution_lock
@bot.message_handler(commands=['time'])
def send_time(message):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bot.send_message(message.chat.id, f"Текущее время: {current_time}")


@execution_lock
@bot.message_handler(func=lambda message: message.text == 'Удалить клавиатуру')
def remove_keyboard(message):
    bot.send_message(message.chat.id, "Клавиатура удалена", reply_markup=types.ReplyKeyboardRemove())


@bot.message_handler(content_types=['location'])
def handle_location(message):
    loc = message.location
    bot.send_message(message.chat.id,
                     f"Вы отправили локацию:\nШирота: {loc.latitude}\nДолгота: {loc.longitude}")


@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    contact = message.contact
    bot.send_message(message.chat.id,
                     f"Вы отправили контакт:\nИмя: {contact.first_name}\nНомер: {contact.phone_number}")


@bot.message_handler(commands=['/to_be_a_millionaire'])
def be_millionaire(message):
    try:
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        print(f"Удалено сообщение {message.message_id}")
    except Exception as e:
        print(f"Ошибка при удалении сообщения {message.message_id}: {e}")


@bot.callback_query_handler(func=lambda call:
call.data.startswith('next') or call.data.startswith('prev') or call.data.startswith('play'))
def handle_navigation(call):
    user_id = call.from_user.id
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
    elif number_arr_dialogs == "3":
        str_return = texts_for_useful_script
        str_prev = "prev3"
        str_next = "next3"

    new_index = current_index
    action_for_base_title = "all"
    action_for_useful_script = "all+"
    if action == "next":

        new_index = current_index + 1
        if new_index >= len(str_return):
            new_index = current_index - 1
        elif new_index == len(str_return) - 1:
            action_for_base_title = "prev"
            if user_useful_script_index.get(user_id, 0) == new_index:
                action_for_useful_script = "prev"
            else:
                action_for_useful_script = "prev_play"
        else:
            if user_useful_script_index.get(user_id, 0) == new_index:
                action_for_useful_script = "all"
            else:
                action_for_useful_script = "all+"
    elif action == "prev":
        new_index = current_index - 1
        if new_index < 0:
            new_index = 0
        if new_index == 0:
            action_for_base_title = "next"
            if user_useful_script_index[user_id] == new_index:
                action_for_useful_script = "next"
            else:
                action_for_useful_script = "next_play"
        else:
            if user_useful_script_index[user_id] == new_index:
                action_for_useful_script = "all"
            else:
                action_for_useful_script = "all+"

    if number_arr_dialogs == "3":
        this_action = action_for_useful_script
    else:
        this_action = action_for_base_title
    if action == "play":
        user_useful_script_index[user_id] = new_index
        bot.edit_message_text(
            str_return[current_index],
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            parse_mode="Markdown",
            reply_markup=create_markup_for_text_info(current_index, action_for_base_title, str_prev, str_next)
        )
        reply_markup_func, name_play = select_keyboard_and_text(current_index)
        bot.send_message(call.message.chat.id, name_play, reply_markup=reply_markup_func)
        if current_index == 2:
            send_cat_photo(call.message)
    else:
        bot.edit_message_text(
            str_return[new_index],
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            parse_mode="Markdown",
            reply_markup=create_markup_for_text_info(new_index, this_action, str_prev, str_next),
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


@bot.message_handler(commands=['fun_panel'])
def send_welcome(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = types.KeyboardButton("😂")
    button2 = types.KeyboardButton("🤩")
    button3 = types.KeyboardButton("😍")
    button4 = types.KeyboardButton("😜")

    keyboard.add(button1, button2)
    keyboard.add(button3, button4)

    bot.send_message(message.chat.id, "Выберите кнопку:", reply_markup=keyboard)


@bot.message_handler(func=lambda message:
message.text in ("❤️", "💌", "👎", "🚫") and user_useful_script_index.get(message.from_user.id, 0) == 2)
def handle_message(message):
    emoji = message.text
    if emoji == "❤️":
        bot.send_message(message.chat.id, "Лайк отправлен")
    elif emoji == "💌":
        bot.send_message(message.chat.id, "Замурчательная открытка")
    elif emoji == "👎":
        pass
    elif emoji == "🚫":
        bot.send_message(message.chat.id, "Вы пожаловались")
    send_cat_photo(message)



@bot.message_handler(func=lambda message:
message.text in ("👊", "✋", "✌") and user_useful_script_index.get(message.from_user.id, 0) == 1)
@execution_lock
def handle_message(message):
    player_move = message.text
    bot_move = code_play.select_item()
    info_str = code_play.result(player_move, bot_move)
    bot.send_message(message.chat.id, bot_move)
    bot.send_message(message.chat.id, info_str)


@bot.message_handler(func=lambda message: message.text in ("😂", "🤩", "😍", "😜"))
def handle_message(message):
    bot.reply_to(message, "👍", reply_markup=types.ReplyKeyboardRemove())


@bot.message_handler(content_types=['text', 'animation'])
@execution_lock
def delete_text_message(message):
    if message.text in EMOJI_DATA:
        return
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)



if __name__ == '__main__':
    print("Бот запущен...")
    bot.infinity_polling()
