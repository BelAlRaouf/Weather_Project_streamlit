import requests

API_KEY = "87734298fc1db6da250ef5a13409bf4c"


def get_data(locations, days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={locations}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 2*days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    test = get_data(locations="Toronto", days=3, temperature_option="Temperature")
    print(len(test))
