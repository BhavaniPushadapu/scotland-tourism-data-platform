import json
from datetime import datetime
from pathlib import Path

import requests

# Open-Meteo API
URL = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=55.9533"
    "&longitude=-3.1883"
    "&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
)

response = requests.get(URL)

if response.status_code == 200:
    print("✅ Connected successfully!")

    weather_data = response.json()

    # Create timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Ensure data/raw exists
    output_folder = Path("data/raw")
    output_folder.mkdir(parents=True, exist_ok=True)

    # Output file
    output_file = output_folder / f"weather_{timestamp}.json"

    # Save JSON
    with open(output_file, "w") as file:
        json.dump(weather_data, file, indent=4)

    print(f"✅ Weather data saved to: {output_file}")

else:
    print(f"❌ Error: {response.status_code}")