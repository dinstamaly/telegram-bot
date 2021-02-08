import re

import requests
from telegram import Update
from telegram.ext import (
    Updater, CommandHandler, CallbackContext, MessageHandler, Filters,
    PicklePersistence,
)

from creadentials import bot_token, map_token, atm_url, currency_url
from key_buttons import (
    tele_button, nav_button, credit1_menu, deposit_menu, credit2_menu,
    credit3_menu, credit4_menu, currency
)
from button_dict import dep_menu, cred_menu, info_button

from menu_keyboards import (
    main_menu_keyboard, atm_menu_keyboard, depo_menu_keyboard,
    deposits_menu_keyboard, credits_menu_keyboard, potreb_menu_keyboard,
    ipoteka_menu_keyboard, auto_menu_keyboard, currency_menu_keyboard,
)
from messages import (
    m_atm, m_depo, m_auto, m_main, m_credit, m_deposit,
    m_ipoteka, m_potreb, m_currency
)

TOKEN = bot_token
MAP_TOKEN = map_token


############################### Bot ##########################################
def start(bot, update):
    bot.message.reply_text(
        main_menu_message(),
        reply_markup=main_menu_keyboard()
    )


############################### Location #####################################
def location(update: Update, context: CallbackContext):
    message = update.message
    current_position = (message.location.longitude, message.location.latitude)
    if list(context.user_data.values())[-1] == ('Банкоматы',):
        context.user_data.pop('Банкоматы')
        r = requests.post(atm_url,
                          json={
                              "lat": current_position[1],
                              "long": current_position[0],
                              "type_code": "BANKOMAT"
                          }, headers={"Authorization": "Basic MTE6MQ==",
                                      "Content-Type": "application/json"},
                          verify=False)
        # получаем данные
        json_data = r.json()

        for atm in json_data.get('atm_list', []):
            msg = context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=atm["name"] + "\n" + atm["address"])
            context.bot.sendLocation(
                chat_id=update.effective_chat.id,
                longitude=atm["long"],
                latitude=atm["lat"],
                reply_to_message_id=msg.message_id
            )

    elif list(context.user_data.values())[-1] == ('🏦 Отделения',):
        context.user_data.pop('🏦 Отделения')
        # ,
        r = requests.post(atm_url,
                          json={
                              "lat": current_position[1],
                              "long": current_position[0],
                              "type_code": "BRANCH"
                          }, headers={"Authorization": "Basic MTE6MQ==",
                                      "Content-Type": "application/json"},
                          verify=False)
        # получаем данные
        json_data = r.json()

        for atm in json_data.get('atm_list', []):
            msg = context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=atm["name"] + "\n" + atm["address"])
            context.bot.sendLocation(
                chat_id=update.effective_chat.id,
                longitude=atm["long"], latitude=atm["lat"],
                reply_to_message_id=msg.message_id
            )


############################ Keyboards #####################################
# from menu_keyboards
############################ REGEX #########################################
DEPOSITS_REGEX = r"(?=(" + (tele_button[4]) + r"))"
CREDITS_REGEX = r"(?=(" + (tele_button[3]) + '|' + (nav_button[2]) + r"))"
CREDITS_POTREB_REGEX = r"(?=(" + (credit1_menu[0]) + r"))"
CREDITS_IPOTEKA_REGEX = r"(?=(" + (credit1_menu[1]) + r"))"
CREDITS_AUTO_REGEX = r"(?=(" + (credit1_menu[2]) + r"))"
CURRENCY_REGEX = r"(?=(" + (tele_button[5]) + r"))"
HOME_REGEX = r"(?=(" + (nav_button[1]) + r"))"
D_INFO_REGEX = r"(?=(" + '|'.join(deposit_menu) + r"))"
INFO_REGEX = r"(?=(" + (tele_button[2]) + '|' + (tele_button[6]) + \
             '|' + (tele_button[7]) + r"))"
C_1_INFO_REGEX = r"(?=(" + '|'.join(credit2_menu) + r"))"
C_2_INFO_REGEX = r"(?=(" + '|'.join(credit3_menu) + r"))"
C_3_INFO_REGEX = r"(?=(" + (credit4_menu[0]) + '|' + (credit4_menu[1]) + r"))"
CURRENCY_CODE_REGEX = r"(?=(" + '|'.join(currency) + r"))"

############################# Messages #######################################
ATM_REGEX = r'^🏧 (Банкоматы)$'


def receive_atm_location(update: Update, context: CallbackContext):
    info = re.match(ATM_REGEX, update.message.text).groups()
    context.user_data[info[0]] = (info[0],)
    update.message.reply_text(m_atm,
                              reply_markup=atm_menu_keyboard()
                              )


DEPO_REGEX = r'^(🏦 Отделения)$'


def receive_depo_location(update: Update, context: CallbackContext):
    info = re.match(DEPO_REGEX, update.message.text).groups()
    context.user_data[info[0]] = (info[0],)
    update.message.reply_text(m_depo,
                              reply_markup=depo_menu_keyboard()
                              )


