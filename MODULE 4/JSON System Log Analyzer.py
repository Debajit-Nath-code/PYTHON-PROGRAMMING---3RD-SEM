import json

event_list = [
    {"event": "Login", "status": "Success"},
    {"event": "Upload", "status": "Success"},
    {"event": "Payment", "status": "Failed"},
    {"event": "Logout", "status": "Success"}
]

with open("logs.json", "w") as out_json:
    json.dump(event_list, out_json, indent=4)

with open("logs.json", "r") as in_json:
    records = json.load(in_json)

ok_count = 0
fail_count = 0

for item in records:
    if item["status"] == "Success":
        ok_count += 1
    else:
        fail_count += 1

print("Total Logs:", len(records))
print("Successful Events:", ok_count)
print("Failed Events:", fail_count)
