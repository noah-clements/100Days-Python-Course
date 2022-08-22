#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from notification_manager import NotificationManager
# from flight_data import FlightData
from flight_search import FlightSearch
from pprint import pprint

sheet_mgr = DataManager()
# sheet_data = [
#     {
#       "city": "Paris",
#       "iataCode": "PAR",
#       "lowestPrice": 54,
#       "id": 2
#     },
#     {
#       "city": "Berlin",
#       "iataCode": "BER",
#       "lowestPrice": 42,
#       "id": 3
#     },
#     {
#       "city": "Tokyo",
#       "iataCode": "TYO",
#       "lowestPrice": 485,
#       "id": 4
#     },
#     {
#       "city": "Sydney",
#       "iataCode": "SYD",
#       "lowestPrice": 551,
#       "id": 5
#     },
#     {
#       "city": "Istanbul",
#       "iataCode": "IST",
#       "lowestPrice": 95,
#       "id": 6
#     },
#     {
#       "city": "Kuala Lumpur",
#       "iataCode": "KUL",
#       "lowestPrice": 414,
#       "id": 7
#     },
#     {
#       "city": "New York",
#       "iataCode": "NYC",
#       "lowestPrice": 240,
#       "id": 8
#     },
#     {
#       "city": "San Francisco",
#       "iataCode": "SFO",
#       "lowestPrice": 260,
#       "id": 9
#     },
#     {
#       "city": "Cape Town",
#       "iataCode": "CPT",
#       "lowestPrice": 378,
#       "id": 10
#     },
#     {
#       "city": "Bali",
#       "iataCode": "DPS",
#       "lowestPrice": 501,
#       "id": 11
#     }
# ]
sheet_data = sheet_mgr.get_data()
# pprint(sheet_data)

# determine which cities need codes
need_codes = {row['id']: row['city'] for row in sheet_data if not row['iataCode']}
# print(need_codes)

#test FlightSearch.find_IATA_codes
# test_cities = [
#     'Paris',
#     'Berlin',
#     'Tokyo',
#     'Sydney',
#     'Istanbul',
#     'Kuala Lumpur',
#     'New York',
#     'San Francisco',
#     'Cape Town'
#     ]

flight_search = FlightSearch()
if len(need_codes) > 0:
    IATA_data = flight_search.find_IATA_codes(need_codes.values())
    print(IATA_data)
    for city in IATA_data:
        destination = list(filter(lambda destination: destination['city'] == city, sheet_data))
        # print(destination)
        # print(destination[0])
        destination[0]['iataCode'] = IATA_data[city]
        sheet_mgr.set_IATA(destination[0])
    # pprint(sheet_data)

#test best price flight search
city_codes = [row['iataCode'] for row in sheet_data]
# print(city_codes)
flights = flight_search.search_flights(city_codes)

#check low price and send texts
sms = NotificationManager()
users = sheet_mgr.get_user_emails()
for flight in flights:
    print(flight)
    destination = list(filter(lambda destination: destination['iataCode'] == flight.dest_city_IATA, sheet_data))[0]
    # print(destination)
    if flight.price <= destination['lowestPrice']:
        # print(f"sending sms for {flight}")
        sms.send_flight_alert(flight=flight)
        sms.send_emails(flight=flight, users=users)
        # for user in users:
        #     # print(f"sending email for {flight}")
        #     sms.send_flight_email(flight=flight, first_name=user['firstName'], 
        #                    last_name=user['lastName'], email=user['email'])
