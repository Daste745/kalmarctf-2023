import json

with open("packets.json") as f:
    packets = json.load(f)

data_points = []
for packet in packets:
    layers = packet["_source"]["layers"]
    data = layers["data"]["data.data"]

    data_points.append(data)

with open("output.json", "w") as f:
    json.dump(data_points, f, indent=2)
