'''verifica se o numero e valido de onde é'''
import phonenumbers
from phonenumbers import geocoder


phone_number = phonenumbers.parse('+551140028922')  # SBT
print(geocoder.description_for_number(phone_number, 'pt'))

phone_number2 = phonenumbers.parse('+16502230000')  # GooglePlax?
print(geocoder.description_for_number(phone_number2, 'pt'))
