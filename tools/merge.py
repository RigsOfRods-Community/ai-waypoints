import json
import os

data = []

for filename in os.listdir("waypoints"):
    print(filename)
    f = open(os.path.join(os.getcwd(), "waypoints", filename), "r")
    data.append(json.loads(f.read()))
    f.close()

waypoints = open(os.path.join(os.getcwd(), "publish", "waypoints.json"), "w")
waypoints.write(json.dumps(data))
waypoints.close()
