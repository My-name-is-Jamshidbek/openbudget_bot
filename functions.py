from baza import basetek, basebantek
from send import send
from vote import vote
def f1(telefon_raqam):
	if len(telefon_raqam) == 7:
		try:
			int(telefon_raqam)
			if basetek(telefon_raqam):
				if basebantek(telefon_raqam):
					return [True,'Iltimos telefon raqamingizga yetob borgan qodni 2 daqiqa ichida kiriting!']
				else:return [False,'Kechirasiz bu raqam BAN qilingan!']
			else:return[False,'Bu raqam oldin ro`yxatdan o`tgan!']
		except:
			return [False, 'Iltimos raqamni to`g`ri kiriting!']
	else:return [False, 'Iltimos raqamni to`gri kiriting!']

def qodniyuborish(tel):
	a = send(tel)
	if 'This number was used to vote' in a[1] and a[0] is not True:
		return [False,'Bu raqam oldin ro`yxatdan o`tgan!']
	elif 'Incorrect phone number' in a[1] and a[0] is not True:
		return [False, 'Bu raqam noto`g`ri!']
	elif a[0]:
		return [True,a[1]]
def qodnitasdiqlash(tel,kod,token):
	a = vote(tel,kod,token)
	if 'Invalid code' in str(a):
		return False
	else:return True