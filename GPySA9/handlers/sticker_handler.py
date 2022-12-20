from modes.mode import Number_mode
from aiogram import types, Dispatcher
from create_bot import bot


async def message_reply(message: types.Message):
    global mode
    mode = Number_mode.DEFAULT.value
    await bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEGqV5jiyw2iRSTw6bH788UxRAvS6u5uAACJxgAApd54UvWARYS3sXfTysE")


def register_handler_sticker(dp: Dispatcher):
    dp.register_message_handler(message_reply, content_types=['sticker'])
