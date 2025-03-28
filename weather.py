import requests

# Replace 'your_api_key' with your actual API key
key = "54d6a02800b5f582abdc56225fca59b2"
api_address = f"http://api.openweathermap.org/data/2.5/weather?q=Kadapa&appid={key}"
json_data = requests.get(api_address).json()

def temp():
    temperature = round(json_data["main"]["temp"]-273,1)
    return temperature

def des():
    description = json_data["weather"][0]["description"]
    return description

# print(temp())
# print(des())