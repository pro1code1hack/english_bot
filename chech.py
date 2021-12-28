from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN

import aiogram

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler(text=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


#----------------------------------- open files with (with) ----------------------------------------#
with open(r'C:\Users\Hacking\Desktop\B2_boy_bands.mp3', 'rb') as file:           # Путь к файлу который нужно прочесть
    A2 = file.read()

VOICE = A2

@dp.message_handler(commands=['voice'])
async def process_voice_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Отправляю аудио файл")
    await bot.send_voice(message.from_user.id, VOICE,
                         reply_to_message_id=message.message_id)




if __name__ == '__main__':
    executor.start_polling(dp)