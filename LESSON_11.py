import json, requests

url = "http://api.giphy.com/v1/gifs/search"

query_params = input()
resp = requests.get(
    url, 
    params={
        "q": f"{query_params}",
        "api_key": "iVK5WCK3L5e970meRCfV7UaSgGRb6dDQ",
        "limit": 5,
        "offset": 5,
        "lang": "en",
        "rating": "g"

    }
)
result = resp.json()['data'][0]['url']
try:
  print(f'STATUS_CODE = {resp.status_code}, your GIF - {result}')
except IndexError:
  pass
