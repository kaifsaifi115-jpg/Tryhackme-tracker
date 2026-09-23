import json
from datetime import datetime

DATA_FILE = "data/progress.json"

with open(DATA_FILE, "r") as file:
    data = json.load(file)

data["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
data["total_rooms"] = len(data["rooms_completed"])

with open(DATA_FILE, "w") as file:
    json.dump(data, file, indent=4)

print("TryHackMe tracker updated!")
print(f"Rooms completed: {data['total_rooms']}")