from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import KEYBOARD as kb
from aiogram import Bot, types
import time
TOKEN = 'your_token'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("", reply_markup=kb.markup_big, disable_web_page_preview=True)

@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
    
 
    if msg.text == '///':
        while True:
            await msg.answer_sticker(r'sticker-id')
            await msg.answer_sticker(r'sticker-id')
            await msg.answer_sticker(r'sticker-id')
            time.sleep(3)


if __name__ == '__main__':
    executor.start_polling(dp)
