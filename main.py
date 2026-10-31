import csv
import time
import requests

url = "https://rickandmortyapi.com/api/character"
characters = []

session = requests.Session()

while url:
    response = session.get(url, timeout=10)

    # אם נחסמנו, מחכים ומנסים שוב את אותו עמוד
    if response.status_code == 429:
        wait = int(response.headers.get("Retry-After", 5))
        print(f"429 - waiting {wait} seconds...")
        time.sleep(wait)
        continue

    response.raise_for_status()
    data = response.json()

    for character in data["results"]:
        if (
            character["species"] == "Human"
            and character["status"] == "Alive"
            and character["origin"]["name"].startswith("Earth")
        ):
            characters.append({
                "Name": character["name"],
                "Location": character["location"]["name"],
                "Image": character["image"],
            })

    url = data["info"]["next"]
    time.sleep(0.5)  # הפסקה קטנה בין בקשות

with open("characters.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Location", "Image"])
    writer.writeheader()
    writer.writerows(characters)

print(f"Found {len(characters)} characters.")
print("Results saved to characters.csv")
