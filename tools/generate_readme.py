import json
import os


readmefile = open("README.md", "r")
readme = readmefile.read()
readmefile.close()

readme = readme.replace("publish/map_preview.png?raw=true", "map_preview.png")

readme += """
# Terrains with waypoint presets

| terrain | preset | Ammount of waypoints |
| ----------- | ----------- | ----------- |
"""
for filename in os.listdir("waypoints"):
    f = open(os.path.join(os.getcwd(), "waypoints", filename), "r")
    d = json.loads(f.read())
    f.close()
    terrain = d["terrain"]
    preset = d["preset"]
    waypoints = len(d["waypoints"])
    readme += f"|{terrain}|{preset}|{waypoints}|\n"
    
readmefile = open(os.path.join(os.getcwd(), "publish", "README.md"), "w")
readmefile.write(readme)
readmefile.close()