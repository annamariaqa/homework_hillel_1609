import requests
import json
from requests.adapters import HTTPAdapter

session = requests.Session()

adapter = HTTPAdapter(max_retries=3)

session.mount('http://', adapter)
# session.mount('https://', adapter)

response = session.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos')

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    photos = data["photos"]
    for photo in photos:
        response = requests.get(photo["img_src"])
        with open(f"mars_photo{photo['id']}.jpg", 'wb') as file:
            file.write(response.content)

else:
    print('Помилка запиту:', response.status_code)
