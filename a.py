import requests

url = "https://graphhopper.com/api/1/route"

query = {
  "key": "5b42b4d3-18a2-4b21-b6e5-d63af51def79"
}

payload = {
  "profile": "bike",
  "points": [
    [
      11.539421,
      48.118477
    ],
    [
      11.559023,
      48.12228
    ]
  ],
  "point_hints": [
    "Lindenschmitstraße",
    "Thalkirchener Str."
  ],
  "snap_preventions": [
    "motorway",
    "ferry",
    "tunnel"
  ],
  "details": [
    "road_class",
    "surface"
  ],
  "algorithm": "alternative_route"
}

headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers, params=query)

data = response.json()
print(data)