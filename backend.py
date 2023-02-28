import requests

API_KEY = "87734298fc1db6da250ef5a13409bf4c"


def get_data(locations, days=None, temperature_option = None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={locations}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data


if __name__ == "__main__":
    test = get_data(locations="Toronto")
    print(test)
