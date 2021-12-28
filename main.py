# не спрашивай почему в мейне, просто так захотелось


TOKEN = '1935890794:AAG1pkfgdSy9wjEq8tnA3ZzXz3FrXy0YNvQ'
help_message = '''
Через этого бота можно купить курсы, чтобы посмотреть, как происходит покупка и оплата в Telegram.
Отправьте команду /buy, чтобы перейти к покупке.
Узнать правила и положения можно воспользовавшись командой /terms.
'''

start_message = 'Привет! Это демонстрация работы платежей в Telegram!\n' + help_message

pre_buy_demo_alert = '''\
Так как сейчас я запущен в тестовом режиме, для оплаты нужно использовать карточку с номером `4242 4242 4242 4242`
Счёт для оплаты:
'''

terms = '''\
*Спасибо, что выбрали нашего бота. Мы надеемся, вам понравится этот опыт!*
'''

tm_title = 'А1 курс'
tm_description = '''\
Хотите выучить английский и не дегродить?
'''


successful_payment = '''
Ура! Платеж на сумму `{total_amount} {currency}` совершен успешно! Приятного пользования тестами!
Правила возврата средств смотрите в /terms
Купить ещё  - /buy
'''


MESSAGES = {
    'start': start_message,
    'help': help_message,
    'pre_buy_demo_alert': pre_buy_demo_alert,
    'terms': terms,
    'tm_title': tm_title,
    'tm_description': tm_description,
     #'AU_error': AU_error,
     #'wrong_email': wrong_email,
    'successful_payment': successful_payment,
}
