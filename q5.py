import requests

url = "http://api.open-notify.org/iss-now.json"
try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        latitude = data['iss_position']['latitude']
        longitude = data['iss_position']['longitude']
        timestamp = data['timestamp']

        print(f'Longitude: {longitude}')
        print(f'Latitude: {latitude}')
        print(f'TimeStamp: {timestamp}')

    else:
        print("Failed to retrieve data", response.status_code)

except requests.exceptions.RequestException as e:
    print("Error in fetching data", e)
