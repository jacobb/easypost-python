import easypost
easypost.api_key = 'API KEY'

types = easypost.CarrierAccount.types()

for carrier_type in types:
    print carrier_type.type
