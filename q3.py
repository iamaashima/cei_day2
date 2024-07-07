import json

# Sample JSON data as a string
eg_json = '''
{
    "date": "2023-12-31",
    "explanation": "This is a sample explanation of the Astronomy Picture of the Day",
    "title": "Sample Title",
    "url": "https://apod.nasa.gov/apod/image/2312/sample_image.jpg"
}
'''

# Parse the JSON string
eg_data = json.loads(eg_json)

# Print the keys "explanation" and "title"
print("Explanation:", eg_data.get("explanation", "Key not found"))
print("Title:", eg_data.get("title", "Key not found"))

# Print the initial data (ensure to print the dictionary, not the JSON string)
print("Initial Data:", json.dumps(eg_data, indent=4))

# Add a new key-value pair
eg_data["photographer"] = "Aashima"
print("After adding photographer:", json.dumps(eg_data, indent=4))

# Print all key-value pairs
print("\nAll key-value pairs:")
for key, value in eg_data.items():
    print(f"{key}: {value}")
