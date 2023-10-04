import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobileNo = input("Enter phone number with country code (+xx xxxxxxxxxx): ")
mobileNo = phonenumbers.parse(mobileNo)
if phonenumbers.is_valid_number(mobileNo):
    print("Region: ", timezone.time_zones_for_number(mobileNo))
    print("Service provider: ", carrier.name_for_number(mobileNo, "en"))
    print("Country: ", geocoder.description_for_number(mobileNo, "en"))
else:
    print("Please enter valid phone number")