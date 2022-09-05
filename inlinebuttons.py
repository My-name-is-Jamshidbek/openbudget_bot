from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def keyboard_qodni_qayta_yuborish(telefon_raqam,user_id):
	b=InlineKeyboardMarkup()
	b.add(InlineKeyboardButton(text='Qayta yuborish',callback_data=f"qayta_yuborish_{telefon_raqam}_{user_id}"),)
	return b