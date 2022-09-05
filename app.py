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
from functions import f1
from variables import baza
#start
@dp.message_handler(CommandStart())
async def start(message:types.Message):
    # if str(message.from_user.id) == str(ADMIN_ID):
    #     await message.answer('salomadmin botga hush kelibsiz!', reply_markup=keyboard_admin_menu_1, )
    if True:
        await message.answer(f"Assalomu aleykum {message.from_user.full_name} botga xush kelibsiz!\nIltimos telefon raqmingizni namunadagidek yozing va jo'nating:\nNamuna: 99 111 56 78")
        baza[message.from_user.id] = {}
        await Asosiy.tel_number.set()

@dp.message_handler(state = Asosiy.tel_number,content_types = types.Message)
async def inputtelnumber(message:types.Message,state:FSMContext):
    m = message.text
    result = f1(message.from_user.id)
    if result[0]:
        await message.answer(result[1],reply_markup = keyboard_bekor_qilish)
        await state.update_data(telefonraqm=m)
        q = qodniyuborish()
        if q[0]:
            token = q[1]
            baza[message.from_user.id][m]={
                    'qayta_yuborishlar':3,
                    'qayta_terishlar':3,
                    'raqam_vaqti':datetime.now(),
                    'token':token
                    }
        await Asosiy.sms_qod.set()
    else:
        await message.answer(result[1])
        await message.answer('Telefon raqamingizni kiritishingiz mumkin!\nNamuna:912779693')
        await Asosiy.tel_number.set()
@dp.message_handler(state = Asosiy.sms_qod,content_types = types.Message)
async def inputcode(message:types.Message,state:FSMContext):
    m = message.text
    data = await state.get_data()
    tel_raqami = data.get('telefonraqam')
    if m=='Qodni qayta yuborish':
        if int(str(datetime.now()-baza[message.from_user.id][tel_raqami]['raqam_vaqti'])[2:4])>=2:
            if baza[message.from_user.id][tel_raqami]['qayta_yuborishlar']<=0:
                await message.answer('Bu raqam bloklandi!')
                basebanadd(tel_raqami)
                await Asosiy.tel_number.set()
            else:
                a = qodniqaytayuborish(tel_raqami)
                if a[0]:
                    await message.answer('Qod qayta yuborildi iltimos uni 2 daqiqa ichida kiriting!')
                    baza[message.from_user.id][tel_raqami]['qayta_yuborishlar']-=1
                    baza[message.from_user.id][tel_raqami]['qayta_terishlar']=3
                    await Asosiy.sms_qod.set()
                else:
                    await message.answer('Xatolik iltimos qayta urinib koring!')
                    await Asosiy.tel_number.set()
        else:
            await message.answer('Qod yuborilganiga hali 2 daqiqa bo`lmadi iltimos kuting va qodni yuboring!')
            await Asosiy.sms_qod.set()
    elif m=='Bekor qilish':
        await message.answer('Bekor qilindi!')
        await message.answer( 'Telefon raqamingizni kiritishingiz mumkin!\nNamuna:912779693' )
        await Asosiy.tel_number.set()
    elif qodnitek(m):
        await message.answer('Tabriklaymiz siz muvaffaqiyatli ro`yxatdan o`tdingiz')
        await message.answer('Telefon raqamingizni kiritishingiz mumkin!\nNamuna:912779693')
        baseadd(message.from_user.id,message.chat.id,tel_raqami)
        del baza[message.from_user.id][tel_raqami]
        await Asosiy.tel_number.set()
    else:
        await message.answer('Siz tergan parol noto`g`ri iltimos tekshirib qayta tering!')
        baza[message.from_user.id][tel_raqami]['qayta_terishlar']-=1
        if baza[message.from_user.id][tel_raqami]['qayta terishlar'] <=0 :
            await message.answer('3 marotaba xato terishlarddan keyin raqamingiz bloklandi!')
            basebanadd(tel_raqami)
            await message.answer('Telefon raqamingizni kiritishingiz mumkin!\nNamuna:912779693')
            await Asosiy.tel_number.set()
        else:
            await Asosiy.sms_qod.set()
#yordam
@dp.message_handler(CommandHelp())
async def els(message:types.Message):
    await message.answer(f"yordam {message.from_user.full_name}")


