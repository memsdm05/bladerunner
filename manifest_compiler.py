from configparser import SectionProxy
import sys
import json
import re

if len(sys.argv) != 3:
    exit(1)

output = {
    "shots": [],
    "sections": [],
}

shots = output["shots"]
sections = output["sections"]

# parse shots
with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.strip()
        if line.startswith(";") or line == "":
            continue

        parts = line.split(" ")
        shots.append({
            "frame": int(parts[0]),
            "distance": parts[1],
            "angle": {
                "la": "Low Angle",
                "ha": "High Angle",
                "el": "Eye Level"
            }[parts[2]],
            "special": len(parts) > 3
        })

        print(shots[-1])


# parse sections
HEADER_PATTERN = re.compile(r"\((\d*)\) ([\w \']*)")
with open(sys.argv[2], "r", encoding='utf-8') as f:
    while True:
        header = HEADER_PATTERN.match(f.readline())
        if not header: continue
        end, title = int(header.group(1)), header.group(2)

        body = ""
        while (body_line := f.readline()) != "\n":
            body_line = body_line.strip()
            body_line = re.sub()
            body += body_line.strip() + "<br><br>"

        sections.append({
            "title": title,
            "start": sections[-1]["end"] if len(sections) > 0 else 0,
            "end": end,
            "body": body
        })

        print(sections[-1])

        if f.readline() == "":
            break
        


# output
shots.sort(key=lambda s: s["frame"])
sections.sort(key=lambda s: s["end"])
with open("manifest.json", "w") as f:
    json.dump(output, f, indent=2)

print("\ndone")