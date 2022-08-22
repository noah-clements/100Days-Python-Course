import requests
import toml

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self) -> None:
        config = toml.load(".project_config")
        self.sheet_headers = {
            "Authorization": config['Sheety']['Sheety_Auth']
        }
        self.end_point = "https://api.sheety.co/6e554546d51ae434c4a518b2f69806bd/flightDeals/"

    def get_data(self):
        response = requests.get(self.end_point + 'prices', headers=self.sheet_headers) 
        response.raise_for_status()
        # print(response.text)
        return response.json()['prices']

    def set_IATA(self, destination:dict) -> None:
        row_id = destination['id']
        parameters = {
            "price" : {
                "iataCode": destination['iataCode']
            }
        }
        response = requests.put(url=f"{self.end_point}/{row_id}", 
                                headers=self.sheet_headers, 
                                json=parameters)
        response.raise_for_status()
        print(response.text)

    def get_user_emails(self):
        response = requests.get(self.end_point + 'users', headers=self.sheet_headers) 
        response.raise_for_status()
        # print(response.text)
        return response.json()['users']
        