import json

settings = {
    "volume": 75,
    "language": "en"
}

with open("settings.json", "w", encoding="utf-8") as file:
    json.dump(settings, file, indent=4)