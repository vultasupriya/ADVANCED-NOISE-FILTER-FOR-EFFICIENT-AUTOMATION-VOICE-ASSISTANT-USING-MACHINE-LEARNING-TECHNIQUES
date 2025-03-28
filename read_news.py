import requests

# Replace 'your_api_key' with your actual API key
key = "cc049cc879ae444089630802dd72b7af"
api_address = f"http://newsapi.org/v2/top-headlines?country=us&apikey={key}"
json_data = requests.get(api_address).json()

ar = []

def news():
    for i in range(min(3, len(json_data.get("articles", [])))):
        ar.append("number " + str(i+1) + ": " + json_data["articles"][i]["title"] + ".")
    return ar

# arr = news()
# print(arr)
