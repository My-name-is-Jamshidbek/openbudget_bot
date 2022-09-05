import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def send(phone_number):
    key = '1da141ca67105af41fdbb4c0839124617c591c1d'
    phone = f'+{phone_number[0:3]} ({phone_number[3:5]}) {phone_number[5:8]}-{phone_number[8:10]}-{phone_number[10:12]}'
    r = requests.post('https://admin.openbudget.uz/api/v1/user/validate_phone/',
                      data={'key': key, 'phone': phone,
                            'application': "123288"}, verify='')
    response = r.json()
    try:
        return response['token']
    except:
        return response['detail']
#       agar ro'yhatdan o'tgan bo'lsa raqam 'This number was used to vote' shu habar qaytadi
#       agar raqam xato bo'lsa 'Incorrect phone number' shu xabar qaytadi


"+998 (99) 223-16-38"
print(send('99945999936'))

