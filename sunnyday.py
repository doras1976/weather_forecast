import requests, pprint

# apikey = 741e1ad8a03bb12d0fabb6a8d65c4df0


class Weather:
    """
    Creates a Weather object getting an apikey as input
    and either a city name or lat and lon coordinates.
    You can get your own apikey from https://openweathermap.org
    """

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

        if self.data['cod'] != '200':
            raise ValueError(self.data['message'])

    def next_12h(self):
        return self.data['list'][:4]

    def next_12h_simplified(self):
        simple_data_list = []
        for item in self.data['list'][:4]:
            simple_data_list.append((item['dt_txt'], item['main']['temp'], item['weather'][0]['description']))
        return simple_data_list


# weather = Weather(apikey="741e1ad8a03bb12d0fabb6a8d65c4df0", city="Madrid")
# weather = Weather(apikey="741e1ad8a03bb12d0fabb6a8d65c4df0", lat=4.1, lon=4.5)
# weather = Weather(apikey="741e1ad8a03bb12d0fabb6a8d65c4df0")
#
# print(weather.next_12h())

try:
    # Example with missing inputs
    weather = Weather(apikey="741e1ad8a03bb12d0fabb6a8d65c4df0", city="aaa")
    # pprint.pprint(weather.next_12h())
    pprint.pprint(weather.next_12h_simplified())

except ValueError as e:
    print(e)
