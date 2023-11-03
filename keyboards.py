from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

# Main menu
btn1 = KeyboardButton('О компании')
btn2 = KeyboardButton('Где находимся?')
btn3 = KeyboardButton('Новости')
btn4 = KeyboardButton('Отправить резюме')
btn5 = KeyboardButton('Контакты')

markup = ReplyKeyboardMarkup()
markup.row(btn1, btn2)
markup.add(btn3)
markup.row(btn4, btn5)

# Submenu for btn2 button
submenu_btn2_btn1 = InlineKeyboardButton('Отправить адрес', callback_data='address')
submenu_btn2_btn2 = InlineKeyboardButton('Показать местоположение на карте', callback_data='map')
submenu_markup = InlineKeyboardMarkup().row(submenu_btn2_btn1, submenu_btn2_btn2)