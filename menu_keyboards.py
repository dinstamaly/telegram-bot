
import telegram
from key_buttons import (
    tele_button, nav_button, deposit_menu, credit1_menu,
    credit2_menu, credit3_menu, credit4_menu,
    currency)


def main_menu_keyboard():
    keyboard = ([
        [
            telegram.KeyboardButton(tele_button[0]),
            telegram.KeyboardButton(tele_button[1])
        ],
        [
            telegram.KeyboardButton(tele_button[2]),
            telegram.KeyboardButton(tele_button[3])
        ],
        [
            telegram.KeyboardButton(tele_button[4]),
            telegram.KeyboardButton(tele_button[5])
        ],
        [
            telegram.KeyboardButton(tele_button[6]),
            telegram.KeyboardButton(tele_button[7])
        ]
    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )


def atm_menu_keyboard():
    menu_keyboard = ([
        [telegram.KeyboardButton(nav_button[0], request_location=True)],
        [telegram.KeyboardButton(nav_button[1])],
    ])
    return telegram.ReplyKeyboardMarkup(
        menu_keyboard, resize_keyboard=True, one_time_keyboard=False
    )


def depo_menu_keyboard():
    menu_keyboard = ([
        [telegram.KeyboardButton(nav_button[0], request_location=True)],
        [telegram.KeyboardButton(nav_button[1])]
    ])
    return telegram.ReplyKeyboardMarkup(
        menu_keyboard, resize_keyboard=True, one_time_keyboard=False
    )


def deposits_menu_keyboard():
    menu_keyboard = ([
        [telegram.KeyboardButton(deposit_menu[0])],
        [
            telegram.KeyboardButton(deposit_menu[1]),
            telegram.KeyboardButton(deposit_menu[2])
        ],
        [
            telegram.KeyboardButton(deposit_menu[3]),
            telegram.KeyboardButton(deposit_menu[4])
        ],
        [telegram.KeyboardButton(nav_button[1])]
    ])
    return telegram.ReplyKeyboardMarkup(
        menu_keyboard, resize_keyboard=True, one_time_keyboard=False
    )


def credits_menu_keyboard():
    menu_keyboard = ([
        [telegram.KeyboardButton(credit1_menu[0])],
        [
            telegram.KeyboardButton(credit1_menu[1]),
            telegram.KeyboardButton(credit1_menu[2])
        ],
        [telegram.KeyboardButton(nav_button[1])]
    ])
    return telegram.ReplyKeyboardMarkup(
        menu_keyboard, resize_keyboard=True, one_time_keyboard=False
    )


def potreb_menu_keyboard():
    menu_keyboard = ([
        [telegram.KeyboardButton(credit2_menu[0])],
        [
            telegram.KeyboardButton(credit2_menu[1]),
            telegram.KeyboardButton(credit2_menu[2])
        ],
        [
            telegram.KeyboardButton(credit2_menu[3]),
            telegram.KeyboardButton(credit2_menu[4])
        ],
        [telegram.KeyboardButton(nav_button[2])]
    ])
    return telegram.ReplyKeyboardMarkup(
        menu_keyboard, resize_keyboard=True, one_time_keyboard=False
    )


def ipoteka_menu_keyboard():
    menu_keyboard = ([
        [telegram.KeyboardButton(credit3_menu[0])],
        [
            telegram.KeyboardButton(credit3_menu[1]),
            telegram.KeyboardButton(credit3_menu[2])
        ],
        [telegram.KeyboardButton(nav_button[2])]
    ])
    return telegram.ReplyKeyboardMarkup(
        menu_keyboard, resize_keyboard=True, one_time_keyboard=False
    )


def auto_menu_keyboard():
    menu_keyboard = ([
        [telegram.KeyboardButton(credit4_menu[0])],
        [telegram.KeyboardButton(credit4_menu[1])],
        [telegram.KeyboardButton(nav_button[2])]
    ])
    return telegram.ReplyKeyboardMarkup(
        menu_keyboard, resize_keyboard=True, one_time_keyboard=False
    )


def currency_menu_keyboard():
    menu_keyboard = ([
        [
            telegram.KeyboardButton(currency[0]),
            telegram.KeyboardButton(currency[1]),
            telegram.KeyboardButton(currency[2]),
            telegram.KeyboardButton(currency[3]),
        ],
        [
            telegram.KeyboardButton(currency[4]),
            telegram.KeyboardButton(currency[5]),
            telegram.KeyboardButton(currency[6]),
            telegram.KeyboardButton(currency[7]),
        ],
        [
            telegram.KeyboardButton(currency[8]),
            telegram.KeyboardButton(currency[9]),
            telegram.KeyboardButton(currency[10]),
            telegram.KeyboardButton(currency[11]),
        ],
        [
            telegram.KeyboardButton(currency[12]),
            telegram.KeyboardButton(currency[13]),
            telegram.KeyboardButton(currency[14]),
            telegram.KeyboardButton(currency[15]),
        ],
        [telegram.KeyboardButton(nav_button[1])]
    ])
    return telegram.ReplyKeyboardMarkup(
        menu_keyboard, resize_keyboard=True, one_time_keyboard=False
    )
