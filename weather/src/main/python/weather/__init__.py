import requests
import xmltodict

BERLIN = '20065563'
WEATHER_API_ENDPOINT = 'http://weather.yahooapis.com/forecastrss?w={0}&u=c'


def request_weather_for(location_id):
    endpoint = WEATHER_API_ENDPOINT.format(location_id)

    request = requests.get(endpoint)
    request_successful = request.status_code == requests.codes.ok
    if not request_successful:
        raise RuntimeError("Cannot get weather for {0}, response was {1}".format(
            location_id, request.text))

    return xmltodict.parse(request.text)


if __name__ == '__main__':
    import json
    print json.dumps(request_weather_for(BERLIN), indent=4)