def receive_deposit_option(update: Update, context: CallbackContext):
    info = re.match(DEPOSITS_REGEX, update.message.text)
    update.message.reply_text(m_deposit,
                              reply_markup=deposits_menu_keyboard()
                              )


def receive_credit_option(update: Update, context: CallbackContext):
    info = re.match(CREDITS_REGEX, update.message.text)
    update.message.reply_text(m_credit,
                              reply_markup=credits_menu_keyboard()
                              )


def receive_potreb_option(update: Update, context: CallbackContext):
    info = re.match(CREDITS_POTREB_REGEX, update.message.text)
    update.message.reply_text(m_potreb,
                              reply_markup=potreb_menu_keyboard()
                              )


def receive_ipoteka_option(update: Update, context: CallbackContext):
    info = re.match(CREDITS_IPOTEKA_REGEX, update.message.text)
    update.message.reply_text(m_ipoteka,
                              reply_markup=ipoteka_menu_keyboard()
                              )


def receive_auto_option(update: Update, context: CallbackContext):
    info = re.match(CREDITS_AUTO_REGEX, update.message.text)
    update.message.reply_text(m_auto,
                              reply_markup=auto_menu_keyboard()
                              )


def receive_currency_option(update: Update, context: CallbackContext):
    info = re.match(CURRENCY_REGEX, update.message.text)
    update.message.reply_text(m_currency,
                              reply_markup=currency_menu_keyboard()
                              )


def back_main_menu(update: Update, context: CallbackContext):
    info = re.match(HOME_REGEX, update.message.text)
    update.message.reply_text(
        m_main,
        reply_markup=main_menu_keyboard()
    )


def receive_info(update: Update, context: CallbackContext):
    info = re.match(INFO_REGEX, update.message.text).groups()

    for item in info_button:
        if item['name'] == info[0]:
            update.message.reply_text(item['desc'])


def receive_deposit_info(update: Update, context: CallbackContext):
    info = re.match(D_INFO_REGEX, update.message.text).groups()
    for i in dep_menu[tele_button[4]]:
        if i['name'] == info[0]:
            update.message.reply_text(i['desc'])


def receive_potreb_info(update: Update, context: CallbackContext):
    info = re.match(C_1_INFO_REGEX, update.message.text).groups()
    for i in cred_menu[credit1_menu[0]]:
        if i['name'] == info[0]:
            update.message.reply_text(i['desc'])


def receive_ipoteka_info(update: Update, context: CallbackContext):
    info = re.match(C_2_INFO_REGEX, update.message.text).groups()
    for i in cred_menu[credit1_menu[1]]:
        if i['name'] == info[0]:
            update.message.reply_text(i['desc'])


def receive_auto_info(update: Update, context: CallbackContext):
    info = re.match(C_3_INFO_REGEX, update.message.text).groups()
    for i in cred_menu[credit1_menu[2]]:
        if i['name'] == info[0]:
            update.message.reply_text(i['desc'])


def code_info(update: Update, context: CallbackContext):
    info = re.match(CURRENCY_CODE_REGEX, update.message.text).groups()
    #
    r = requests.get(
        currency_url,
        json={},
        headers={"Authorization": "Basic MTE6MQ==",
                 "Content-Type": "application/json"},
        verify=False)
    # получаем данные
    json_data = r.json()
    for currency in json_data.get('currencies', []):
        if info[0] == currency["code"]:
            update.message.reply_text(
                f"{currency['code']}: {currency['buy']} - {currency['sell']}\n"
                f"НБКР: {currency['nbkr']}"
            )


def main_menu_message():
    return "Добро пожалоавть, выберите опцию: "


updater = Updater(TOKEN, persistence=PicklePersistence(filename='bot_data'))

updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(ATM_REGEX),
    receive_atm_location))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(DEPO_REGEX),
    receive_depo_location))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(INFO_REGEX),
    receive_info))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(DEPOSITS_REGEX),
    receive_deposit_option))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(D_INFO_REGEX),
    receive_deposit_info))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(CREDITS_REGEX),
    receive_credit_option))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(CREDITS_POTREB_REGEX),
    receive_potreb_option))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(CREDITS_IPOTEKA_REGEX),
    receive_ipoteka_option))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(CREDITS_AUTO_REGEX),
    receive_auto_option))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(C_1_INFO_REGEX),
    receive_potreb_info))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(C_2_INFO_REGEX),
    receive_ipoteka_info))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(C_3_INFO_REGEX),
    receive_auto_info))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(CURRENCY_REGEX),
    receive_currency_option))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(CURRENCY_CODE_REGEX),
    code_info))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(HOME_REGEX),
    back_main_menu))
updater.dispatcher.add_handler(
    MessageHandler(Filters.location,
                   location))

updater.start_polling()
updater.idle()
