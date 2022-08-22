import requests
import toml
from datetime import date

pixela_endpoint = "https://pixe.la/v1/users"

config = toml.load(".python_config")

user_params = {
    "token": config['pixela']['token'],
    "username": config['pixela']['username'],
    "agreeTermsofService": "yes",
    "notMinor": "yes"
}

# response = requests.post(pixela_endpoint,json=user_params)
# print(response.text)

graph_config = {
    # "id": config['pixela']['graph_id'],
    "name": "Exercise",
    "unit": "minutes",
    "type": "int",
    "color": "sora"
}

header = {
    "X-USER-TOKEN": config['pixela']['token']
}

graph_endpoint = f"{pixela_endpoint}/{config['pixela']['username']}/graphs"
# response = requests.post(graph_endpoint, json=graph_config, headers=header)
# print(response.text)

today = date.today()
pixel_create_url = f"{graph_endpoint}/{config['pixela']['graph_id']}"
pixel_data = {
    "date": today.strftime("%Y%m%d"), 
    "quantity": "65"    
}

# update graph info
# response = requests.put(url=pixel_create_url, headers=header, json=graph_config)

# add data-point/pixel
# response = requests.post(url=pixel_create_url, headers=header, json=pixel_data)

update_data = {"quantity": "30"}
# update pixel
# response = requests.put(url=f"{pixel_create_url}/20220702", headers=header, json=update_data)

# delete pixel
response = requests.delete(url=f"{pixel_create_url}/{today.strftime('%Y%m%d')}", headers=header)

print(response.text)