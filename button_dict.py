from credit_info import all_purposes, without_deposit, buy_product, elkart_visa, installment, \
    ipoteka, ipo_bank, gov_ipo_comp, car_partners, auto_
from info_text import cards_, contacts_, transfers_
from deposit_info import deposit_emerge, deposit_abundance, deposit_capital, deposit_pension, deposit_kid
from key_buttons import tele_button, deposit_menu, credit1_menu, credit2_menu, credit3_menu, credit4_menu

info_button = [
    {'name': tele_button[2], 'desc': contacts_, },
    {'name': tele_button[6], 'desc': cards_, },
    {'name': tele_button[7], 'desc': transfers_, }]

dep_menu = {
    tele_button[4]: [
        {'name': deposit_menu[0], 'desc': deposit_emerge, },
        {'name': deposit_menu[1], 'desc': deposit_abundance, },
        {'name': deposit_menu[2], 'desc': deposit_capital, },
        {'name': deposit_menu[3], 'desc': deposit_pension, },
        {'name': deposit_menu[4], 'desc': deposit_kid, },
    ] }

cred_menu = {credit1_menu[0]: [
    {'name': credit2_menu[0], 'desc': all_purposes, },
    {'name': credit2_menu[1], 'desc': without_deposit, },
    {'name': credit2_menu[2], 'desc': buy_product, },
    {'name': credit2_menu[3], 'desc': elkart_visa, },
    {'name': credit2_menu[4], 'desc': installment, }, ],
    credit1_menu[1]: [
        {'name': credit3_menu[0], 'desc': ipoteka, },
        {'name': credit3_menu[1], 'desc': gov_ipo_comp, },
        {'name': credit3_menu[2], 'desc': ipo_bank, }
    ], credit1_menu[2]: [
        {'name': credit4_menu[0], 'desc': car_partners, },
        {'name': credit4_menu[1], 'desc': auto_, },
    ],
}
