from modes.mode import Number_mode
from aiogram import types, Dispatcher
import service.service as s
from create_bot import bot
from src.config import mode


async def message_reply_location(message: types.Message):
    global mode
    mode = Number_mode.DEFAULT.value
    if message.location is not None:
        weather = s.get_weather(message.location.latitude, message.location.longitude)
        await bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEGsdZjjePC0fBNe2w051trdGs9ApzAyAACmhUAAhjCOUoQthLkmEXldSsE")
        await bot.send_message(message.chat.id, f"Погода за окном такая:\n Температура {weather.get('temperature')} градусов\n Скорость ветра {weather.get('windspeed')}м/с\n")
        await bot.send_message(message.chat.id, f"Кстати, между Вами и офисом гугл {s.get_distance_between_points(message.location.latitude,message.location.longitude)} км")


def register_handler_location(dp: Dispatcher):
    dp.register_message_handler(
        message_reply_location, content_types=['location'])
