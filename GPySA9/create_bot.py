from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from src.config import token

bot = Bot(token=token)
dp = Dispatcher(bot)
