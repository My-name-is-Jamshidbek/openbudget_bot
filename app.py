from aiogram import types
from loader import dp
from config import ADMIN_ID
from aiogram.dispatcher.filters import CommandStart, CommandHelp
from states import Asosiy
from loader import bot
from aiogram.dispatcher import FSMContext
from replybuttons import keyboard_bekor_qilish
from inlinebuttons import keyboard_qodni_qayta_yuborish
from baza import baseadd, basebantek, basebanadd
from datetime import datetime
from functions import f1, qodniyuborish, qodnitasdiqlash
from variables import baza


# start
@dp.message_handler(CommandStart())
async def start(message: types.Message):
    # if str(message.from_user.id) == str(ADMIN_ID):
    #     await message.answer('salomadmin botga hush kelibsiz!', reply_markup=keyboard_admin_menu_1, )
    if True:
        await message.answer(
            f"Assalomu aleykum {message.from_user.full_name} botga xush kelibsiz!\nIltimos telefon raqmingizni namunadagidek yozing va jo'nating:\nNamuna: 991115678")
        baza[str(message.from_user.id)] = {}
        await Asosiy.tel_number.set()


@dp.message_handler(state=Asosiy.tel_number, content_types=types.ContentType.TEXT)
async def inputtelnumber(message: types.Message, state: FSMContext):
    m = str(message.text)
    result = f1(str(m))
    if result[0]:
        q = qodniyuborish(m)
        if q[0]:
            await message.answer(result[1], reply_markup=keyboard_bekor_qilish)
            await state.update_data(telefonraqam=m)
            token = q[1]
            baza[str(message.from_user.id)][m] = {
                'qayta_yuborishlar': 3,
                'qayta_terishlar': 3,
                'raqam_vaqti': datetime.now(),
                'token': token
            }
            await Asosiy.sms_qod.set()
        else:
            await message.answer(q[1])
            await message.answer('Telefon raqamingizni kiritishingiz mumkin!\nNamuna:912779693')
            await Asosiy.tel_number.set()
    else:
        await message.answer(result[1])
        await message.answer('Telefon raqamingizni kiritishingiz mumkin!\nNamuna:912779693')
        await Asosiy.tel_number.set()


@dp.message_handler(state=Asosiy.sms_qod, content_types=types.ContentType.TEXT)
async def inputcode(message: types.Message, state: FSMContext):
    m = message.text
    data = await state.get_data()
    tel_raqami = data.get('telefonraqam')
    token = baza[str(message.from_user.id)][tel_raqami]['token']
    if m == 'Qodni qayta yuborish':
        if int(str(datetime.now() - baza[str(message.from_user.id)][tel_raqami]['raqam_vaqti'])[2:4]) >= 2:
            if baza[str(message.from_user.id)][tel_raqami]['qayta_yuborishlar'] <= 0:
                await message.answer('Bu raqam bloklandi!',reply_markup=types.ReplyKeyboardRemove())
                a = basebanadd(tel_raqami)
                if a is not True: print('qodni qayta yuborish basebanadd false')
                await Asosiy.tel_number.set()
            else:
                a = qodniyuborish(tel_raqami)
                if a[0]:
                    await message.answer('Qod qayta yuborildi iltimos uni 2 daqiqa ichida kiriting!')
                    baza[str(message.from_user.id)][tel_raqami]['qayta_yuborishlar'] -= 1
                    baza[str(message.from_user.id)][tel_raqami]['qayta_terishlar'] = 3
                    baza[str(message.from_user.id)][tel_raqami]['token'] = a[1]
                    await Asosiy.sms_qod.set()
                else:
                    await message.answer(a[1],reply_markup=types.ReplyKeyboardRemove())
                    await Asosiy.tel_number.set()
        else:
            await message.answer('Qod yuborilganiga hali 2 daqiqa bo`lmadi iltimos kuting va qodni yuboring!')
            await Asosiy.sms_qod.set()
    elif m == 'Bekor qilish':
        await message.answer('Bekor qilindi!',reply_markup=types.ReplyKeyboardRemove())
        await message.answer('Telefon raqamingizni kiritishingiz mumkin!\nNamuna:912779693')
        await Asosiy.tel_number.set()
    else:
        a = qodnitasdiqlash(tel_raqami, m, token)
        if str(a)=='0':
            await message.answer('Sayt bilan bog`liq muammo yuz berdi!\nIltimos keyinroq urinib koring!',reply_markup=types.ReplyKeyboardRemove())
            await message.answer('Telefon raqamingizni kiritishingiz mumkin!\nNamuna:912779693')
            await Asosiy.tel_number.set()
        elif str(a)=='block':
            await message.answer('Tabriklaymiz siz muvaffaqiyatli ro`yxatdan o`tdingiz 3 daqiqadan keyin ovozingiz hisobga olinadi!',reply_markup=types.ReplyKeyboardRemove())
            await message.answer('Telefon raqamingizni kiritishingiz mumkin!\nNamuna:912779693')
            await Asosiy.tel_number.set()
        elif a:
            await message.answer('Tabriklaymiz siz muvaffaqiyatli ro`yxatdan o`tdingiz',reply_markup=types.ReplyKeyboardRemove())
            await message.answer('Telefon raqamingizni kiritishingiz mumkin!\nNamuna:912779693')
            baseadd(str(message.from_user.id), str(message.chat.id), tel_raqami)
            del baza[str(message.from_user.id)][tel_raqami]
            await Asosiy.tel_number.set()
        else:
            await message.answer('Siz tergan parol noto`g`ri iltimos tekshirib qayta tering!')
            baza[str(message.from_user.id)][tel_raqami]['qayta_terishlar'] -= 1
            if baza[str(message.from_user.id)][tel_raqami]['qayta_terishlar'] <= 0:
                await message.answer('3 marotaba xato terishlarddan keyin raqamingiz bloklandi!',reply_markup=types.ReplyKeyboardRemove())
                a = basebanadd(tel_raqami)
                if a is not True: print('else basebanadd false line 91')
                await message.answer('Telefon raqamingizni kiritishingiz mumkin!\nNamuna:912779693')
                await Asosiy.tel_number.set()
            else:
                await Asosiy.sms_qod.set()


# yordam
@dp.message_handler(CommandHelp())
async def els(message: types.Message):
    await message.answer(f"yordam {message.from_user.full_name}")
