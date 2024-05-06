import requests
from datetime import datetime

TOKEN = "token"
USER_NAME = "user_name"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": "graph01",
    "name": "Study Time Graph",
    "unit": "min",
    "type": "int",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


GRAPH_ID = "graph01"

post_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# today = datetime(year=2024, month=5, day=5)
# print(today.strftime("%Y%m%d"))

quantity = input("How many minutes did you study today? :")


post_pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": quantity,
}

response = requests.post(url=post_pixel_endpoint, json=post_pixel_config, headers=headers)
print(response.text)


# update_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"

# update_pixel_config = {
#     "quantity": "150",
# }

# response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
# print(response.text)


# response = requests.delete(url=update_pixel_endpoint, headers=headers)
# print(response.text)
