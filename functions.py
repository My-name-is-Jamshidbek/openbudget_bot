from baza import basetek, basebantek

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