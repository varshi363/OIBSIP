import requests

def main():
    location = input("Enter the city name you want weather info for: ").strip()
    if not location:
        print("Location cannot be empty.Enter positive text")

    api_key = "4f53f08db2535f778a03c3d673156395"
    url = "https://api.openweathermap.org/data/2.5/weather"

    arg_dict = {"q": location,"appid": api_key, "units": "metric"}

    try:
        max_wait = 20
        fetch_result = requests.get(url, params=arg_dict, timeout = max_wait)
        stream = fetch_result.json()

        working = stream.get("cod") == 200
        if not working:
            print("Oops! City not found. Try again!!!!")
        else:
            stats = stream["main"]
            forecast = stream["weather"][0]
            temp_cel = stats["temp"]
            temp_far = temp_cel * 9/5 + 32
            humid = stats["humidity"]
            status = forecast["description"]

            print("Climate of:" ,location)
            print(f"Temperature right now: {temp_cel}°C / {temp_far:.1f}°F")
            print(f"Humidity level: {humid}%")
            print("Atmospheric Condition:" ,status)

    except requests.exceptions.RequestException:
        print("Umm....seems like your internet is off.")

if __name__ == "__main__":
    main()
