from aiogram import types, Dispatcher
from create_bot import bot
import service.service as s
import service.tic_tac_service as stic
from service.tic_tac_service import call_back_info


async def sell_callback_handler(call: types.CallbackQuery, callback_data: dict):
    if call.data.startswith("tXO:t_t_t="):
        arr_str: str = callback_data.get("t_b")
        arr_arr = stic.string_to_array(arr_str)
        cell = callback_data.get("c")
        arr: list = stic.mark_cell_user_action(cell, arr_arr)[1]
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=stic.get_sea_battle_field(arr))
        result = stic.check_win_or_end(arr)
        if result != None:
            if result == "Draw":
                await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
                await bot.send_message(call.from_user.id, "Ничья")
                return
            elif result in "XO":
                await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
                await bot.send_message(call.from_user.id, f"Победили {result}")
                return
        arr: list = stic.mark_cell_bot_action(arr)
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=stic.get_sea_battle_field(arr))
        result = stic.check_win_or_end(arr)
        if result != None:
            if result == "Draw":
                await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
                await bot.send_message(call.from_user.id, "Ничья")
                return
            elif result in "XO":
                await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
                await bot.send_message(call.from_user.id, f"Победили {result}")
                return


def register_handler_query(dp: Dispatcher):
    dp.register_callback_query_handler(
        sell_callback_handler, call_back_info.filter())
