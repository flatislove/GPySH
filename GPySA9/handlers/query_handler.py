from aiogram import types, Dispatcher
from create_bot import bot
from src.config import complexity, mode, candy_count, set_candy_count, get_candy_count, set_complexity, get_comlexity
import service.service_db as dbs
import service.service as s
from modes.mode import Complexity, Candy_amount


async def callback_inline(call: types.CallbackQuery):
    global mode
    global complexity
    global candy_count
    if call.data == 'Привет':
        await bot.send_sticker(call.from_user.id, "CAACAgIAAxkBAAEGrjtjjNUJLFyOJRT_L3XX8H07O9gQJQACaRcAAqnJOUoBu84B21ly6isE")
        await bot.send_message(call.from_user.id, "И тебе привет)")
    elif call.data == 'Как дела?':
        await bot.send_sticker(call.from_user.id, "CAACAgIAAxkBAAEGrj1jjNUe36tGdpHA7CsEUJYY5RMr9QAC-BEAAoPF6UvVPQGi07k3jSsE")
        await bot.send_message(call.from_user.id, "А у тебя?")
    elif call.data.startswith('team'):
        team = call.data.split(" ")
        id_team, name_team = team[1], team[2]
        await bot.send_message(call.from_user.id, f"Состав {name_team}:", reply_markup=s.players_to_markups(id_team))
    elif call.data.startswith('player'):
        p = dbs.get_player_by_id(call.data.split(" ")[1])
        await bot.send_message(call.from_user.id, s.show_player_details(p))
    elif call.data.startswith('complexity='):
        if call.data == "complexity=EASY":
            set_complexity(Complexity.EASY.name)
            await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
            await bot.send_message(call.from_user.id, "Выбран низкий уровень сложности")
            await call.answer('Главное, чтоб по кайфу', show_alert=True)
        elif call.data == "complexity=HARD":
            set_complexity(Complexity.HARD.name)
            await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
            await bot.send_message(call.from_user.id, "Выбран высокий уровень сложности")
            await call.answer('Не твой уровень, дорогой', show_alert=True)
        await bot.send_message(call.from_user.id, "Выбери количество конфет", reply_markup=s.get_markup_game_candy_amount())
    elif call.data.startswith('amount='):
        if call.data == "amount=150":
            set_candy_count(Candy_amount.FEW.value)
            await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
            candy_count = get_candy_count()
        if call.data == "amount=500":
            set_candy_count(Candy_amount.NORMAL.value)
            await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
            candy_count = get_candy_count()
        if call.data == "amount=1000":
            set_candy_count(Candy_amount.MANY.value)
            await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
            candy_count = get_candy_count()
        await bot.send_message(call.from_user.id, f"Установлено количество конфет {candy_count}")
        await bot.send_sticker(call.from_user.id, "CAACAgIAAxkBAAEG5SpjoMBL1FOK8DHESMT38J5108i5VwAC5xIAAu-S6EvY9IfRXkZ-LCwE")
        await bot.send_message(call.from_user.id, f'Есть тема распилить {candy_count} конфет.\n Набирать можно от 1 до 28 включительно')
        await bot.send_message(call.from_user.id, f"Ходи первым) Подарок на Новый год.")
        if get_comlexity() == "HARD":
            await call.answer('Ты все равно проиграешь', show_alert=False)


def register_handler_query(dp: Dispatcher):
    dp.register_callback_query_handler(callback_inline, types.CallbackQuery)
