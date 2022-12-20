from modes.mode import Number_mode, Candy_amount
from aiogram import types
from create_bot import bot
from src.config import mode, get_candy_count, set_candy_count
import service.game_service as gs


async def game(message: types.Message):
    global mode
    mode = Number_mode.GAME
    candy_count: int = get_candy_count()
    candy_count -= int(message.text)
    set_candy_count(candy_count)
    if gs.is_win(candy_count):
        await bot.send_message(message.chat.id, f'Поздравляю. Надеюсь, что было сложно')
        await bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEG5lxjoQ5V5YFQZ1H0NaI1iQyqitEh1wACGxoAAkgz0Ur028ckVCAhiCwE")
        mode = Number_mode.DEFAULT.value
        candy_count = Candy_amount.FEW.value
        return
    await bot.send_message(message.chat.id, f'Есть тема распилить {candy_count} конфет.')
    bot_candy_amount: int = gs.get_candy_amount(candy_count)
    new_value: int = int(get_candy_count())-bot_candy_amount
    set_candy_count(new_value)
    candy_count = new_value
    if gs.is_win(candy_count):
        await bot.send_message(message.chat.id, f'Я победил. Это было легко')
        await bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEG5l5joQ8hSd25BqWZDeV4Ft2VqUVzbwAChxoAAr1NOEq9sPjp-eU-CSwE")
        mode = Number_mode.DEFAULT.value
        candy_count = Candy_amount.FEW.value
        return
    await bot.send_message(message.chat.id, f'Я набрал {bot_candy_amount}. Осталось {candy_count}')
    await bot.send_message(message.chat.id, f'Твоя очередь набирать конфеты. Накалякай количество')
