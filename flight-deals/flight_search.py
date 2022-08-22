import requests
import toml
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from flight_data import FlightData
import bitlyshortener

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self, base_city='BOS') -> None:
        config = toml.load(".project_config")
        self.api_headers = {
            "apikey": config['Kiwi']['api_key']
        }
        self.end_point = "https://tequila-api.kiwi.com"
        self.base_city = base_city
        self.bitly_token = config['bitly']['token']

    def find_IATA_codes(self, cities: list) -> dict:
        locations_point = "/locations/query"
        codes = {city:'' for city in cities}
        parameters = {
            "location_types": "city",
            "limit": "1"        
        }
        for city in cities:
            parameters['term'] = city
            response = requests.get(f"{self.end_point}{locations_point}", headers=self.api_headers, params=parameters)
            response.raise_for_status()
            city_info = response.json()['locations'][0]
            # print(f"{city_info['name']}: {city_info['code']}")
            codes[city] = city_info['code']
        return codes

    def search_flights(self, destinations: list, stopovers=0):
        # setup url shortener for links to flights
        shortener = bitlyshortener.Shortener(tokens=[self.bitly_token])
        
        search_point = "/v2/search"
        starting_date = date.today()
        last_date = starting_date + relativedelta(months=6)
        parameters = {
            "fly_from": self.base_city,
            "fly_to": ",".join(destinations),
            "date_from": starting_date.strftime("%d/%m/%Y"),
            "date_to": last_date.strftime("%d/%m/%Y"),
            "curr": "USD",
            "max_stopovers": stopovers, 
            "only_working_days": "false",
            "only_weekends": "false",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "max_fly_duration": 30,
            "one_for_city": 1            
        }
        response = requests.get(f"{self.end_point}{search_point}", headers=self.api_headers, params=parameters)
        response.raise_for_status()
        data = response.json()['data']
        flights = []
        found_destinations = []
        for flight in data:
            via_city = ""
            if stopovers > 0:
                via_city  = flight['route'][0]['cityTo']
            # print(datetime.fromisoformat(flight['local_departure'].strip('Z')))
            flight_data = FlightData(to_city=flight['cityTo'],
                                     to_city_code=flight['cityCodeTo'], 
                                     to_airport=flight['flyTo'],
                                     departure_time=datetime.fromisoformat(flight['local_departure'].strip('Z')),
                                     nights_in_dest=flight['nightsInDest'],
                                     price=flight['price'], stop_overs=stopovers,
                                     via_city=via_city, 
                                     link_to_flight=shortener.shorten_urls([flight['deep_link']])[0])
            flights.append(flight_data)
            found_destinations.append(flight['cityCodeTo'])
            # print(flight_data)

            # check to make sure that there are flights for all destinations
            # if not, allow one stopover and check again
        rechecks = [i for i in destinations if i not in found_destinations]
        if len(rechecks) > 0 and stopovers == 0:
            flights = flights + self.search_flights(rechecks, stopovers=1)
        return flights        
        
        