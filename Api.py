#Create api method program bxb
#Facebook sidra_malik
import requests

URL = 'https://b-api.facebook.com/data'  

try:
    response = requests.get(URL)
    response.raise_for_status()  
    print("Response Content-Type:", response.headers['content-type'])
    print("Response Status Code:", response.status_code)
    with open('a.txt', 'w', encoding='utf-8') as file:
        file.write(response.text)
    if response.headers['content-type'] != 'application/json':
        print("Error: Response is not in JSON format.")
    else:
        data = response.json()  
        print(data)
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
except ValueError as e:
    print(f"Error parsing response as JSON: {e}")
