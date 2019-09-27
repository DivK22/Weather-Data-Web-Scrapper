import requests
from pprint import pprint
def weather_data(query):
	res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=39b3a60227122ac5bd28709b124d1dc8&units=metric')
	return res.json();
def print_weather(result,city):
    print("Temperature: {}°C ".format(result['main']['temp']))
    print("Wind speed: {} m/s".format(result['wind']['speed']))
    print("Pressure: {} mbar".format(result['main']['pressure']))
    print("Humidity: {}".format(result['main']['humidity']))
    print("Description: {}".format(result['weather'][0]['description']))
    print("Weather: {}".format(result['weather'][0]['main']))
def main():
	city=input('Enter the city:')
	print()
	try:
	  query='q='+city
	  w_data=weather_data(query)
	  print_weather(w_data, city)
	  print()
	except:
	  print('City name not found...')
if __name__=='__main__':
	main()
