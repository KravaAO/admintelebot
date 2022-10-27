from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from config import TOKEN_API

HELP_COMMAND = """
<b>/help</b> - <em>List commands</em>
<b>/start</b> - <em>Start Bot</em>
<b>/description</b> - <em>my possibilities</em> 
"""

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard = True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/description')
kb.add(b1).insert(b2)

#@dp.message_handler()
#async def echo(message: types.Message):
#    await message.send.answer(chat_id = message.from_user)

@dp.message_handler(commands = ['help'])
async def help_command(message: types.Message):
    await message.reply(text = HELP_COMMAND,
                        parse_mode = "HTML")
    await message.delete()

@dp.message_handler(commands = ['start'])
async def help_command(message: types.Message):
    await message.reply(text = "welcome to Bot",
                        parse_mode = "HTML",
                        reply_markup = kb)
    await message.delete()

@dp.message_handler(commands = ['description'])
async def description_command(message: types.Message):
    await message.reply(text = "I can nothing, sorry",
                        parse_mode = "HTML",
                        reply_markup = kb)

if __name__ == "__main__":
    print('vrode working')
    executor.start_polling(dp, skip_updates = True)
