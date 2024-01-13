from telebot import types

# Кнопка номера
def num_bt():
    # Создаем пространство
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Создаем сами кнопки
    number = types.KeyboardButton('Отправить номер', request_contact=True)
    # Добавляем кнопки в пространство
    kb.add(number)
    return kb

# Кнопка геолокации
def loc_bt():
    # Создаем пространство
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Создаем сами кнопки
    location = types.KeyboardButton('Отправить локацию', request_location=True)
    # Добавляем кнопки в пространство
    kb.add(location)
    return kb

# Главная кнопка
def main_menu_buttons():
    # Создаем пространство
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Создаем сами кнопки
    secret = types.KeyboardButton('Узнать тайну всего мира!')
    helper = types.KeyboardButton('Помощь')
    kb.add(secret, helper)
    return kb
# Кнопка ок
def ok():
    # Создаем пространство
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Создаем сами кнопки
    ok = types.KeyboardButton('ОК')
    kb.add(ok)
    return kb