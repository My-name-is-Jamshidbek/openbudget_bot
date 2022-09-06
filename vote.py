import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def vote(phone_number, kod, token):
    phone_number = '998'+str(phone_number)
    try:
    # phone_number = "998992231638"
    # kod = "546546"
    # token = "TFVFBK46GJT5EJU3IILDZXWRZLCSLRQA"
        votes = requests.post('https://admin.openbudget.uz/api/v1/user/temp/vote/',
                              data={'phone': phone_number, 'otp': kod, 'token': token,
                                    'application': "123288"}, verify=False)
    except: return False
    try:a = votes.json()
    except:
        return 'rt'
    try:
        a = a.get('detail')
        return a
    except:return False
# except:
#     return False

#   agar parol xato bo'lsa 'Invalid code' shu xabar qaytadi. JSON Key and Value -> {'detail': 'Invalid code'}
