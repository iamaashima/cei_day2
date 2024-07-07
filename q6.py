import requests
import pandas as pd
import time

url = "http://api.open-notify.org/iss-now.json"
records = []
num_records = 100

for i in range(num_records):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            latitude = data['iss_position']['latitude']
            longitude = data['iss_position']['longitude']
            timestamp = data['timestamp']

            records.append({
                'timestamp': timestamp,
                'latitude': latitude,
                'longitude': longitude
            })

        else:
            print("Failed to retrieve data", response.status_code)

    except requests.exceptions.RequestException as e:
        print("Error in fetching data", e)

    time.sleep(1)

#print(records)

# Create a pandas DataFrame from the records list
df = pd.DataFrame(records)
print(df.head(5))

# Save the DataFrame to a CSV file
df.to_csv('iss_location_data.csv', index=False)

print("Data saved to iss_location_data.csv")
