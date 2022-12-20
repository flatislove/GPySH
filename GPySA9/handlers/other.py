from aiogram import types, Dispatcher
from create_bot import dp, bot
from src.config import mode
import service.service as s
import service.service_db as dbs
from modes.mode import Number_mode


@dp.message_handler(commands=['start'])
async def button_message_geo(message: types.Message):
    global mode
    mode = Number_mode.DEFAULT.value
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='👁‍🗨 Что могу?', callback_data="what?"),
               types.InlineKeyboardButton(
                   text="💾 Ссылка на гит с кодом", callback_data="gitcode"),
               types.InlineKeyboardButton(text="💲 Конвертер BYN/KZT", callback_data="tenge_is"))
    markup.add(types.KeyboardButton(text="🔅 Что по погоде?", request_location=True),
               types.InlineKeyboardButton(text="🎲 Игра \"Распили конфеты\"", callback_data="game_mode"))
    await bot.send_message(message.chat.id, f"Погнали, {message.from_user.username}!", reply_markup=markup)
    await bot.send_sticker(message.chat.id, sticker='CAACAgIAAxkBAAEGqV5jiyw2iRSTw6bH788UxRAvS6u5uAACJxgAApd54UvWARYS3sXfTysE')


@dp.message_handler(commands=['info'])
async def get_info_messages(message: types.Message):
    global mode
    mode = Number_mode.DEFAULT.value
    await bot.send_message(message.from_user.id, "Команды", reply_markup=s.teams_to_markups())


@dp.message_handler(commands=['add_player'])
async def firstname_handler(message: types.Message):
    await bot.send_message(message.chat.id, f"Еще не реализовано.")
    # global mode
    # mode = Number_mode.DEFAULT.value
    # firstname = await bot.send_message(message.chat.id, 'Введите имя',)
    # await lastname_handler(firstname)


async def lastname_handler(message: types.Message):
    firstname = message.text
    lastname = await bot.send_message(message.chat.id, f"Ваше имя {firstname}. Введите фамилию")
    await bot.register_next_step_handler(lastname, team_handler, firstname)


async def team_handler(message: types.Message, firstname):
    lastname = message.text
    team_id = bot.send_message(
        message.chat.id, f"Введите id номер команды", reply_markup=s.teams_to_markups_add())
    await bot.register_next_step_handler(team_id, number_handler, firstname, lastname)


async def number_handler(message: types.Message, firstname, lastname):
    team_id = message.text
    number = bot.send_message(message.chat.id, f"Введите игровой номер")
    await bot.register_next_step_handler(number, position_handler, firstname, lastname, team_id)


async def position_handler(message: types.Message, firstname, lastname, team_id):
    number = message.text
    position_id = bot.send_message(
        message.chat.id, f"Введите id номер позиции", reply_markup=s.positions_to_markups_add())
    await bot.register_next_step_handler(position_id, summary_handler, firstname, lastname, team_id, number)


async def summary_handler(message: types.Message, firstname, lastname, team_id, number):
    position_id = message.text
    res = dbs.add_player(firstname, lastname, team_id, number, position_id)
    if res != -1:
        await bot.send_message(message.chat.id, f'Игрок успешно добавлен')
    else:
        await bot.send_message(message.chat.id, f'Не удалось добавить игрока')


def register_handler_commands(dp: Dispatcher):
    dp.register_message_handler(button_message_geo, commands=['start'])
    dp.register_message_handler(get_info_messages, commands=['Info'])
    dp.register_message_handler(firstname_handler, commands=['add_player'])
