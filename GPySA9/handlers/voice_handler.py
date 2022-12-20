from modes.mode import Number_mode
from aiogram import types, Dispatcher
from create_bot import dp, bot


@dp.message_handler(content_types=['voice'])
async def message_reply_voice(message: types.Message):
    global mode
    mode = Number_mode.DEFAULT.value
    await bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEGqV5jiyw2iRSTw6bH788UxRAvS6u5uAACJxgAApd54UvWARYS3sXfTysE")


def register_handler_voice(dp: Dispatcher):
    dp.register_message_handler(
        register_handler_voice, content_types=['voice'])
