import time

from baza import basetek, basebantek
from send import send
from vote import vote


def f1(telefon_raqam):
    if len(telefon_raqam) == 9:
        try:
            int(telefon_raqam)
            if basetek(telefon_raqam):
                if basebantek(telefon_raqam):
                    return [True, 'Iltimos telefon raqamingizga yetob borgan qodni 2 daqiqa ichida kiriting!']
                else:
                    return [False, 'Kechirasiz bu raqam BAN qilingan!']
            else:
                return [False, 'Bu raqam oldin ro`yxatdan o`tgan!']
        except:
            return [False, 'Iltimos raqamni to`g`ri kiriting!']
    else:
        return [False, 'Iltimos raqamni to`gri kiriting!']


def qodniyuborish(tel):
    a = str(send(tel))
    if 'This number was used to vote' == a:
        return [False, 'Bu raqam oldin ro`yxatdan o`tgan!']
    elif 'Incorrect phone number' == a:
        return [False, 'Bu raqam noto`g`ri!']
    elif a == str(False):
        return [False, 'Sayt bilan bog`liq muammo yuz berdi!\nIltimos keyinroq urinib koring!']
    else:
        return [True, a]


def qodnitasdiqlash(tel, kod, token):
    a = vote(tel, kod, token)
    if 'Invalid code' == str(a):
        return False
    elif str(a) == str(False):
        return 0
    elif str(a)=='rt':
        return 'block'
    else:
        return True
