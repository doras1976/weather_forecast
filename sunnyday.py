import requests

# apikey = 741e1ad8a03bb12d0fabb6a8d65c4df0


class Weather:

    def __init__(self, apikey, city=None, lat=None, lon=None):
        if city:
            params = {'q': city}
        elif lat and lon:
            params = {'lat': lat, 'lon': lon}
        else:
            raise ValueError("You should enter either city name, or lat and lon values")

        params.update({
            'appid': apikey,
            'units': 'imperial'
        })

        url = "https://api.openweathermap.org/data/2.5/forecast"
        response = requests.get(url, params=params)
        self.data = response.json()

    def next_12h(self):
        return self.data['list'][:4]

    def next_12h_simplified(self):
        pass


# weather = Weather(apikey="741e1ad8a03bb12d0fabb6a8d65c4df0", city="Madrid")
# weather = Weather(apikey="741e1ad8a03bb12d0fabb6a8d65c4df0", lat=4.1, lon=4.5)
# weather = Weather(apikey="741e1ad8a03bb12d0fabb6a8d65c4df0")
#
# print(weather.next_12h())

try:
    # Example with missing inputs
    weather = Weather(apikey="741e1ad8a03bb12d0fabb6a8d65c4df0")
    print(weather.next_12h())
except ValueError as e:
    print(e)
