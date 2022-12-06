import logging
import math
import asyncio
import requests
from pprint import pprint as print
from aiogram import Bot, Dispatcher, executor, types
from obhavo import data
from googletrans import Translator
import asyncio

translator = Translator()
API_TOKEN = '5653922895:AAE4Vj-kAdKQRtcykleiclMf8yMTyye8obc'
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("🌥☁🌧🌨\n🌩⛅🌤🌪\n⛈🌦🌥🔆\n Ob-havo Bot\nXush Kelibsiz!!!")
    await asyncio.sleep(3)
    await message.answer("Ob-havosini bilmoqchi bo'layotgan joy nomini kiritng ✅:")

@dp.message_handler()
async def keldimal(message: types.Message):
    message_id = (await message.answer("Qidirilmoqda ...🚀")).message_id
    if not data(message.text):
        await bot.delete_message(chat_id=message.from_user.id, message_id=message_id)
        await message.answer("Bunday hudud Topilmadi ❌")
    baza = data(message.text)
    icon = baza["icon"]
    hudud = baza["joy"]
    dav = baza["dav"]
    ob = baza["ob"]
    word = translator.translate(ob, dest='uz').text
    gradus = baza["havo"]
    await bot.delete_message(chat_id=message.from_user.id, message_id=message_id)
    await message.reply("Ma'lumotlar Topildi ✅")
    await message.answer_photo(f"http://openweathermap.org/img/wn/{icon}@2x.png")
    await message.answer(f"1️⃣  Hudud 🌎 : {hudud},{dav}\n\n2️⃣ Harorat 🌡 : {math.floor(gradus)}°C\n\n3️⃣ Iqlim ☁ : {word.capitalize()}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)