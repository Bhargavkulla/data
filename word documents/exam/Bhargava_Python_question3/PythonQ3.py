import requests
API_KEY = "8f2d6822fb2e4524adf20f8132e6f463"
city = input("Enter city name: ")
 
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
 
response = requests.get(url).json()
 
if response["cod"] == 200:
    print(f"\nCity: {response['name']}")
    print(f"Temperature: {response['main']['temp']}°C")
    print(f"Weather: {response['weather'][0]['description']}")
else:
    print("\nCity not found!")