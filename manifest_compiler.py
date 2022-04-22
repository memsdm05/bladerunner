import sys
import json

if len(sys.argv) != 3:
    exit(1)

output = {
    "shots": [],
    "sections": [],
}

# parse shots
with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.strip()
        if line.startswith(";") or line == "":
            continue

        parts = line.split(" ")
        print(parts)
        output["shots"].append({
            "frame": int(parts[0]),
            "distance": parts[1],
            "angle": {
                "la": "Low Angle",
                "ha": "High Angle",
                "el": "Eye Level"
            }[parts[2]],
            "special": len(parts) > 3
        })

output["shots"].sort(key=lambda s: s["frame"])

# parse sections


# output
with open("manifest.json", "w") as f:
    json.dump(output, f, indent=2)