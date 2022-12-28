from aiogram.utils import executor
from create_bot import dp

from handlers import location_handler, sticker_handler, voice_handler, text_handler, query_handler, other, tic_tac_toe_handler

tic_tac_toe_handler.register_handler_query(dp)
location_handler.register_handler_location(dp)
sticker_handler.register_handler_sticker(dp)
voice_handler.register_handler_voice(dp)
query_handler.register_handler_query(dp)
text_handler.register_handler_text(dp)
other.register_handler_commands(dp)


executor.start_polling(dp, skip_updates=True)
