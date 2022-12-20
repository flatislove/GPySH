from modes.mode import Number_mode
from aiogram import types, Dispatcher
from create_bot import bot, dp
from src.config import candy_count, mode
import re
import service.service as s
import model.currency as cur
from handlers.game_handler import game


async def message_reply(message: types.Message):
    global mode
    global candy_count
    if message.text.lower().strip() == "привет":
        mode = Number_mode.DEFAULT.name
        await bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEGrjtjjNUJLFyOJRT_L3XX8H07O9gQJQACaRcAAqnJOUoBu84B21ly6isE")
        await bot.send_message(message.chat.id, "И тебе привет)")
    elif message.text.lower() == "как дела?" or message.text.lower() == "как дела":
        mode = Number_mode.DEFAULT.name
        await bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEGrj1jjNUe36tGdpHA7CsEUJYY5RMr9QAC-BEAAoPF6UvVPQGi07k3jSsE")
        await bot.send_message(message.chat.id, "А у тебя?")
    elif message.text == "💲 Конвертер BYN/KZT":
        mode = Number_mode.CONVERTER.name
        await bot.send_message(message.from_user.id, f"Введите сумму в BYN")
    elif message.text == "💾 Ссылка на гит с кодом":
        mode = Number_mode.DEFAULT.name
        await bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEGrktjjNjTDAJuWz_MA0tEAAGZoo_YZa4AApAZAAKn6UFKS0BguZTHflkrBA")
        count = await bot.send_message(message.chat.id, "https://github.com/flatislove/derby_bot")
    elif message.text == "👁‍🗨 Что могу?":
        mode = Number_mode.DEFAULT.name
        await bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEGrk1jjNkBgQhb796wZ-vwpnPkzMMmOgACRiAAAkRbyErWG5mnIxS-aCsE")
        await bot.send_message(message.chat.id, s.get_description(), reply_markup=s.answers_to_markups_add())
    elif message.text == "🎲 Игра \"Распили конфеты\"":
        mode = Number_mode.GAME.name
        await bot.send_message(message.chat.id, "Выбери сложность", reply_markup=s.get_markup_game_complex())
    elif (re.match("^[\d]+$", message.text) != None) and mode == "CONVERTER":
        await get_count_tenge(message)
    elif (re.match("^[\d]+$", message.text) != None) and mode == "GAME" and 0 < int(message.text) < 29:
        mode = Number_mode.GAME.name
        await game(message)
    else:
        await bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEGrj9jjNWr6sgP5-edjkWOZnDoE9FwkwACPhYAAiR2OUhOF80tn_t59CsE")
        await bot.send_message(message.chat.id, "Такой команды нет)")


def register_handler_text(dp: Dispatcher):
    dp.register_message_handler(message_reply, content_types=['text'])


async def get_count_tenge(message: types.Message):
    global mode
    mode = Number_mode.CONVERTER.name
    try:
        count_money = float(message.text)
    except Exception as ex:
        count_money = float(0)
    await bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEGqXdjiy8tTv-fqQJLo3OKf8-fiddXbgAC3BQAAnWf4EtIjabVCNG-PisE")
    await bot.send_message(message.chat.id, f"{count_money} BYN это {s.get_exchange_currency(cur.Currency.KZT.value,count_money)} KZT в тенге")
