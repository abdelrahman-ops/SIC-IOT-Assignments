import requests

# Define the data to be sent as a dictionary, json
data_to_send = {
    "key1": "value1",
    "key2": "value2",
}

# Send a POST request to Node.js server
response = requests.post('http://localhost:3000/api/data', json=data_to_send)

# Print the response from the server
print(response.json())
