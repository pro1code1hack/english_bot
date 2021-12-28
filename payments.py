# import random
# import time
# import typing
# from datetime import datetime, timedelta
# from typing import Dict, List, Tuple, TypeVar
# from asyncio import sleep
# from aiogram import Bot, types
# from aiogram.dispatcher import Dispatcher, FSMContext
# from aiogram.dispatcher.filters import Command
# from aiogram.utils import executor
# import sqlite3
# import config as con  # buttons
# import random as r
# import asyncio
# import logging
# from aiogram.types.message import ContentType
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
#
# from pyqiwip2p.AioQiwip2p import AioQiwiP2P
# from pyqiwip2p.types import QiwiCustomer, QiwiDatetime
# from main import MESSAGES
# # from config import TOKEN, PAYMENTS_PROVIDER_TOKEN, Creator
# from config import TOKEN
# from service import register_user, get_quiz_questions, get_user_test_question_id, \
#     get_question_info, save_user_result, get_user_subscriptions, get_topic_url, get_listening_info, set_user_level
# from aiogram.types import InputFile, InlineKeyboardButton, InlineKeyboardMarkup
# import Texts as t
# from states import Test
#
# QIWI_PRIV_KEY = "eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6Ims3NjB5Yi0wMCIsInVzZXJfaWQiOiIzODA5MzQxMzA2MjUiLCJzZWNyZXQiOiJjN2RmY2JhZWNiMDQ1Y2ZmM2JmYjhlZjVlZmVkZjZmZjQxYWUyZDU3OTYxNTYzNWNmNzFiNDZhN2E0ODUwMTY4In19"
# p2p = AioQiwiP2P(auth_key=QIWI_PRIV_KEY)
#
# LEVELS = {
#     1: 'A1',
#     2: 'A2',
#     3: 'B1',
#     4: 'B2'
# }
#
# loop = asyncio.get_event_loop()
# storage = MemoryStorage()
# bot = Bot(TOKEN, parse_mode='HTML')
# dp = Dispatcher(bot, loop=loop, storage=storage)
#
#
# def check_subscriptions(func):
#     async def wrapper(message: types.Message):
#         user_id = message.from_user.id
#         user_subscriptions = get_user_subscriptions(user_id)
#         request_subscription = message.text[-3:-1:]
#         if request_subscription not in user_subscriptions:
#             return await bot.send_message(message.from_user.id, 'Купи подписку бичь')
#         return await func(message)
#
#     return wrapper
#
#
# # проверка отправляется ли instant view #
#
# def get_user_level(score: int) -> int:
#     if score <= 15:
#         level = 1
#     elif score <= 25:
#         level = 2
#     elif score <= 35:
#         level = 3
#     else:
#         level = 4
#     return level
#
#
# def generate_inline_keyboard(options: List) -> InlineKeyboardMarkup:
#     keyboard = InlineKeyboardMarkup()
#     # _len = 0
#     # cancel_button = InlineKeyboardButton('Отменить прохождение теста', callback_data='cancel')
#     # keyboard.add(cancel_button)
#     for option in options:
#         btn = InlineKeyboardButton(option, callback_data=f'ans/{option}')
#         keyboard.add(btn)
#         # _len += len(option)
#     return keyboard
#
#
# @dp.message_handler(text='Определить уровень❓', state=None)
# async def enter_test(message: types.Message, state: FSMContext):
#     if message.text == 'Определить уровень❓':
#         quiz_id = 1
#         quiz = get_quiz_questions(quiz_id)
#         async with state.proxy() as data:
#             data['quiz_id'] = quiz_id
#             data['questions'] = quiz
#             question = data['questions'].pop(0)
#             data['last_questions_id'] = question['id']
#             data['score'] = 0
#         options = [option['text'] for option in question['options']]
#         keyboard = generate_inline_keyboard(options)
#         await bot.send_message(message.chat.id, question['task_text'], reply_markup=keyboard)
#         await Test.AdaptiveTest.set()
#
#
# @dp.message_handler(commands=['cancel'], state=Test.InProgress)
# async def cancel_test(message: types.Message, state: FSMContext):
#     await state.finish()
#     await bot.send_message(message.from_user.id, 'Тест прерван', reply_markup=con.Main_menu)
#
#
# @dp.message_handler(commands=['cancel'], state=Test.AdaptiveTest)
# async def cancel_test(message: types.Message, state: FSMContext):
#     await state.finish()
#     await bot.send_message(message.from_user.id, 'Тест прерван', reply_markup=con.Main_menu)
#
#
# @dp.callback_query_handler(lambda c: c.data and c.data.startswith('Test'), state=None)
# async def process_callback_kb1btn1(callback_query: types.CallbackQuery, state: FSMContext):
#     quiz_id = int(
#         callback_query.data[5:])  # Беремо ід теста з команди /Test id. З ПЯТОГО символа начинается номера теста
#     quiz = get_quiz_questions(quiz_id)
#     async with state.proxy() as data:
#         data['quiz_id'] = quiz_id
#         data['questions'] = quiz
#         question = data['questions'].pop(0)
#         data['last_questions_id'] = question['id']
#         data['score'] = 0
#     options = [option['text'] for option in question['options']]
#     keyboard = generate_inline_keyboard(options)
#     await bot.send_message(callback_query.from_user.id, question['task_text'], reply_markup=keyboard)
#
#     await Test.InProgress.set()
#
#
# @dp.callback_query_handler(lambda c: c.data and c.data.startswith('ans'), state=Test.InProgress)
# async def process_callback_kb1btn1(callback_query: types.CallbackQuery, state: FSMContext):
#     async with state.proxy() as data:
#         question_id = data['last_questions_id']
#         left_questions = data['questions']
#     answer = callback_query.data[4:]
#     question = get_question_info(question_id)
#     correct_answer = get_question_correct_answer(question['options'])
#     if answer == correct_answer:
#         await bot.send_message(callback_query.from_user.id, f'Правильно ✅')
#         async with state.proxy() as data:
#             data['score'] += question['weight']
#     else:
#         await bot.send_message(callback_query.from_user.id, f'Неправильно❌\nОтвет: asfasfa')
#     if left_questions:
#         async with state.proxy() as data:
#             question = data['questions'].pop(0)
#             data['last_questions_id'] = question['id']
#         options = [option['text'] for option in question['options']]
#         keyboard = generate_inline_keyboard(options)
#         await bot.send_message(callback_query.from_user.id, question['task_text'], reply_markup=keyboard)
#     else:
#         async with state.proxy() as data:
#             score = data['score']
#             quiz_id = data['quiz_id']
#         save_user_result(callback_query.from_user.id, quiz_id, score)
#         await bot.send_message(callback_query.from_user.id, f'Тест завершено. У вас {score} балов из 20')
#         await state.finish()
#
#
# @dp.callback_query_handler(lambda c: c.data and c.data.startswith('ans'), state=Test.AdaptiveTest)
# async def process_callback_kb1btn1(callback_query: types.CallbackQuery, state: FSMContext):
#     async with state.proxy() as data:
#         question_id = data['last_questions_id']
#         left_questions = data['questions']
#     answer = callback_query.data[4:]
#     question = get_question_info(question_id)
#     correct_answer = get_question_correct_answer(question['options'])
#     if answer == correct_answer:
#         await bot.send_message(callback_query.from_user.id, ':checkПравильно:check')
#         async with state.proxy() as data:
#             data['score'] += question['weight']
#     else:
#         await bot.send_message(callback_query.from_user.id, '😭Неправильно😭')
#     if left_questions:
#         async with state.proxy() as data:
#             question = data['questions'].pop(0)
#             data['last_questions_id'] = question['id']
#         options = [option['text'] for option in question['options']]
#         keyboard = generate_inline_keyboard(options)
#         await bot.send_message(callback_query.from_user.id, question['task_text'], reply_markup=keyboard)
#     else:
#         async with state.proxy() as data:
#             score = data['score']
#             quiz_id = data['quiz_id']
#         save_user_result(callback_query.from_user.id, quiz_id, score)
#         user_level = get_user_level(score)
#         user_id = callback_query.from_user.id
#         set_user_level(user_level, user_id)
#         await bot.send_message(user_id, f'Тест завершено. У вас {score} балов')
#         await bot.send_message(user_id, f'Ваш уровень: {LEVELS.get(user_level)}')
#
#
# def get_question_correct_answer(options: List[Dict]) -> int:
#     for option in options:
#         if option['is_correct'] == 1:
#             return option['text']
#
#
# @dp.message_handler(commands=['start'])
# async def command_start(message: types.Message):
#     if register_user(message.from_user.id, message.from_user.username):
#         await message.answer(t.greetings, reply_markup=con.Main_menu)
#     else:
#         await message.answer(t.greetings, reply_markup=con.Main_menu)
#
#
# # ----------------------------------- main menu handler ----------------------------------------#
#
# def generate_payment_keyboard(bill_id: int) -> InlineKeyboardMarkup:
#     check_button = InlineKeyboardButton('Проверить оплату', callback_data=f'check_pay/{bill_id}')
#     cancel_button = InlineKeyboardButton('Отменить оплату', callback_data=f'cancel_pay/{bill_id}')
#     keyboard = InlineKeyboardMarkup(row_width=2).add(check_button, cancel_button)
#
#     return keyboard
#
#
# # @dp.message_handler(text='Оплатить обучение💵')
# # async def process_pay_command(message: types.Message):
# #     await bot.send_message(message.from_user.id, 'Платеж генерируется')
# #     expired = datetime.now() + timedelta(minutes=10)
# #     new_bill = await p2p.bill(amount=140, expiration=expired)
# #     reply_keyboard = generate_payment_keyboard(new_bill.bill_id)
# #     await bot.send_message(message.from_user.id, f'Ссылка для оплаты: \n {new_bill.pay_url}',
# #                            reply_markup=reply_keyboard)
#
# @dp.callback_query_handler(lambda c: c.data and c.data.startswith('check_pay'))
# async def check_payment(callback_query: types.CallbackQuery):
#     bill_id = callback_query.data.split('/')[1]
#     status = await p2p.check(bill_id=bill_id)
#     print(status)
#     status = status.status
#     print(status)
#     if status == 'PAID':
#         await bot.send_message(callback_query.from_user.id, 'oplaceno')
#
#
# # l= ['Beginner(A1)', 'Pre-Intermediate(A2)', 'Intermediate(B1)', 'Upper-Intermediate(B2)']
#
# # @dp.message_handler(lambda message: message.text and message.text[-3:-1:] in ['A1', 'A2', 'B1', 'B2'])
# # @check_subscriptions
# # async def subscription_menu(message: types.Message):
#
# @dp.message_handler()
# async def process_start_command(message: types.Message):
#     if message.text == 'Программа работы🎓':
#         await message.reply("Здесь блять вся теория ", reply_markup=con.lvl_menu)
#     elif message.text == 'Контакты☎️':
#         await bot.send_message(message.from_user.id, t.developers)
#     elif message.text == 'Ознакомиться с ботом👀':
#         await message.answer("Отправляю видео:", reply_markup=con.Main_menu)
#     elif message.text == 'Main Menu🏠':
#         await message.answer("Выберите опцию: ", reply_markup=con.Main_menu)
#     elif message.text == 'Информация о курсеℹ':
#         await message.answer("Отправляю файл:", reply_markup=con.Main_menu)
#         await bot.send_document(message.chat.id, ('A1_all.pdf', A1))
#     elif message.text == 'Оплатить обучение💵':
#         await message.answer('Чтобы лалаалалалала Тут егор напише', reply_markup=con.payment_keyboard)
#     elif message.text == 'Назад':
#         await message.answer("Выберите опцию: ", reply_markup=con.lvl_menu)
#     if message.text == 'Beginner(A1)👶':
#         await message.answer("Программа работы:", reply_markup=con.MenuA1)
#     elif message.text == 'Pre-Intermediate(A2)🧒':
#         await message.answer("Программа работы:", reply_markup=con.MenuA2)
#     elif message.text == 'Intermediate(B1)🧑‍🎓':
#         await message.answer("Программа работы:", reply_markup=con.MenuB1)
#     elif message.text == 'Upper-Intermediate(B2)🧙':
#         await message.answer("Программа работы:", reply_markup=con.MenuB2)
#     elif message.text == 'Test (id)':  # Блядь. Мають бути тестові кнопки, на каждій кнопкі команда /test 1 або /test 2 або /test 3
#         await message.reply("Tests", reply_markup=con.Test_menu)
#         print(con.Test_menu)
#     if message.text == 'Grammar(B2)':
#         await message.reply("Программа работы Grammar(B2):", reply_markup=con.B2_GrammarFull)
#     if message.text == 'Reading(B2)':
#         await message.reply("Программа работы Reading(B2):", reply_markup=con.B2_ReadingFull)
#     if message.text == 'Listening(B2)':
#         await message.reply("Программа работы Listening(B2):", reply_markup=con.B2_ListeningFull)
#     if message.text == 'Vocabulary(B2)':
#         await bot.send_document(message.chat.id, ('A1_all.pdf', A1))
#     if message.text == 'Grammar(B1)':
#         await message.reply("Программа работы Grammar(B1):", reply_markup=con.B1_GrammarFull)
#     if message.text == 'Reading(B1)':
#         await message.reply("Программа работы Reading(B1):", reply_markup=con.B1_ReadingFull)
#         # await message.answer("https://telegra.ph/Topic-1-A-Traditional-Wedding-07-15")
#     if message.text == 'Listening(B1)':
#         await message.answer("Программа работы Listening(B1):", reply_markup=con.B1_ListeningFull)
#     if message.text == 'Vocabulary(B1)':
#         await bot.send_document(message.chat.id, ('A1_all.pdf', A1))
#     if message.text == 'Grammar(A2)':
#         await message.reply("Программа работы Grammar(A2):", reply_markup=con.A2_GrammarFull)
#     if message.text == 'Reading(A2)':
#         await message.reply("Программа работы Reading(A2):", reply_markup=con.A2_ReadingFull)
#     if message.text == 'Listening(A2)':
#         await message.reply("Программа работы Listening(A2):", reply_markup=con.A2_ListeningFull)
#     if message.text == 'Vocabulary(A2)':
#         await bot.send_document(message.chat.id, ('A1_all.pdf', A1))
#     if message.text == 'Grammar(A1)':
#         await message.reply("Программа работы Grammar(A1):", reply_markup=con.A1_GrammarFull)
#     if message.text == 'Reading(A1)':
#         await message.reply("Программа работы Reading(A1):", reply_markup=con.A1_ReadingFull)
#     if message.text == 'Listening(A1)':
#         await message.reply("Программа работы Listening(A1):", reply_markup=con.A1_ListeningFull)
#     if message.text == 'Vocabulary(A1)':
#         await bot.send_document(message.chat.id, ('A1_all.pdf', A1))
#     # if message.text == 'Grammar(B2)':
#     #     await message.reply("Программа работы Grammar(B2):", reply_markup=con.A2_GrammarFull)
#     # if message.text == 'Reading(B2)':
#     #     await message.reply("Программа работы Reading(B2):", reply_markup=con.A2_ReadingFull)
#     # if message.text == 'Listening(B2)':
#     #     await message.reply("Программа работы Listening(B2):", reply_markup=con.A2_ListeningFull)
#     # if message.text == 'Vocabulary(B2)':
#     #     await bot.send_document(message.chat.id, ('A1_all.pdf', A1))
#     # keyboard A1
#
#
# # ----------------------------------- main menu handler ----------------------------------------#
#
# async def generate_payment(amount: int) ->
#
#
# def check_existing_subscription(func):
#     async def wrapper(callback_query: types.CallbackQuery):
#         user_id = callback_query.from_user.id
#         user_subscriptions = get_user_subscriptions(user_id)
#         request_subscription_id = int(callback_query.data.split('/')[1])
#         request_subscription_name = LEVELS.get(request_subscription_id, '')
#         if request_subscription_name in user_subscriptions:
#             return await bot.send_message(callback_query.from_user.id, 'Єта подписка уже куплена')
#         return await func(callback_query)
#
#     return wrapper
#
#
# @dp.callback_query_handler(lambda c: c.data and c.data.startswith('pay'))
# @check_existing_subscription
# async def process_listening_command(callback_query: types.CallbackQuery):
#     subscription_id = int(callback_query.data.split('/')[1])
#     listening_info = get_listening_info(listening_id)  # tuple(0 - audio_file path, 1 - instant_view_url)
#     audio_file_path = listening_info[0]
#     text_url = listening_info[1]
#     await bot.send_message(callback_query.from_user.id, text_url)
#     file_obj = read_file(audio_file_path)
#     await bot.send_voice(callback_query.from_user.id, file_obj)
#
#
# AnyStr = TypeVar('AnyStr', bytes, str)
#
#
# def read_file(filepath: str) -> AnyStr:
#     with open(filepath, 'rb') as file:
#         try:
#             result = file.read()
#             return result
#         except Exception as e:
#             print(e)
#             return ''
#
#
# @dp.callback_query_handler(lambda c: c.data and c.data.startswith('Listening'))
# async def process_listening_command(callback_query: types.CallbackQuery):
#     listening_id = int(callback_query.data.split('/')[1])
#     listening_info = get_listening_info(listening_id)  # tuple(0 - audio_file path, 1 - instant_view_url)
#     audio_file_path = listening_info[0]
#     text_url = listening_info[1]
#     await bot.send_message(callback_query.from_user.id, text_url)
#     file_obj = read_file(audio_file_path)
#     await bot.send_voice(callback_query.from_user.id, file_obj)
#
#
# # Reading
# @dp.callback_query_handler(lambda c: c.data and c.data.startswith('Topic'))
# async def process_reading_command(callback_query: types.CallbackQuery):
#     topic_id = int(callback_query.data.split('/')[1])
#     topic_url = get_topic_url(topic_id)
#     await bot.send_message(callback_query.from_user.id, topic_url)
#
#
# @dp.callback_query_handler(lambda c: c.data and c.data.startswith('Get'))
# async def process_konspekt_command(callback_query: types.CallbackQuery):
#     await bot.send_document(callback_query.from_user.id, ('A1_all.pdf', A1))
#
#
# if __name__ == '__main__':
#     executor.start_polling(dp)
#
